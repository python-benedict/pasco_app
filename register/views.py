from django.shortcuts import redirect, render
from.models import Register
from .forms import RegistrationForms
from django.contrib.auth import login, authenticate
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForms(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            if Register.objects.filter(username=username).exists():
                messages.info(request, 'Invalid Credential')
                form = RegistrationForms()
            else:
                form.save()
                account = authenticate(username=username, email=email, password=password)
                login(request, account)
                return redirect('main-view/')
        else:
            form['registration_form'] = form
    else:
        form = RegistrationForms()
    context = {
        'form':form
    }
    return render(request, 'register.html', context)