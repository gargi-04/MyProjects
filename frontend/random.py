from backend.models import Ticket
import random

def rand_Id():
    rand_ticket_id=random.randint(10000000,99999999)
    ticket=Ticket.objects.all().filter(Ticket_id=rand_ticket_id).first()
    if(ticket==None):
        return rand_ticket_id
    rand_Id()