import json
from models import GlideProfile, Interests, Compnay, Proffession
from dajaxice.decorators import dajaxice_register

@dajaxice_register
def get_user_id(request, user_id):
	if user_id:
		try:
			glideprofile = GlideProfile.objects.get(pk=user_id)
			interests = glideprofile.profile.interest_set()
			companies = glideprofile.objects.company_set()
			professions = glideprofile.objects.proffession_set()
			if interests:
				return json.dumps({'interests':interests})
			else:
				return json.dumps({'interests':'User does not currently have any interests'})
			if companies:
				return json.dumps({'companies':companies})
			else:
				return json.dumps({'error_message':'This user does not currently have any interests'})
			if professions:
				return json.dumps('professions':proffessions)
			else:
				return json.dumps('error_message':'this user does not currently have any proffessions')

		except Exception, e:
			return json.dumps({'error_message':'something went wrong'})
	else:
		return json.dumps({'error_message':'something went wrong.'})