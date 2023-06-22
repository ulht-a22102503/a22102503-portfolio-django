from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def layout_view(request):
	return render(request, 'portfolio/layout.html')

def discoparty_view(request):
	return render(request, 'portfolio/discoparty.html')

def random_view(request):
	return render(request, 'portfolio/random.html')
