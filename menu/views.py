from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime, timedelta
from .forms import EmailForm
from .models import Entree
from .models import Pizza
from .models import Pates
from .models import Dessert
from .models import Boisson
from .models import Annonce
from .models import Horaire

def check_if_open():  
    annonce = Annonce.objects.exclude(actif=False).last()
    horaire = Horaire.objects.order_by('pk')
    dt = datetime.now()
    
    today = dt.today().date()
    day = dt.isoweekday()
    now = dt.time()
    isOpen = ""
    next = ""

    if annonce and (annonce.actif and (annonce.debut <= today <= annonce.fin)): # check si annonce active
        isOpen = "Fermé"
        next = " - Ouvre le " + (annonce.fin + timedelta(days=1)).strftime('%d-%m-%Y')
    else:
        for j, jour in enumerate(horaire): # parcours les jours de la semaine
            if day == jour.pk: # cherche jour actuel
                if jour.services.count() != 0: # check si il y a des services ce jour
                    for s, service in enumerate(jour.services.all()): # parcours des services du jour
                        if now > service.debut and now < service.fin: # check si service en cours actuellement
                            isOpen = "Ouvert"
                            next = " - Ferme à " + str(service.fin.strftime('%H:%M'))
                            return isOpen, next
                        else:
                            isOpen = "Fermé"
                else:
                            isOpen = "Fermé"
                if day == 7 and now > jour.services.all().last().fin: # recherche prochaine reouverture à partir de dimanche apres services
                    for k in horaire:
                        for ser in k.services.all():
                            if ser:
                                if k.pk == 1:
                                    next = " - Ouvre demain à " + str(ser.debut.strftime('%H:%M'))
                                    break
                                else:
                                    next = " - Ouvre " + str(k.jour).lower() + " à " + str(ser.debut.strftime('%H:%M'))
                                    break
                        if next != "":
                            break
                else: # recherche prochaine reouverture les autres jours
                    for l in horaire[j:]:
                        for se in l.services.all():
                            if (se and now < se.debut) or (l.pk > day and se):
                                if l.pk > day:
                                    if l.pk == day + 1:
                                        next = " - Ouvre demain à " + str(se.debut.strftime('%H:%M'))
                                    else:
                                        next = " - Ouvre " + str(l.jour).lower() + " à " + str(se.debut.strftime('%H:%M'))
                                else:
                                    next = " - Ouvre à " + str(se.debut.strftime('%H:%M'))
                                break
                        if next != "":
                            break
                break 
        
    return isOpen, next

# Create your views here.
def home(request):
    annonce = Annonce.objects.exclude(actif=False).last()
    horaire = Horaire.objects.order_by('pk')
    isOpen, next = check_if_open()

    return render(request, 'menu/home.html', {
        'annonce': annonce,
        'horaire': horaire,
        'isOpen': isOpen,
        'next': next
     })

def infos(request):
    annonce = Annonce.objects.exclude(actif=False).last()
    horaire = Horaire.objects.order_by('pk')
    isOpen, next = check_if_open()

    return render(request, 'menu/infos.html', {
        'annonce': annonce,
        'horaire': horaire,
        'isOpen': isOpen,
        'next': next
    })

    
def get_menu(request):
    annonce = Annonce.objects.exclude(actif=False).last()
    horaire = Horaire.objects.order_by('pk')
    isOpen, next = check_if_open()

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
        'boissons': boissons,
        'annonce': annonce,
        'horaire': horaire,
        'isOpen': isOpen,
        'next': next
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
    