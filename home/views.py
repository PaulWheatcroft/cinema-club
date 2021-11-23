from django.shortcuts import render


# Create your views here.
def home(request, *args, **kwargs):
    """ A view to return the index page """
    return render(request, "home/index.html")
