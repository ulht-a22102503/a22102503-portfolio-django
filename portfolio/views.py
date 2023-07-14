from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post
from .forms import PostForm

# Create your views here.
def index_view(request):
	return render(request, 'portfolio/layout.html')


# Blog
def blog_home_view(request):
	context = {'posts': Post.objects.all()}
	return render(request, 'portfolio/blog/home.html', context)

def blog_new_post_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:blog_home')

    context = {'form': form}

    return render(request, 'portfolio/blog/new.html', context)

def blog_edit_post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog_home'))

    context = {'form': form, 'post_id': post_id}
    return render(request, 'portfolio/blog/edit.html', context)


def blog_remove_post_view(request, post_id):
    Post.objects.get(id=post_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blog_home'))














def discoparty_view(request):
	return render(request, 'portfolio/discoparty.html')

def random_view(request):
	return render(request, 'portfolio/random.html')
