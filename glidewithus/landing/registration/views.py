from django.shortcuts import render
from models import requested_invites

# Create your views here.

def Request_Invite(request, email_Address, mission_statement):
	if request.POST:
		b = requested_invites(email=email_Address, mission_statement=mission_statement)

