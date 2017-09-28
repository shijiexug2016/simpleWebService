from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
# Create your views here.

@csrf_protect
def index(request):
    templateName = 'abstractEvaluate/index.html'
    '''
    #template = loader.get_template('abstractEvaluate/index.html')
    if request.method == 'POST':
        text = request.POST.get("abstract")
        #print(request.schema)
        print(request.body)
        #print(text)
        #result = {'MAH': True, "reportable": False}
        result = {'text': text}
        context = {'result': result}
        return render(request, templateName, context)
    '''
    return render(request, templateName)