from django.shortcuts import render

#----front page
def index(request):
    return render(request, 'core/index.html')

#---about page
def about(request):
    return render(request, 'core/about.html')
