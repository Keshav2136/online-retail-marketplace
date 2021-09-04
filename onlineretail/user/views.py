from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
     csrfContext = RequestContext(request)
     return render('foo.html', csrfContext)

# Create your views here.
def index(request):
    return render(request, 'user.html')

def login_success(request):
    username=request.POST.get("username")
    email=request.POST.get("email")
    provider=request.POST.get("provider")
    token=request.POST.get("token")
    print("Hello, "+username)
    print(email)
    print(provider)
    print(token)
    return HttpResponse("OK");
