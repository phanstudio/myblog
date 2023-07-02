from django import forms
from .models import Post, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser, User

class PostForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Post
        fields = ['title','author','body', 'categories', 'cover_image']

class SignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already taken')
        return email

class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name','slug')

class PostSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False)