#From core.models import File
from django.utils.translation import gettext_lazy as _

# from core.models import File

# class FileForm(forms.ModelForm):
#     class Meta:
#         model= File
#         fields= ["name", "filepath"]

from django import forms
from core.models import Document, Technology

class TechnologyForm(forms.ModelForm):
    class Meta:
        model = Technology
        fields = ('technology_operating_band', 'technology_cell_id',)



class DocumentForm(forms.ModelForm):
    POSITION_OPTIONS = (  
    ('alpha_pos_1', 'alpha_pos_1'),
    ('alpha_pos_2', 'alpha_pos_2'),)
    #position = forms.ChoiceField(choices=POSITION_OPTIONS)
    #position = forms.ChoiceField(choices=POSITION_OPTIONS, required=True )
    document = forms.FileField(required = False, widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'narrow-select'}))
 
    connected_rrh_serial = forms.CharField(required=False) #This comes from user entry

    #document = forms.FileField()
    class Meta:
        
        #position = forms.ChoiceField(choices=POSITION_OPTIONS, required=True )
        
        model = Document
        #exclude = ['connected_rrh_serial']
        fields = ( 'document', )
        labels = {
            'connected_rrh_serial': _('rrh'),
        }
        # widgets = {
        #     'connected_rrh_serial': TextInput(attrs = {
        #         'placeholder': 'Username',
        #         'class': 'form-control',
        #         'aria-describedby': 'sizing-addon1',

        #     })

# class DocumentForm(forms.ModelForm):
#     file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
#     class Meta:
#         model = Document
#         fields = ['file']

# class DocumentForm(forms.Form):
#     file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))