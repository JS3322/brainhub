from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from django.views.generic import View
from django.http import Http404
from django.shortcuts import render
from . import models, forms


def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/home.html", {"page": rooms})
    except EmptyPage:
        return redirect("/")


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/room_detail.html", {"room": room})
    except models.Room.DoesNotExist:
        raise Http404()


def search(request):
    form = forms.SearchForm()
    return render(request, "rooms/search.html", {"form": form})
