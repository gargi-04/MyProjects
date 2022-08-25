from wsgiref.util import request_uri
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate ,logout
from django.shortcuts import render,redirect,HttpResponse
from backend.models import Venue,Ticket
from .random import rand_Id
from .qr import qr_generation
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail,EmailMessage

#get full name 
def findVenue(venueID):
    return Venue.objects.all().filter(venue_id_code=venueID).first()
def getFullName(First_name,Last_name):
    return First_name +" "+ Last_name
# Create your views here.
def home(request):
    venue=Venue.objects.all()
    return render (request,"index.html",{"venues":venue})
def bookvenue(request,venueid):
    if (request.user.is_anonymous):
         return redirect("/")
    venue=Venue.objects.all().filter(venue_id_code=venueid).first()
    if (request.method=="POST"):
        first_name=request.POST['First_name']
        last_name=request.POST["Last_name"]
        email=request.POST["Email"]
        phone_number =request.POST['phone_number']
        venueID=request.POST['Venue_id_code']
        number_of_tickets=request.POST['Number_of_ticket']
        id_type=request.POST['ID_type']
        id_number=request.POST["ID_Number"]
        visiting_date=request.POST['Visiting_Date']
        ticket=Ticket( user=request.user,user_name=getFullName(first_name,last_name),ID_type=id_type,venue_id_code=findVenue(venueID),Num_ticket=number_of_tickets,phone_number=phone_number,email=email,Visiting_Date=visiting_date,Ticket_id=rand_Id(),ID_number=id_number)
        ticket.save()
        context= qr_generation({"venueID":venueID,'entry':ticket.Ticket_id,'number_of_tickets':number_of_tickets},ticket)
        #send_mail("booked",ticket.qr_svg,"teamhustlers522@gmail.com",[email])
        html_msg="entry cod e:" + str(ticket.Ticket_id)
        msg=EmailMessage("booked",html_msg,"teamhustlers522@gmail.com",[email])
        msg.content_subtype="html"
        msg.attach_file(str(ticket.Ticket_id)+".png")
        msg.send()
        return render (request, "mytickets.html" ,{"ticket":ticket})
   
    if(venue==None):
        print (venue)
        return redirect('/')
    return render(request,"BookPage.html",{"venue":venue})
def contact(request):
    return HttpResponse('contact')
def about(request):
    return HttpResponse('about')
def login(request):
    return render(request,'login.html')
def loginuser(request):
    if(request.method=='POST'):
        user_name=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(username=user_name,password=password)
        print(user)
        if user is not None:
            auth_login(request,user)
    return redirect('/')
def register(request):
    if(request.method=='POST'):
        user_name=request.POST["username"]
        password=request.POST["password"]
        confirm_password=request.POST["confirm_password"]
        email=request.POST["email"]
        if password==confirm_password:
            newuser=User.objects.create_user(user_name,email,password)
            newuser.save()
            user=authenticate(username=user_name,password=password)
            auth_login(request,user)
            return HttpResponse('Hi user Welcome to Scantist'+user.username)
    return HttpResponse('Hi user Welcome to Scantist undefined')
def mytickets(request):
    if (request.user.is_authenticated):
        userTickets=Ticket.objects.all().filter(user=request.user)
        print (userTickets)
    return render (request,'mytickets.html',{"context":userTickets})
def download(request,venuecode,idcode):
    allTicket= Ticket.objects.all().filter(venue_id_code=venuecode ,Ticket_id=idcode).first()
    return render (request,'index.html',{"context":allTicket})
def scanner(request):
    return render(request,'scanner.html')
def logoutuser(request):
    logout(request)
    return redirect ("/")
