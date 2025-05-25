from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from Base.models import models
from Base.models import Contact
# Create your views here.
 

#def home (request):return render (request, 'home.html' )
def contact(request):
    if request.method == "POST":
        print('post')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        content = request.POST.get('content', '')
        number = request.POST.get('number', '')
        print(name, email, content, number)

        if 1 < len(name) < 30:
            pass
        else:
            messages.error(request, 'Please fill the form correctly')
            return render(request, 'home.html')

        if 1 < len(email) < 30:
            pass
        else:
            messages.error(request, 'Please fill the form correctly')
            return render(request, 'home.html')

        if 1 < len(number) < 13:
            pass
        else:
            messages.error(request, 'Please fill the form correctly')
            return render(request, 'home.html')

        ins = Contact(name=name, email=email, content=content, number=number)
        ins.save()
        messages.success(request, 'Your message has been sent successfully')
        print('data has been saved successfully in database')

    return render(request, 'home.html')