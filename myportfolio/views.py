from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import contact, education, experience, projects

def index(request):
    template = loader.get_template('index.html')
    context = {
        'name': "Benjamin Loh Choon How",
        'course': 'Bachelor of Science with Honours in Computing Science',
        'profilePic': '/images/profile.jpg',
        'description': 'With a passion for Technology, I have both the skill set and professional background necessary to dive deep into the Tech world.'
                       ' As an upbeat, self-motivated team player with excellent communication and critical thinking skills as well as being a reliable team leader,'
                       ' I envision an exciting future in the industry. Browse my site and connect with me on LinkedIn to see all that I have to offer!',
        'email': 'xrando20@gmail.com',
        'phone': 92731310,
        'skills': ['Python', 'Java', 'C++', 'HTML', 'CSS', 'JavaScript', 'SQL', 'Django'],
        'projects': [
            {
                'title': 'Project 1',
            },
            {
                'title': 'Project 2',
            },
        ],
        'experience': [
            {
                'duration': 'August 2021–July 2022',
                'company': 'Commerce Online Pte Ltd',
                'position': 'Software Developer',
                'skills': 'C# , ASP.NET , SharePoint, Powershell Scripting',
            },
            {
                'duration': 'July 2019–July 2021',
                'company': 'Singapore Armed Forces (SAF)',
                'position': 'Enlistee',
            },
            {
                'duration': 'March 2018–May 2018',
                'company': 'ST Electronics (Info-Comm Systems)',
                'position': 'Software Support Engineer Intern',
                'skills': 'Scripting in C, Regression Testing, Software Debugging, Software Documentation',
            },
        ],
        'education': [
            {
                'school': 'Singapore Institute of Technology & University of Glasgow',
                'certification': 'Bachelor of Science with Honours in Computing Science, Specialise in the Internet of Things (IoT)',
                'duration': '2022-2025',
            },
            {
                'school': 'Nanyang Polytechnic',
                'certification': 'Diploma in Infocomm & Security (Specialization in Network Security)',
                'duration': '2016-2019',
            },
            {
                'school': 'Ahmad Ibrahim Secondary School',
                'certification': 'GCE O Level',
                'duration': '2012-2015',
            }
        ],
    }

    return HttpResponse(template.render(context, request))
