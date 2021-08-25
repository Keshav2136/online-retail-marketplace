from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable1":"Harry is great",
        "variable2":"Rohan is great"
    } 
    return render(request, 'home.html', context)
    # return HttpResponse("this is homepage")
