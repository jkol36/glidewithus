from django import forms
from glidewithus.profiles.models import GlideProfile
from models import message

class new_message(forms.ModelForm):
	text = forms.CharField(label="", widget=forms.Textarea(attrs={"id":'message_text', 'class':'form-control', 'rows':5, 'placeholder':'Your message here' }))

	class Meta:
		model = message
		fields = ['text']