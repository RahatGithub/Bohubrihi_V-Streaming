from django import forms 
from App_Posts.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta: 
        model = Post 
        fields = ['title', 'description', 'video_link']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 2, 'cols': 30}),  
        }