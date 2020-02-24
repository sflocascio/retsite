#From core.models import File

# from core.models import File

# class FileForm(forms.ModelForm):
#     class Meta:
#         model= File
#         fields= ["name", "filepath"]

from django import forms
from core.models import Document



class DocumentForm(forms.ModelForm):
    POSITION_OPTIONS = (  
    ('alpha_pos_1', 'alpha_pos_1'),
    ('alpha_pos_2', 'alpha_pos_2'),)
    position = forms.ChoiceField(choices=POSITION_OPTIONS)
    #position = forms.ChoiceField(choices=POSITION_OPTIONS, required=True )
    document = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    #document = forms.FileField()
    class Meta:
        
        #position = forms.ChoiceField(choices=POSITION_OPTIONS, required=True )
        
        model = Document
        fields = ( 'document','position',  )

# class DocumentForm(forms.ModelForm):
#     file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
#     class Meta:
#         model = Document
#         fields = ['file']

# class DocumentForm(forms.Form):
#     file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))