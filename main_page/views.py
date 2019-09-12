from django.shortcuts import render
from main_page.models import Project, Job, Skill

# Create your views here.
def main_page(request):
    skills = Skill.objects.all()
    context = {
        'skills': skills
    }
    return render(request, 'main_page.html', context)