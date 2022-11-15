from django.shortcuts import render
from .models import Listing

# Create your views here.

# basically going to be doing crud: create, retireve, update, delete, list(retireving multiple data)


def listing_list(request):
    listings = Listing.objects.all()
    context = {
        "listings": listings  # key points to values returned from db call
    }
    # request is required; html file is template; "context" refers to values to be injected into template
    return render(request, "listings.html", context)
