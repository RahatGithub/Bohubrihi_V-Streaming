from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from App_Posts.models import Post, Comment
from App_Posts.forms import CommentForm
from django.contrib.auth.models import User 
from django.db.models import Q  # used for complex queries


def home(request):
    posts = Post.objects.all()

    if request.method == 'GET':
        search = request.GET.get('search', '')
        result = Post.objects.filter(Q(title__icontains=search) | Q(category__icontains=search))   # Q is used for complex queries 
        context={
            'title':'Home . V-Streaming', 
            'search':search, 
            'result':result, 
            'posts':posts, 
        }
    return render(request, 'App_Posts/home.html', context)



# ***********WE'RE WORKING HERE***********

def post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    form = CommentForm()

    comments = Comment.objects.filter(post=post)
    print(comments)

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('comment')
            comment = Comment(post=post, user=request.user, comment=text)
            comment.save()
            return HttpResponseRedirect(reverse('App_Posts:post_view', args=[post_id]))
            
    context = {
        'title' : 'post_view . v-stream', 
        'post' : post, 
        'form' : form,
        'comments' : comments
    }

    return render(request, 'App_Posts/post_view.html', context)