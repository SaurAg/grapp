from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def Csignup_view(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('grievances:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup_page.html', {'form':form})

def Clogin_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 's@next' in request.POST:
                return redirect(request.POST.get('s@next'))
            else:
                return redirect('grievances:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login_page.html', {'form':form})

def Clogout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('grievances:list')