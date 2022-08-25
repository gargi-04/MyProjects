from datetime import datetime, date,time
from email.policy import default
from random import choices
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Venue(models.Model):
    Name=models.CharField(max_length=50)
    image=models.ImageField(blank=True)
    desc=models.CharField(max_length=500,default="")
    venue_id_code=models.IntegerField(default=0,primary_key=True)
    pin_code=models.IntegerField(default=0)
    location=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    open_timing=models.TimeField(blank=True, null=True ,default=datetime.now().strftime("%H:%M:%S"))
    close_timing=models.TimeField(blank=True, null=True ,default=datetime.now().strftime("%H:%M:%S"))
    entry_fee=models.IntegerField(default=0)
    def __str__(self):
        return self.Name

id_type=(("Aadhar Card","Aadhar Card"),("Voter Card","Voter Card"),("Pan Card","Pan Card"))
payment_mode=(("Cash","Cash"),("Online","Online"))
class Ticket(models.Model):
    user_name=models.CharField(max_length=50)
    ID_type=models.CharField(max_length=20,choices=id_type,default="Aadhar Card")
    ID_number=models.CharField(max_length=50)
    venue_id_code=models.ForeignKey(Venue,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Num_ticket=models.IntegerField(default=0)
    phone_number=models.IntegerField(default=0)
    email=models.CharField(max_length=50)
    payment=models.CharField(max_length=20,choices=payment_mode,default="Online")
    Trans_ID=models.CharField(max_length=50)
    Total_amt=models.IntegerField(default=0)
    entry_code=models.IntegerField(default=0)
    QR_code=models.ImageField(blank=True)
    Ticket_validation=models.BooleanField(default=True)
    booking_time=models.DateTimeField(default=datetime.now())
    Visiting_Date=models.DateTimeField(blank=True)
    Ticket_id=models.IntegerField(unique=True,primary_key=True)
    qr_svg=models.CharField(max_length=100000,blank=True,null=True)
    def __str__(self):
        return self.email
    def sendMessage(self,num_ticket=0):
        if num_ticket==0:
            return "You don't have any more tickets left"
        else:
            return "You have "+str(num_ticket)+"number of tickets left"

    def ticketLeft(self):
        if (self.Num_ticket>0):
            self.Num_ticket-=1
            self.save()
            self.sendMessage(self.Num_ticket)
        else :
            self.Ticket_validation=False
            self.sendMessage()
        return self.Num_ticket      
    def CheckTicket(self):
        scanDate=datetime.now()
        if scanDate.day==self.Visiting_Date.day:
            venue=self.venue_id_code
            n=self.Num_ticket
            if (n==0): return 0
            if (venue.open_timing.hour <=scanDate.hour and scanDate.hour<=venue.close_timing.hour):
                if (self.Ticket_validation):
                    self.ticketLeft()

                    return 1
        return 0
