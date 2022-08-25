from pkgutil import ImpImporter
from django.shortcuts import render,redirect,HttpResponse
from backend.models import Venue,Ticket
from django.http import JsonResponse
import json,ast
from django.contrib.auth.decorators import login_required
def TicketCheck(request):
    entrycode=request.GET['content']
    body=ast.literal_eval((json.loads(entrycode)))
    ticket=Ticket.objects.all().filter(Ticket_id=int(body["entry"])).first()
    if (ticket==None):
        return JsonResponse({"status ":404})
    if (ticket.CheckTicket()):
        return JsonResponse({"status":200,"entry":"ok"})
    return JsonResponse({"status":200,"entry":"error"})


def findVenue(request,pin_code):
    venues=Venue.objects.all().filter(pin_code=pin_code)
    return JsonResponse({"venues":venues})
