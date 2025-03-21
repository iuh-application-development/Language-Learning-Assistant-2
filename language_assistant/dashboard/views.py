from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'dashboard/index.html')

def about(request):
    return render(request, 'dashboard/about.html')

def courses(request):
    return render(request, 'dashboard/courses.html')

def team(request):
    return render(request, 'dashboard/team.html')

def testimonial(request):
    return render(request, 'dashboard/testimonial.html')
    
def contact(request):
    return render(request, 'dashboard/contact.html')


