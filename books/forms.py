from django import forms
from books.models import *

class AddBookForm(forms.ModelForm):
    # title = forms.CharField(max_length=255, label = "Book Title")
    # slug = forms.SlugField(max_length=255,label="Slug")
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows':10}),label="Content")
    # is_published = forms.BooleanField(label="Publication", required=False,initial=True)
    # cat = forms.ModelChoiceField(queryset=Category.objects.all(),label="Category",empty_label="No Chosen")

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['cat'].empty_label = "Not Chosen"

    class Meta:
        model = Books
        fields = ['title','slug','content','photo','is_published','cat']

        # widgets = {
        #     'title':forms.TextInput(attrs={'class':'form-input'}),
        #     'content':  forms.Textarea(attrs={'cols':60,'rows':10}),
        # }
     