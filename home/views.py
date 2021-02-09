from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


def index(request):
    return render(request, 'home/index.html')


def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_mail = request.POST['message-mail']
        message = request.POST['message']

        # send a mail
        send_mail(
            message_name,  # subject
            message,  # message
            message_mail,  # from email
            ['jihane.azim@gmail.com']  # to email
        )

        return render(request,
                      'home/contact.html',
                      {'message_name': message_name})
    else:
        return render(request, 'home/contact.html', {})


def github(request):
    return render(request, 'home/github.html')
