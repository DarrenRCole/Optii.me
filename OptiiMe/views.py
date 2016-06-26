from django.shortcuts import render
from scheduler.models import *
from django.http import HttpResponse
from itertools import *
from copy import copy
import math
import time

def render_home(request):
    return render(request, 'index.html')