from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404

def home(req):
    context = {}
    return render(req, 'home.html', context)
