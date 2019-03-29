from django.shortcuts import render
from django.http import HttpResponse
from . import models
import json

def index(request):
    data = {}
    data["modules"] = list(models.module_info.objects.values())
    # data["modules"] = list(models.module_info.objects.all())
    # data["modules"] = list(models.module_info.objects.values('title', 'code', 'smester_taught'))
    # modules = models.module_info.objects.all()
    # data = {"modules": []}
    # l = len(modules)
    # for i in range(l):
    #     data["modules"].append({"name": modules[i].title, "code": modules[i].code, "session": modules[i].smester_taught})
    # # js_data = json.dumps(data)
    return render(request, 'index.html', {'data': data})






