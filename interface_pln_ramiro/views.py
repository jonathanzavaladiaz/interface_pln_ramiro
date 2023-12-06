from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse("<h1>Interface PLN, Jonathan Zavala-Díaz</h1>")
