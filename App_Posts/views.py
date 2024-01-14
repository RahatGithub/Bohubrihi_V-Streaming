from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from App_Posts.models import Post 
from django.contrib.auth.models import User 
from django.db.models import Q  # used for complex queries


def home(request):
    posts = Post.objects.all()
    # liked_post = Like.objects.filter(user=request.user)
    # liked_post_list = liked_post.values_list('post', flat=True)

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