from django.http import HttpResponse
from .models import URLShortener
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import URLForm
import validators


def index(request):
    if request.method == "POST":
        form = URLForm(request.POST)
        form.save(commit=False)
        link = form.cleaned_data["url"]
        already_exists = URLShortener.objects.filter(url=link).exists()
        short_link = URLShortener.objects.get(url=link).shortened_url
        if validators.url(short_link):
            if already_exists == False:
                form.save()   
        else:
            message_error = "Please enter a correct link"    
            short_link = None              
        form = URLForm
        return render(request, "shortener/index.html", {"form": form, "short_link": short_link, "message_error": message_error})
    else:
        form = URLForm
        return render(request, "shortener/index.html", {"form": form})

def redirect_url(request, entered_url):
    try:
        link = URLShortener.objects.get(shortened_url = entered_url).url
        if "http" not in link:
            link = f"https://{link}"
        print(link)
        return HttpResponseRedirect(link)
    except:
        return HttpResponse(entered_url)


