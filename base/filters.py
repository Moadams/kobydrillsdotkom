import django_filters
from .models import *
from django import forms
from django_filters import CharFilter

class PostFilter(django_filters.FilterSet):
    title = CharFilter(field_name = 'title', lookup_expr='icontains', label = 'Title')    
    # category/ = django_filters.ModelMultipleChoiceFilter(queryset = Category.objects.all(), widget = forms.CheckboxSelectMultiple)
    
    class Meta:
        model =  Post
        fields = [
            'title',
            
        ]
        
        
class VideoFilter(django_filters.FilterSet):
    caption = CharFilter(field_name = 'caption', lookup_expr = 'icontains', label = 'Caption')
    
    class Meta:
        model = VideoPost
        fields = [
            'caption'
        ]
        
        
class AudioFilter(django_filters.FilterSet):
    caption = CharFilter(field_name = 'caption', lookup_expr = 'icontains', label = 'Caption')
    
    class Meta:
        model = AudioPost
        fields = [
            'caption'
        ]
        
        