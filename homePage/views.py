from django.shortcuts import render

# Create your views here.
def homePage(request):
    templateName = 'homePage/base.html'
    return render(request, templateName)