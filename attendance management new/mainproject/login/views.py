# from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
# #new
# from django.contrib.auth import login,logout
# # Create your views here.
# def login_page (request):
#   return render(request,'login.html')

# def newlogin (request):
#   if request.method == 'POST':
#     form = UserCreationForm(request.POST)
#     if form.is_valid():
#       user = form.save()
#       login(request,user)
#       return 'success'
#   else:
#     form = UserCreationForm()
#     return render(request,'newlogin.html',{'form':form})
#   return render(request,'newlogin.html')


# loginapp/views.py
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, authenticate

def newlogin(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Automatically log in after registration
            login(request, user)
            return redirect('login:login_page')
    else:
        form = RegistrationForm()
    return render(request, 'newlogin.html', {'form': form})



# loginapp/views.py (add to it)
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home or any page
            else:
                form.add_error(None, "Invalid credentials")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def school (reqest):
  return render (reqest,'school.html')

# loginapp/views.py
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('loginapp:login')

# loginapp/views.py
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'school.html')

