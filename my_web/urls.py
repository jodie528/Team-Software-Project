# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Weishi Li
# time: 2019-03-12

from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index),
    path('module_input/', views.module_input, name = 'module_input'),
    path('program_input/', views.program_input, name = 'program_input'),

]
