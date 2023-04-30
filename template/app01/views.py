from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from app01.models import Message


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def sendMessage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        Message.objects.create(name=name,email=email,phone=phone,message=message)
    return HttpResponse('success')
