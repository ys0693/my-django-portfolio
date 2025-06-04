# intro/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

# 지금 당장 필요한 skills 뷰를 아래에 추가
def skills(request):
    return render(request, 'skills.html')

def projects(request):
    return render(request, 'projects.html')

def performance(request):
    return render(request, 'performance.html')

def aspiration(request):
    return render(request, 'aspiration.html')
