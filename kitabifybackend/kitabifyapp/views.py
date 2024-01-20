from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            remember_me = form.cleaned_data['remember_me']
            user = authenticate(request, **form.cleaned_data)
            if user is not None:
                login(request, user)
                if not remember_me:
                    # Egerki 'Məni yatda saxla' secilmiyibse vaxt goyursanki nece vaxtdan sora unutsun 
                    request.session.set_expiry(0)
                return redirect('home')  # esas seyfenin url yazirsan 'home'nin yerine
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

#1000IQ