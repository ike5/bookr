from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World!")

def fun(request):
    return HttpResponse("What the fudge?")

def a(request):
    return HttpResponse("A is the first letter of the alphabet")

def b(request):
    return HttpResponse("B stands for baby")

def c(request):
    return HttpResponse("C stands for cat")

def d(request):
    return HttpResponse(

    )