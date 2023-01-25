from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse("this is my homepage (/)")
    vars = {'name':'shivam','course':'django'}
    return render(request, 'home.html',vars)

def about(request):
    # return HttpResponse("this is my aboutpage (/)")
    return render(request, 'about.html')
def projects(request):
    # return HttpResponse("this is my projectspage (/)")
    return render(request, 'projects.html')

def contact(request):
    # return HttpResponse("this is my contactpage (/)")
    return render(request, 'contact.html')
