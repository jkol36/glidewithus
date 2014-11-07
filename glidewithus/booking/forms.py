from glidewithus.profiles.models import GlideProfile
from models import meetuprequest
from django import forms

class sendmeetrequestForm(forms.ModelForm):
	message = forms.CharField(label="Include a message along with your request", widget=forms.Textarea(attrs={"id":'message', 'placeholder':'your message', 'class':'form-control', 'rows':5}))

	class Meta:
		model = meetuprequest
		fields = ['message']
		exclude = ['seen', 'date', 'target_sender', 'target_recipient', 'start_time', 'response']


