import json
from models import GlideProfile, Interest, Company, Proffession
from dajaxice.decorators import dajaxice_register

@dajaxice_register(method="GET")
def removeinterest(request):
	print request.GET
	return json.dumps({'message':'helloworld'})