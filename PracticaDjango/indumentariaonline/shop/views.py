from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import FormularioRemera
from .models import Remera


def index(request):
    remeras = Remera.objects.all()
    ctx = {"remeras": remeras}
    return render(request, "shop/index.html", ctx)


def contacto(request):
    return render(request, "shop/contacto.html")


def nueva_remera(request):
    if request.method == "POST":
        form = FormularioRemera(request.POST)
        if form.is_valid():
            Remera.objects.create(
                marca=form.cleaned_data["marca"],
                talle=form.cleaned_data["talle"],
                color=form.cleaned_data["color"],
                lisa=form.cleaned_data["lisa"],
                genero=form.cleaned_data["genero"]
            )
            return HttpResponseRedirect(reverse("index"))
    else:
        form = FormularioRemera()
    ctx = {"form": form}
    return render(request, "shop/nueva_remera.html", ctx)
