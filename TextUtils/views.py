from django.http import HttpResponse

def index(request):
    return HttpResponse("TESTING")

def about(request):
    return HttpResponse("TESTING 2")