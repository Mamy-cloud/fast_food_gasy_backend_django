from django import forms
from .models import Tacos

class TacosUploadForm(forms.ModelForm):
    class Meta:
        model = Tacos
        fields = ['name', 'image_url', 'price']  # si tu utilises URLField
        # si tu veux upload fichier direct, tu peux mettre un FileField temporaire

        #pour indiquer d'entrer le nom et l'url d'image du tacos
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder': "Entrer le nom tacos"}),
            'image_url': forms.TextInput(attrs={'placeholder': "Entrer l'image tacos"}),
        }
