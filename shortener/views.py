from django.http import HttpResponse
from .models import URLShortener
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import URLForm


def index(request):
    if request.method == "POST":
        error = ""
        form = URLForm(request.POST)
        form.save(commit=False)
        link = form.cleaned_data["url"]
        already_exists = URLShortener.objects.filter(url=link).exists()
        if already_exists:
            short_link = URLShortener.objects.get(url=link).shortened_url
        else:
            form.save()         
            short_link = URLShortener.objects.get(url=link).shortened_url
        form = URLForm
        if "www" not in link and "http" not in link:
            short_link = ""
            error = "Please enter a valid url"
        return render(request, "shortener/index.html", {"form": form, "short_link": short_link, "error": error})
    else:
        form = URLForm
        return render(request, "shortener/index.html", {"form": form})

def redirect_url(request, entered_url):
    try:
        link = URLShortener.objects.get(shortened_url = entered_url).url
        if "http" not in link:
            link = f"http://{link}"
        return HttpResponseRedirect(link)
    except:
        return HttpResponse(entered_url)


