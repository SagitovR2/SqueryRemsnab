from django.shortcuts import render
from .models import Abduction, Applience, People, Type, Bringing, Repair
from .forms import AbductionForm, ApplienceForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect


def post_new(request):
    if request.method == "POST":
        form = AbductionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'blog/post_edit.html', {'form': form})
    else:
        form = AbductionForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def applience_new(request):
    if request.method == "POST":
        form = ApplienceForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.save()
            return render(request, 'blog/tablet.html', {'form': form})
    else:
        form = ApplienceForm()
    return render(request, 'blog/tablet.html', {'form': form})


def post_list(request):
    return render(request, 'blog/post_list.html', {})


def abduction(request):
    abductions = Abduction.objects.all()
    return render(request, 'blog/abduction.html', {'uvoz': abductions})


def applience(request):
    appliences = Applience.objects.all()
    return render(request, 'blog/applience.html', {'pribori': appliences})


def table(request):
    appliences = Applience.objects.all()
    return render(request, 'blog/table.html', {'pribori': appliences})


def bringing(request):
    bringings = Bringing.objects.all()
    return render(request, 'blog/bringing.html', {'privoz': bringings})


def people(request):
    persons = People.objects.all()
    return render(request, 'blog/people.html', {'ludi': persons})


def repair(request):
    repairs = Repair.objects.all()
    return render(request, 'blog/repair.html', {'remont': repairs})


def type(request):
    types = Type.objects.all()
    return render(request, 'blog/type.html', {'tip': types})
# Create your views here.
