from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import CandidateRegistrationForm, CandidateLoginForm, EventForm
from .models import Event

def candidate_register(request):
    if request.method == 'POST':
        form = CandidateRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('candidate_login')
    else:
        form = CandidateRegistrationForm()
    return render(request, 'candidate_register.html', {'form': form})

def candidate_login(request):
    if request.method == 'POST':
        form = CandidateLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('event_list')
    else:
        form = CandidateLoginForm()
    return render(request, 'candidate_login.html', {'form': form})

def candidate_logout(request):
    logout(request)
    return redirect('candidate_login')

@login_required(login_url='/candidate/login/')
def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

@login_required(login_url='/candidate/login/')
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'event_detail.html', {'event': event})

@staff_member_required
def admin_dashboard(request):
    events = Event.objects.all()
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = EventForm()
    return render(request, 'admin_dashboard.html', {'events': events, 'form': form})
