from django import forms
from .models import Destination

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = [
            'place_name', 
            'weather', 
            'location_state', 
            'location_district', 
            'google_map_link', 
            'image', 
            'description'
        ]  # Make sure these fields match exactly with the model
