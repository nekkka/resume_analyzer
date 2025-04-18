from pymongo import MongoClient
from django.conf import settings
from .models import Job

client = MongoClient(settings.MONGO_URI)
db = client[settings.MONGO_DB_NAME]
analysis_collection = db['analyses']

def calculate_match_score(resume_skills, job_required_skills):
    if not resume_skills or not job_required_skills:
        return 0

    resume_skills_set = set(skill.lower() for skill in resume_skills)
    job_skills_set = set(skill.strip().lower() for skill in job_required_skills.split(','))

    matched_skills = resume_skills_set & job_skills_set
    score = len(matched_skills) / len(job_skills_set) * 100
    return round(score, 2)

def get_matching_jobs_for_user(user_id):
    analysis = analysis_collection.find_one({'user_id': user_id}, sort=[('_id', -1)])
    if not analysis:
        return []

    resume_skills = analysis.get('skills', [])
    jobs = Job.objects.all()
    matching_jobs = []

    for job in jobs:
        score = calculate_match_score(resume_skills, job.required_skills)
        if score > 0:
            matching_jobs.append({
                'job_id': job.id,
                'title': job.title,
                'description': job.description,
                'location': job.location,
                'required_skills': job.required_skills,
                'match_score': score,
            })

    # Отсортировать по убыванию score
    matching_jobs.sort(key=lambda x: x['match_score'], reverse=True)
    return matching_jobs
