from django.shortcuts import render

# Create your views here.
from my_app.models import Contact


def index(request):
    if request.method == 'POST':
        data = request.POST
        name = data['name']
        phone = data['phone']
        a = Contact(name=name, phone=phone)
        a.save()
    return render(request, 'index.html')

