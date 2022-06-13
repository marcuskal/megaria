from django import forms
from .models import Post, Comment, MessageModel


class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'rows': '3',
                'placeholder': 'Say something...'
            }
        )
    )

    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'multiple': True
        })
    )

    class Meta:
        model = Post
        fields = ['body']

class DonationForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'rows': '3',
                'placeholder': 'Describe your donation'
            }
        )
    )

    address = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'rows': '1',
                'placeholder': 'Your address'
            }
        )
    )

    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'multiple': True
        })
    )

    

    class Meta:
        model = Post
        fields = ['body', 'address', 'image']



class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'rows': '3',
                'placeholder': 'Say something...'
            }
        )
    )

    class Meta:
        model = Comment
        fields = ["comment"]


class ThreadForm(forms.Form):
    username = forms.CharField(label='', max_length=100)


class MessageForm(forms.ModelForm):
    body = forms.CharField(label='', max_length=1000)

    image = forms.ImageField(required=False)

    class Meta:
        model = MessageModel
        fields = ['body', 'image']


class ShareForm(forms.Form):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say Something...'
        }))


class ExploreForm(forms.Form):
    query = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Explore tags'
        })
    )
