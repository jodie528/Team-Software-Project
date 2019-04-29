from django.shortcuts import render
from django.http import HttpResponse
from . import models
import json

def index(request):
    #data["modules"] = list(models.module_info.objects.values())
    # data["modules"] = list(models.module_info.objects.values('title', 'code', 'smester_taught'))

    # create a dic used for info display
    data = {"modules": [], "programs":[]}

    # get all basic information of modules
    modules = models.module_info.objects.all()

    # get all basic information of programmes
    programs = models.Program_cont.objects.all()

    # info of module
    l = len(modules)
    for i in range(l):
        data["modules"].append({"name": modules[i].title, "code": modules[i].code, "session": modules[i].smester_taught})

    # info of program
    # l_pro = len(programs)
    # for i in range(l_pro):
    #     data["programs"].append()

    return render(request, 'index.html', {'data': data})

def program_input(request):
    return render(request, 'program_input.html')

def module_input(request):
    return render(request, 'module_input.html')





