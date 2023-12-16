from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
# Create your views here.

from django.contrib.auth import authenticate, login

def login_pge(request):
    if request.method == "POST":
        username = request.POST.get('Usernames')  # Get the username from the form
        password = request.POST.get('Passwords')  # Get the password from the form
        user = authenticate(username=username, password=password)

        if user is not None:
            print("pass")
            login(request, user)
            return redirect('dashboard')  # Redirect to the "dashboard" URL pattern
        else:
            print("fail")
            return render(request, 'login_page.html', {'error_message': 'Invalid credentials'})
    return render(request, 'login_page.html')

class Dashboard():
    def dashboard(request):
        return render(request,'dashboard.html')
    def door_status(request):
        return render(request,'door.html')
    def cctv(request):
        return render(request,'cctv.html')
    def smart_tv(request):
        return render(request,'smart_tv.html')
    def user_info(request):
        return render(request,'user_info.html')