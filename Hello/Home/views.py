from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
     # return HttpResponse("This is Homepage.")
     return render(request,'index.html')

def about (request):
     # return HttpResponse("This is about page.")
     return render(request,'about.html')

def orders (request):
     return render(request,'orders.html')
     # return HttpResponse("This is orders page.")

def contacts (request):
     return render(request,'contact.html')
     # return HttpResponse("This is contacts page.")


def india (request):
     return HttpResponse("This is homepage for india ")
def usa (request):
     return HttpResponse("This is homepage for usa.")
def germany (request):
     return HttpResponse("This is homepage for germany. ")
def srilanka (request):
     return HttpResponse("This is homepage for sri lanka ")
def custom (request):
     return HttpResponse("This is homepage for custom loaction")