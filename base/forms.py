from django import forms
from django.forms import ModelForm
from .models import *

class AddPostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'author',
            'category',
            'image',
            'body'
        ]
        
        widgets = {
            'category': forms.CheckboxSelectMultiple(),
            'author':forms.TextInput(attrs={'value':'','type':'hidden'})
        }
        
class AddCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        
        
        
class AddVideoPostForm(ModelForm):
    class Meta:
        model = VideoPost
        fields = [
            'caption',
            'video',
            'thumbnail',
            'author',
            'category',
            'body'
        ]
        
        widgets = {
            'category': forms.CheckboxSelectMultiple(),
            'author':forms.TextInput(attrs={'value':'','type':'hidden'})
        }
        
class PostCommentForm(ModelForm):
    class Meta:
        model = PostComment
        fields = [
            'post',
            'name',
            'comment'
        ]
        
        widgets = {
            'post': forms.TextInput(attrs={'value':'','type':'hidden'})
        }
        

class VideoPostCommentForm(ModelForm):
    class Meta:
        model = VideoPostComment
        fields = [
            'video',
            'name',
            'comment'
        ]
        
        widgets = {
            'video': forms.TextInput(attrs={'value':'','type':'hidden'})
        }

class AddAudioForm(ModelForm):
    class Meta:
        model = AudioPost
        fields = [
            'audio',
            'caption',
            'thumbnail',
            'author',
            'category',
            'body'
        ]
        
        widgets = {
            'category': forms.CheckboxSelectMultiple(),
            'author':forms.TextInput(attrs={'value':'','type':'hidden'})
        }
        
class AudioPostCommentForm(ModelForm):
    class Meta:
        model = AudioPostComment
        fields = [
            'audio',
            'name',
            'comment'
        ]
        
        widgets = {
            'audio': forms.TextInput(attrs={'value':'','type':'hidden'})
        }
        
        
