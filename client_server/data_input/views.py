from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')
                  
                  
def add(request):
    if request.method == 'POST':
        data = request.POST['data']
        return HttpResponse("Data added successfully")
    else:
        return render(request, 'home.html')
