from django.shortcuts import render, get_object_or_404 # We will use it later

from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.
from .models import Shortener
from .forms import ShortenerForm

def home_view(request):
    print("all shortener: ", Shortener.objects.all())
    
    template = 'home.html'

    context = {}

    # Empty form
    context['form'] = ShortenerForm()

    if request.method == 'GET':
        return render(request, template, context)

    elif request.method == 'POST':

        used_form = ShortenerForm(request.POST)
        print("request.POST: ", request.POST)
        if used_form.is_valid():
            print("isvalid")
            
            shortened_object = used_form.save()
            print("shortened object: ", shortened_object)
            new_url = request.build_absolute_uri('/') + shortened_object.short_url
            print("new url: ", new_url)
            long_url = shortened_object.long_url 
            print("Long url: ", long_url)
            context['new_url']  = new_url
            context['long_url'] = long_url
            print("request.POST: ", request.POST)
            return render(request, template, context)

        context['errors'] = used_form.errors

        return render(request, template, context)

def redirect_url_view(request, shortened_part):

    try:
        shortener = Shortener.objects.get(short_url=shortened_part)
        shortener.times_followed += 1        

        shortener.save()
        
        return HttpResponseRedirect(shortener.long_url)
        
    except:
        raise Http404('Sorry this link is broken :(')