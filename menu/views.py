from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
import time
from .forms import EmailForm
from .models import Entree
from .models import Pizza
from .models import Pates
from .models import Dessert
from .models import Boisson

# Create your views here.
def home(request):
    return render(request, 'menu/home.html', {

     })

def infos(request):
    return render(request, 'menu/infos.html', {
        
    })

    
def get_menu(request):
    entrees = Entree.objects.order_by('prix', 'nom').exclude(prix=0)
    pizzas = Pizza.objects.order_by('-suggestion', 'prix', 'nom').exclude(prix=0)
    pates = Pates.objects.order_by('prix', 'nom').exclude(prix=0)
    desserts = Dessert.objects.order_by('prix', 'nom').exclude(prix=0)
    boissons = Boisson.objects.order_by('prix', 'nom').exclude(prix=0)
    try:
        return render(request, 'menu/menu.html', {
        'entrees': entrees,
        'pizzas': pizzas,
        'pates': pates,
        'desserts': desserts,
        'boissons': boissons
        })
    except:
        return render(request, 'menu/menu_offline.html', {})

def mail_sender(request):
    # create a variable to keep track of the form
    messageSent = False

    # check if form has been submitted
    if request.method == 'POST':

        form = EmailForm(request.POST)

        # check if data from the form is clean
        if form.is_valid():
            cd = form.cleaned_data
            subject = cd['subject']
            sender = cd['sender']
            message = f"Mail envoyé par: {cd['sender']}\n\n{cd['message']}"

            # send the email to the recipent
            send_mail(subject,
                      message,
                      settings.EMAIL_HOST_USER,
                      [settings.EMAIL_HOST_USER])

            # set the variable initially created to True
            messageSent = True
    else:
        form = EmailForm()

    return render(request, 'menu/contact.html', {
        'form': form,
        'messageSent': messageSent,
    })
    