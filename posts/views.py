from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm, PictureForm
from django.shortcuts import render
from django.urls import reverse_lazy, reverse

# Create your views here.
def index(request):
    if request.method =='POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')

        else:
            return HttpResponseRedirect(form.errors.as_json())

    # Get all posts, limit = 20
    posts = Post.objects.all()[:20]
    # Show
    return render(request, 'posts.html',
                  {'posts': posts}
    )


def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')
def edit(request, post_id):
    # if request.method == "GET":
    #     posts = Post.objects.get(id = post_id)
    #     return render(request, "edit.html", {"posts": posts})
    #post = Post.objects.get(id=post_id)
    post = Post.objects.get(id = post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    form = PostForm
    return render(request, 'edit.html', {'post': post, 'form': form})
def likes(request, post_id):
    likedtweet = Post.objects.get(id=post_id)
    likedtweet.like_count += 1
    likedtweet.save()
    return HttpResponseRedirect('/')