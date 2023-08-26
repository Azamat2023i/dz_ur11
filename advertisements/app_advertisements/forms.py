# from django import forms
# class AdvertisementForm(forms.Form):
    
#     title = forms.CharField(max_length =64,
#                             widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    
#     description = forms.CharField(
#                             widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    
#     price = forms.DecimalField(
#         widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}))
    
#     # auction = forms.BooleanField(required=False,
#     #                         widget=forms.CheckboxInput(attrs={'class': 'form-chek-input'}))

#     auction = forms.BooleanField(required=False, 
#                             widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'type': 'checkbox'}))

#     image = forms.ImageField()
#                             # widget=forms.FileInput(attrs={'class': 'form-control form-control-lg'}))
                            

from django import forms 
from .models import Advertisement 
 
# class AdvertisementForm(forms.ModelForm): 
#     class Meta: 
#         model = Advertisement 
#         fields = ['title', 'description', 'price', 'auction', 'image'] 
#         widgets = { 
#             'title': forms.TextInput(attrs={'class': 'form-control form-control-lg'}), 
#             'description': forms.TextInput(attrs={'class': 'form-control form-control-lg'}), 
#             'price': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}), 
#             'auction': forms.CheckboxInput(attrs={'class': 'form-check-input', 'type': 'checkbox'}), 
#             'image': forms.FileInput() 
#         } 
        
 

class AdvertisementForm(forms.ModelForm):
     
    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'auction', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'price': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'auction': forms.CheckboxInput(attrs={'class': 'form-check-input', 'type': 'checkbox'}),
            'image': forms.FileInput()
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.startswith('?'):
            raise forms.ValidationError(f"Заголовок не может начинаться с '{title[0]}'")
        return title