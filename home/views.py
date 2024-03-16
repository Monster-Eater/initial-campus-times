from django.shortcuts import render, redirect, get_object_or_404
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event, Profile, Meep, Complaint
from.forms import VenueForm, EventForm, MeepForm
from django.contrib import messages





#=================== Home =========================

def complaint(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        complain = Complaint(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        complain.save()
        messages.success(request, 'Your Complain Has Been Submitted and Sended To Chairman Successfully.Thanks....!')
        return redirect('complaint')
    return render(request, 'home/complaint.html')


def profile(request, pk):
    if request.user.is_authenticated:        
        profile = Profile.objects.get(user_id = pk)
        meeps = Meep.objects.filter(user_id = pk).order_by("-created_at")

        if request.method =='POST':
            current_user_profile = request.user.profile
            action = request.POST['follow']
            if action == "unfollow":
                current_user_profile.follows.remove(profile)
            elif action == "follow":
                current_user_profile.follows.add(profile)
            current_user_profile.save()    
        return render (request, "home/profile.html", {
            "profile": profile,
            'meeps': meeps
        })
    else:
        messages.success(request, 'Your must be logged in to view this page....!')
        return redirect('home')



def profile_list(request):
    profiles = Profile.objects.exclude(user = request.user)
    return render (request, 'home/profile_list.html', {
        "profiles": profiles,
    })

def home(request):
    if request.user.is_authenticated:
        form = MeepForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                meep = form.save(commit= False)
                meep.user = request.user
                meep.save()
                messages.success(request, 'Your Meep Has Been Posted....!')
                return redirect("home")            
        meeps = Meep.objects.all().order_by("-created_at")
        return render (request, 'home/home.html', {'meeps': meeps, 'form': form})
    else:
        meeps = Meep.objects.all().order_by("-created_at")
        return render (request, 'home/home.html', {'meeps': meeps })

def add_event(request):
    submitted = False
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True') 
    else:
      
        form = EventForm
        if "submitted" in request.GET:
            submitted= True
    return render (request, 'home/add_event.html', {
        "form": form,
        "submitted": submitted,
    })


def add_venue(request):
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True') 
    else:
      
        form = VenueForm
        if "submitted" in request.GET:
            submitted= True
    return render (request, 'home/add_venue.html', {
        "form": form,
        "submitted": submitted,
    })



def all_events(request):
   event_list = Event.objects.all()
   return render(request, 'home/event_list.html', {
       'event_list': event_list,
   })



def campus(request, year= datetime.now().year, month= datetime.now().strftime('%B')):
    name = 'Sallam'
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    cal = HTMLCalendar().formatmonth(
        year,
        month_number)
    now = datetime.now()
    current_year = now.year

    time = now.strftime('%I:%M %p ')
    return render (request, 'home/campus.html' , {
        'name': name,
        'year': year,
        'month': month,
        'month_number': month_number,
         'cal': cal, 
         'current_year': current_year,  
         'time':time,
})

def meep_like(request, pk):
    if request.user.is_authenticated:
        meep = get_object_or_404(Meep, id= pk)
        if meep.likes.filter(id= request.user.id):
           meep.likes.remove(request.user)
        else:
            meep.likes.add(request.user)
        
        return redirect(request.META.get("HTTP_REFERER"))    
    else:
        messages.success(request, ('Sorry! You must be logged in to like this meep....!'))
        return redirect('home')


#===================   Diciplenes   ========================

def rehb(request):
    return render (request, "diciplen/rehb.html", {})
def applied(request):
    return render (request, "diciplen/applied.html", {})
def comp(request):
    return render (request, "diciplen/comp.html", {})
def engin(request):
    return render (request, "diciplen/engin.html", {})
def islamic_study(request):
    return render (request, "diciplen/islamic_study.html", {})
def phsyco(request):
    return render (request, "diciplen/phsyco.html", {})
def chemis(request):
    return render (request, "diciplen/chemis.html", {})
def socio(request):
    return render (request, "diciplen/socio.html", {})



#======================  Departments  =====================

def biotech(request):
    return render (request, "departments/biotech.html", {})
def hnd(request):
    return render (request, "departments/hnd.html", {})
def mlt(request):
    return render (request, "departments/mlt.html", {})
def dpt(request):
    return render (request, "departments/dpt.html", {})
def slp(request):
    return render (request, "departments/slp.html", {})
def mit(request):
    return render (request, "departments/mit.html", {})
def food_science(request):
    return render (request, "departments/food_science.html", {})
def botany(request):
    return render (request, "departments/botany.html", {})
def softeng(request):
    return render (request, "departments/softeng.html", {})
def infotech(request):
    return render (request, "departments/infotech.html", {})
def datascience(request):
    return render (request, "departments/datascience.html", {})
def cybersec(request):
    return render (request, "departments/cybersec.html", {})
def computersci(request):
    return render (request, "departments/computersci.html", {})
def electricalengin(request):
    return render (request, "departments/electricalengin.html", {})
def bioinformatics(request):
    return render (request, "departments/bioinformatics.html", {})
def phsycodiploma(request):
    return render (request, "departments/phsycodiploma.html", {})
def appliedphsyco(request):
    return render (request, "departments/appliedphsyco.html", {})
def chemistry(request):
    return render (request, "departments/chemistry.html", {})
def biochem(request):
    return render (request, "departments/biochem.html", {})
def criminology(request):
    return render (request, "departments/criminology.html", {})
def masscomm(request):
    return render (request, "departments/masscomm.html", {})
def mediasci(request):
    return render (request, "departments/mediasci.html", {})
def sociology(request):
    return render (request, "departments/sociology.html", {})
