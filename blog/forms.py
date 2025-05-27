from django import forms
from .models import Post, PostComment
from django.forms import CheckboxSelectMultiple

class PostAdminForm(forms.ModelForm):    
    class Meta:
        model = Post
        fields = ['user', 'title', 'content']
        
        
class PostForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter an engaging title...',
            'maxlength': 200
        })
    )
    content = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Enter your post content...',
        'rows': 10
    }))

    class Meta:
        model = Post
        fields = ['title', 'content']
        
        
class PostCommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))
    
    class Meta:
        model = PostComment
        fields = ['name', 'email', 'content']
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.post = kwargs.pop('post', None)
        super().__init__(*args, **kwargs)
   
        
    def clean(self):
        cleaned_data = super().clean()
        
        if not (self.user and self.post):
            raise forms.ValidationError('User and Post are required.')
        
        return cleaned_data
        
    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.user = self.user
        comment.post = self.post
        
        if commit:
            comment.save()
            
        return comment
        
class CommentReplyForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}))
    
    class Meta:
        model = PostComment
        fields = ['content']
        
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.post = kwargs.pop('post', None)
        self.comment = kwargs.pop('comment', None)
        super().__init__(*args, **kwargs)
        
    def clean(self):
        cleaned_data = super().clean()
        
        if not (self.user and self.post and self.comment):
            raise forms.ValidationError('User, Post and Comment are required.')
        
        return cleaned_data
    
    def save(self, commit=True):
        reply = super().save(commit=False)
        reply.user = self.user
        reply.post = self.post
        reply.parent = self.comment
        
        if commit:
            reply.save()
            
        return reply