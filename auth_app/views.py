from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def usignup(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        pw1 = request.POST.get('pw1')
        pw2 = request.POST.get('pw2')
        if pw1 == pw2:
            try:
                usr = User.objects.get(username = uname)
                return render(request, 'usignum.html', {'response': "Username not available"})
            except User.DoesNotExist:
                usr = User.objects.create_user(username = uname, password = pw1)
                usr.save
                return redirect('ulogin')
        else:
            return render(request, 'usignum.html', {'response': "Password does not match"})
    else:
        return render(request, 'usignup.html')

def ulogin(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        usr = authenticate(username = uname, password = pwd)
        if usr is None:
            return render(request, 'ulogin.html', {'response': "Invalid Credentials"})
        else:
            login(request, usr)
            return redirect('home')
    else:
        return render(request, 'ulogin.html')

def ulogout(request):
    logout(request)
    request.session.flush()
    request.session.clear_expired()
    return redirect('ulogin')
