from django.shortcuts import render, get_object_or_404, redirect
from .models import Entrega
from .forms import EntregaForm

# Create your views here.
def entrega_list(request):
    entregas = Entrega.objects.all().order_by('id')
    return render(request, "entregas/entrega_list.html", {"entregas": entregas})


def entrega_detail(request, id):
    entrega = get_object_or_404(Entrega, id=id)
    return render(request, "entregas/entrega_detail.html", {"entrega": entrega})


def entrega_create(request):
    if request.method == "POST":
        form = EntregaForm(request.POST)
        if form.is_valid():
            entrega = form.save()
            return redirect("entrega_detail", id=entrega.id)
    else:
        form = EntregaForm()
    return render(request, "entregas/entrega_form.html", {"form": form})


def entrega_update(request, id):
    entrega = get_object_or_404(Entrega, id=id)
    if request.method == "POST":
        form = EntregaForm(request.POST, instance=entrega)
        if form.is_valid():
            entrega = form.save()
            return redirect("entrega_detail", id=entrega.id)
    else:
        form = EntregaForm(instance=entrega)
    return render(request, "entregas/entrega_form.html", {"form": form})


def entrega_delete(request, id):
    entrega = get_object_or_404(Entrega, id=id)
    if request.method == "POST":
        entrega.delete()
        return redirect("entrega_list")
    return render(request, "entregas/entrega_delete.html", {"entrega": entrega})
