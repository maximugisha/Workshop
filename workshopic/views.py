from functools import reduce
from django.db import models
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.conf.urls import include, url
from django.contrib import admin
from django.template.context import RequestContext
from django.views import generic
from django.shortcuts import render_to_response
from django.utils.safestring import mark_safe

from workshopic.templatetags.event_tags import WorkoutCalendar
from .models import Workshop, Participant, Facilitator
from django.utils import timezone
from .forms import RegForm
import re

# Create your views here.

def search(request):
    query = request.GET.get('search')
    workshops = Workshop.objects.get_or_create(name__icontains=query)
    return render_to_response('workshopic/search.html', {'workshops': workshops})

def home(request):
    paricipants = Participant.objects.filter(reg_date__lte=timezone.now()).order_by('reg_date')
    return render(request, 'workshopic/home.html', {'participants': paricipants},)

def attendants(request):
    participants = Participant.objects.filter(reg_date__lte=timezone.now()).order_by('reg_date')
    return render(request, 'workshopic/attendants.html', {'participants' : participants})

def reg_page(request):
    return render(request, 'workshopic/reg_page.html', {})

def participant_detail(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    return render(request, 'workshopic/participant_detail.html', {'participant': participant})

def new_participant(request):
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            participant = form.save(commit=True)
            participant.save()
            return redirect('participant_detail', pk=participant.pk)
    else:
        form = RegForm()
    return render(request, 'workshopic/reg_page.html', {'form' : form})

