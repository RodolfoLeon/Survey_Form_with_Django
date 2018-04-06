# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string

from models import *

# Create your views here.

def index(request):
    if 'submissioncounter' in request.session:
        request.session['submissioncounter'] += 1
    else:
        request.session['submissioncounter'] = 1
    return render(request, "index.html")

def formprocess(request):
    if request.method == "POST":
        context={
            'Name': request.POST['fname'],
            'Dojo Location': request.POST['location'],
            'Favorite Language': request.POST['language'],
            'Comment': request.POST['comment']
        }
    return redirect('/results', context=context)

def results(request, context):
    return render(request, "results.html", context=context)