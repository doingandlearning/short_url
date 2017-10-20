from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .models import ShortURL
from .forms import SubmitUrlForm
# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title" : "Shorten URL",
            "form" : the_form
        }
        return render(request, "shortener/home.html", context)
    
    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            "title" : "Shorten URL",
            "form": form
            }
        template = "shortener/home.html"
        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            obj, created = ShortURL.objects.get_or_create(url=new_url)
            context = {
                "object": obj,
                "created": created
            }
            if created:
                template = "shortener/success.html"
            else:
                template = "shortener/already-exists.html"
        
        return render(request, template, context)

class short_view(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        print(shortcode)
        obj = get_object_or_404(ShortURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)

