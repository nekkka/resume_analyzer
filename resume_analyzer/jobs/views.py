from rest_framework import generics, permissions
from .models import Job
from .serializers import JobSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .matching import get_matching_jobs_for_user
from resume.utils import get_resume_analysis_for_user


class JobCreateView(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]  

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


"""class JobMatchingView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        resume_analysis = get_resume_analysis_for_user(user.email)
        user_skills = resume_analysis.get('skills', [])

        if not user_skills:
            return Response({"matches": [], "reason": "No skills found in resume"}, status=200)

        normalized_user_skills = set(skill.lower() for skill in user_skills)

        matches = []

        for job in Job.objects.all():
            job_skills = job.required_skills.split(',')
            job_skills = set(skill.strip().lower() for skill in job_skills)

            if normalized_user_skills & job_skills: 
                matches.append(JobSerializer(job).data)

        return Response({"matches": matches})"""


class JobMatchingView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        resume_analysis = get_resume_analysis_for_user(user.email)  # получаем анализ резюме пользователя

        user_skills = resume_analysis.get('skills', [])  # извлекаем навыки из анализа

        if not user_skills:
            return Response({"matches": [], "reason": "No skills found in resume"}, status=200)

        normalized_user_skills = set(skill.lower() for skill in user_skills)  # нормализуем навыки (в нижний регистр)

        matches = []

        for job in Job.objects.all():  # проходим по всем вакансиям
            job_skills = job.required_skills.split(',')  # разделяем навыки вакансии (если они в строке через запятую)
            job_skills = set(skill.strip().lower() for skill in job_skills)  # нормализуем и создаем множество

            if normalized_user_skills & job_skills: 
                matches.append(JobSerializer(job).data)

        return Response({"matches": matches})




class JobListView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer