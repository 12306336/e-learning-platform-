from django.shortcuts import render, HttpResponse

def home(request):
    # return HttpResponse("this is home page")
    context = {
        'a':"this is sent"
    }
    return render(request,'home.html',context)

def about(request):
    # return HttpResponse('This is about page')    
    return render(request,'about.html')

def action(request):
    return HttpResponse("This is action")
