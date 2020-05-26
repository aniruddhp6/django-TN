from django import forms
from .models import RegListing   

class RegListingForm(forms.ModelForm): 
    
    class Meta: 
        model = RegListing  
        fields = [ 
            "title", 
            "message", 
        ] 
     

class UpdateForm(forms.ModelForm): 
      class Meta: 
        model = RegListing  
        fields = [ 
            "title", 
            "message", 
        ] 

    