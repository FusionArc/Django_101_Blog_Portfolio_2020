from django.shortcuts import render
from projects.models import Project
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.shortcuts import redirect
from django.utils import timezone


def index(request):
    context = {}
    return render(request, 'index.html', context)


def project_index(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {'project': project}
    return render(request, 'project_detail.html', context)
