from django.shortcuts import render

def page1(request):
    return render(request, 'events/page1.html')

def page2(request):
    return render(request, 'events/page2.html')

def page3(request):
    return render(request, 'events/page3.html')
