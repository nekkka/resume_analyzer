from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from bson import ObjectId  
from .models import Resume, ResumeAnalysis
from .serializers import ResumeSerializer
from .utils import extract_text_from_pdf, extract_text_from_docx, analyze_resume_text, save_analysis_to_mongo

import json

class ResumeUploadView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            resume = serializer.save(user=request.user)

            file = resume.resume_file
            if file.name.endswith('.pdf'):
                text = extract_text_from_pdf(file)
            elif file.name.endswith('.docx'):
                text = extract_text_from_docx(file)
            else:
                return Response({'error': 'Unsupported file format'}, status=400)


            analysis_data = analyze_resume_text(text)
            analysis_data_str = json.dumps(analysis_data, default=str)
            save_analysis_to_mongo(analysis_data, request.user.email)
            ResumeAnalysis.objects.create(resume=resume, analysis_data=analysis_data_str)



            short_analysis = {
                "skills": analysis_data.get("skills", []),
                "experience": analysis_data.get("experience_summary", ""),
            }

            return Response({
                'message': 'Resume uploaded and analyzed successfully',
                'analysis_data': short_analysis 
            }, status=201)

        return Response(serializer.errors, status=400)
