from django.views.decorators.csrf import csrf_exempt
from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Var, VarGroup
import json

# TODO:
# if no json is sent to api, it will raise server error; fix it!


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
        if data.get('group_id') != None: groupId= data.get('group_id') 
        else: return HttpResponse(status=400)
        try:
            var = Var(text=text, num=num, bit=bit, group= VarGroup.objects.get(id=groupId))
            var.save()
        except: return HttpResponse(status=400)
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
        if data.get('group_id') != None:
            try: var.group= VarGroup.objects.get(id= data.get('group_id'))
            except: return HttpResponse(status= 400)
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

@csrf_exempt
def groupsList(request):
    if request.method == 'GET':
        groups= VarGroup.objects.all()
        return JsonResponse(list(groups.values()), safe=False)

    elif request.method == 'POST':
        data = request.body.decode('utf-8')
        data = json.loads(data)

        title= data.get('title') if data.get('title') != None else ''
        try:
            varGroup= VarGroup(title= title)
            varGroup.save()
        except: return HttpResponse(status=400)
        groups= VarGroup.objects.all()
        return JsonResponse(list(groups.values()), safe=False)

    else: return HttpResponse(status=400)

@csrf_exempt
def groupsDetail(request, pk):
    if request.method == 'GET':
        try: varGroup= VarGroup.objects.get(id=pk)
        except VarGroup.DoesNotExist: return HttpResponse(status=404)
        except: return HttpResponse(status=400)

        groupDict= model_to_dict(varGroup)
        return JsonResponse(groupDict)

    elif request.method == 'PUT' or request.method == 'POST':
        try: varGroup= VarGroup.objects.get(id=pk)
        except VarGroup.DoesNotExist: return HttpResponse(status=404)
        except: return HttpResponse(status=400)

        data = request.body.decode('utf-8')
        data = json.loads(data)

        varGroup.title= data.get('title') if data.get('title') != None else ''
        try: varGroup.save()
        except: return HttpResponse(status= 400)
        
        groupDict= model_to_dict(varGroup)
        return JsonResponse(groupDict)

    elif request.method == 'DELETE':
        try: varGroup= VarGroup.objects.get(id=pk)
        except VarGroup.DoesNotExist: return HttpResponse(status=404)
        except: return HttpResponse(status=400)

        varGroup.delete()
        return HttpResponse(status=204)
    
    else: return HttpResponse(status=400)

