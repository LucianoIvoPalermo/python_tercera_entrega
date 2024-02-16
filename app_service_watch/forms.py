from django import forms
 
class ClientsForm(forms.Form):
    name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=40)
    company = forms.CharField(max_length=30)

class StaffForm(forms.Form):
    name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=40)

class ServicesProvidedForm(forms.Form):
    name = forms.CharField(max_length=60)
    completion_date = forms.DateField()
    completed = forms.BooleanField()

class PendingServicesForm(forms.Form):
    name = forms.CharField(max_length=60)
    status_update_date = forms.DateField()
    status = forms.CharField(max_length=20)

class Search(forms.Form):
    name = forms.CharField(max_length=60)