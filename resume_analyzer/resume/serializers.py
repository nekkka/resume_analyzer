from rest_framework import serializers
from .models import Resume
from rest_framework import serializers
from bson import ObjectId

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['id', 'resume_file', 'uploaded_at']
        read_only_fields = ['id', 'uploaded_at']




class ObjectIdSerializer(serializers.Serializer):
    def to_representation(self, value):
        if isinstance(value, ObjectId):
            return str(value)
        return value
