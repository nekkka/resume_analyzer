from pymongo import MongoClient
from django.conf import settings
import nltk
import spacy
from PyPDF2 import PdfReader
from docx import Document
import re

client = MongoClient(settings.MONGO_URI)
db = client[settings.MONGO_DB_NAME]
collection = db['analyses']


nlp = spacy.load('en_core_web_sm')



def save_analysis_to_mongo(data):
    collection.insert_one(data)


def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)  
    text = ''
    for page in reader.pages:
        text += page.extract_text() or ''
    return text


def extract_text_from_docx(docx_file):
    doc = Document(docx_file)
    text = ""
    for para in doc.paragraphs:
        text += para.text
    return text




def analyze_resume_text(text):
    doc = nlp(text)

    entities = [{'text': ent.text, 'label': ent.label_} for ent in doc.ents]
    words = nltk.word_tokenize(text)
    skills = extract_skills_from_text(text)
    experience = extract_experience_from_text(text)
    
    return {
        'entities': entities,
        'words': words,
        'skills': skills,
        'experience_summary': experience
    }


def extract_skills_from_text(text):
    skill_keywords = [
        'Python', 'Django', 'JavaScript', 'Java', 'SQL', 'HTML', 'CSS', 'React', 'Node.js', 'AWS', 'Docker'
    ]
    skills = []
    for keyword in skill_keywords:
        if keyword.lower() in text.lower():
            skills.append(keyword)
    return skills




def extract_experience_from_text(text):
    
    experience_keywords = [
        'experience', 'worked as', 'developed', 'managed', 'designed', 'led'
    ]
    experience = []
    

    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        if any(keyword in sentence.lower() for keyword in experience_keywords):
            experience.append(sentence)
    
    return ' '.join(experience) 

