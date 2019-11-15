from django.shortcuts import render, get_object_or_404
from .models import Realtor, Immo

# Create your views here.
def home(request):
    immos = Immo.objects.all()
    context = {'immos': immos}
    return render(request, "immo/index.html", context)

def listing(request):
    immos = Immo.objects.all()
    context = {'immos': immos}
    return render(request, "immo/listing.html", context)

def listing_detail(request, immo_id):
    immo = get_object_or_404(Immo, pk=immo_id)
    context = {'immo': immo}
    return render(request, "immo/listing_detail.html", context)

