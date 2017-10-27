from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from keras.models import load_model
# Create your views here.

@csrf_exempt
def evaluateAbstract(request):
    if request.method == "POST":
        try:
            print(request)
            abstractText = str(request.POST.get("abstractText"))
        except KeyError:
            return HttpResponse('Error')  # incorrect post

        reportable = False
        if len(abstractText) > 20:
            reportable = True

        response_data = {'reportable' : reportable}
        return JsonResponse(response_data)
    response = HttpResponse()
    response.write("<h1>Please send post request through evaluate</h1>")
    return response

