from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def login(request):
     csrfContext = RequestContext(request)
     return render_to_response('foo.html', csrfContext)

# Create your views here.
def index(request):
    return render(request, 'user.html')

@csrf_exempt
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
