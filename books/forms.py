from logging import PlaceHolder
from django import forms
from books.models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm , PasswordChangeForm
from captcha.fields import CaptchaField



class AddBookForm(forms.ModelForm):
    # title = forms.CharField(max_length=255, label = "Book Title")
    # slug = forms.SlugField(max_length=255,label="Slug")
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows':10}),label="Content")
    # is_published = forms.BooleanField(label="Publication", required=False,initial=True)
    # cat = forms.ModelChoiceField(queryset=Category.objects.all(),label="Category",empty_label="No Chosen")

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['genr'].empty_label = "Not Chosen"

    class Meta:
        model = Books
        fields = ['title','slug','content','photo','is_published','genr','author']

        # widgets = {
        #     'title':forms.TextInput(attrs={'class':'form-input'}),
        #     'content':  forms.Textarea(attrs={'cols':60,'rows':10}),
        # }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Lenght is too much')

        return title     


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'input-text','placeholder':"Type your First Name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'input-text','placeholder':"Type your Last Name"}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'input-text','placeholder':"Type your Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'input-text','placeholder':"Type your e-mail"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-text','placeholder':"Type your password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-text','placeholder':"Confirm your password"}))

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'input-text','placeholder':"Type your Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-text','placeholder':"Type your Password"}))


class UpdateProfileUser(forms.ModelForm):
    class Meta:
        model = User
        fields= ['username']

class UpdateProfilePassword(forms.ModelForm):
    class Meta:
        model = User
        fields= ['password']

class UpdateProfilePicture(forms.ModelForm):
    # profile_image = models.ImageField(./)
    class Meta:
        model = Profile
        fields = ('profile_image',)

        widgets = {
            'profile_image':forms.FileInput(attrs={'onchange':"this.form.submit()","class":"fileinput"})
        }


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-text','placeholder':"Old Password"}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-text','placeholder':"New Password"}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-text','placeholder':"Confirm New Password"}))

    class Meta:
        model = Profile
        fields = ('old_password','new_password1','new_password2')


class ContactForm(forms.Form):
    name = forms.CharField(label="Name")
    email = forms.EmailField(label = "Email")
    subject = forms.CharField(label = "Subject")
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':10}))
    captcha = CaptchaField()
