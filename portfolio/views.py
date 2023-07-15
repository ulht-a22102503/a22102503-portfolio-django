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
    form = PostForm(request.POST or None, request.FILES)
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


#Labs 1-4
def pwlab1_view(request):
	return render(request, 'portfolio/labs/lab1.html')

def pwlab2_view(request):
	return render(request, 'portfolio/labs/lab2.html')

def pwlab3_view(request):
	return render(request, 'portfolio/labs/lab3.html')

def pwlab4_view(request):
	return render(request, 'portfolio/labs/lab4.html')
