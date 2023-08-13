from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import contact, education, experience, projects
from pymongo import MongoClient

#init mongodb
client = MongoClient('mongodb://localhost:27017/')
db = client['portfolio']

def index(request):
    template = loader.get_template('index.html')
    #get data from mongodb
    contact = db.myportfolio_contact.find()
    education = db.myportfolio_education.find()
    experience = db.myportfolio_experience.find()
    projects = db.myportfolio_projects.find()
    awards = db.myportfolio_awards.find()
    context = {
        'name': contact[0]['name'],
        'course': contact[0]['course'],
        'profilePic': contact[0]['profilePic'],
        'description': contact[0]['description'],
        'email': contact[0]['email'],
        'phone': contact[0]['phone'],
        'linkedinLink': contact[0]['linkedinLink'],
        'githubLink': contact[0]['githubLink'],
        'skills': contact[0]['skills'],
        'project': projects[0]['projects'],
        'experience': experience[0]['experience'],
        'education': education[0]['education'],
        #'awards': awards[0]['awards'],
    }

    return HttpResponse(template.render(context, request))
