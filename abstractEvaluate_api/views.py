from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.views.decorators.csrf import csrf_protect
# Create your views here.

@csrf_protect
def evaluateAbstract(request):
    #template = loader.get_template('abstractEvaluate/index.html')
    if request.method == 'POST':
        #templateName = 'abstractEvaluate/index.html'
        text = request.POST.get("abstract")
        result = {'MAH': False, 'reportable' : False}
        print(text)
        textLength = len(text)
        if (textLength < 5):
            result['MAH'] = False
            result['reportable'] = False
        elif (textLength >= 5 and textLength <= 8):
            result['MAH'] = True
            result['reportable'] = False
        else:
            result['MAH'] = True
            result['reportable'] = True
        context = {'result': result}
        return render(request, 'abstractEvaluate/index.html', context)
    response = HttpResponse()
    response.write("<h1>please set post request through evaluate</h1>")
    return response

