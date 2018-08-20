from django.shortcuts import render, redirect
from .models import Complain
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

def complains_list(request):
    complains = Complain.objects.all().order_by('date')
    return render(request, 'grievances/complain_list.html', {'complains':complains})

def respond(request):
    complains = Complain.objects.all().order_by('date')
    return render(request, 'grievances/respond.html', {'complains':complains})

@login_required(login_url="/resp/login/")
def display(request, id):
    complain = Complain.objects.get(id=id)
    form = forms.RespondForm(instance=complain)
    return render(request, 'grievances/update.html', {'form' : form, 'complain' : complain})

@login_required(login_url="/resp/login/")
def update(request):
    if request.method == 'POST':
        form = forms.RespondForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grievances:respond')
        else:
            print('Error Committed!') 

@login_required(login_url="/accounts/login/")
def complain_new(request):
    if request.method == 'POST':
        form = forms.ComplainForm(request.POST, request.FILES)
        if form.is_valid():
            s_instance = form.save(commit=False)
            s_instance.complainant = request.user
            s_instance.status = "Registered"
            s_instance.save()
            return redirect('grievances:list')
    else:
        form = forms.ComplainForm
    return render(request, 'grievances/complain_register.html', {'form':form})