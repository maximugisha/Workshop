from django.shortcuts import render, get_object_or_404, redirect
from django.conf.urls import include, url
from django.contrib import admin
from .models import Workshop, Participant, Facilitator
from django.utils import timezone
from .forms import RegForm

# Create your views here.

def home(request):
    participants = Participant.objects.filter(reg_date__lte=timezone.now()).order_by('reg_date')
    return render(request, 'workshopic/home.html', {'participants' : participants})


def attendants(request):
    participants = Participant.objects.filter(reg_date__lte=timezone.now()).order_by('reg_date')
    females = Participant.objects.filter(gender='FEMALE').count()
    males = Participant.objects.filter(gender='MALE').count()
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
