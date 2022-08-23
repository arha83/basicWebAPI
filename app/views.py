from django.views.decorators.csrf import csrf_exempt
from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from grpc import Status
from .models import Var
import json

# Create your views here.


def index(request):
    return render(request, 'index.html')

def apiRoot(request):
    return render(request, 'apiRoot.html')

@csrf_exempt
def varsList(request):
    if request.method == 'GET':
        vars = Var.objects.all()
        return JsonResponse(list(vars.values()), safe=False)

    elif request.method == 'POST':
        data = request.body.decode('utf-8')
        data = json.loads(data)

        text= data.get('text') if data.get('text') != None else ''
        num= data.get('num') if data.get('num') != None else 0
        bit= data.get('bit') if data.get('bit') != None else False
        try:
            var = Var(text=text, num=num, bit=bit)
            var.save()
        except:
            return HttpResponse(status=400)
        vars = Var.objects.all()
        return JsonResponse(list(vars.values()), safe=False, status= 201)

    else: return HttpResponse(status=400)

@csrf_exempt
def varsDetail(request, pk):
    if request.method == 'GET':
        try: var = Var.objects.get(id=pk)
        except Var.DoesNotExist: return HttpResponse(status=404)
        except: return HttpResponse(status=400)
        
        varDict= model_to_dict(var)
        return JsonResponse(varDict)
    
    elif request.method == 'PUT' or request.method == "POST":
        try: var = Var.objects.get(id=pk)
        except Var.DoesNotExist: return HttpResponse(status=404)
        except: return HttpResponse(status=400)

        data = request.body.decode('utf-8')
        data = json.loads(data)
        
        var.text= data.get('text') if data.get('text') != None else ''
        var.num= data.get('num') if data.get('num') != None else 0
        var.bit= data.get('bit') if data.get('bit') != None else False
        try: var.save()
        except: return HttpResponse(status= 400)

        varDict= model_to_dict(var)
        return JsonResponse(varDict)

    elif request.method == 'DELETE':
        try: var = Var.objects.get(id=pk)
        except Var.DoesNotExist: return HttpResponse(status=404)
        except: return HttpResponse(status=400)

        var.delete()
        return HttpResponse(status=204)
    
    else: return HttpResponse(status=400)
