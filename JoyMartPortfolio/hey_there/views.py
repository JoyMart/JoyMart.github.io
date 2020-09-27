from django.shortcuts import render
from .models import Project
from .form import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect


def hey_there(request):
    return render(request, 'hey_there.html')


def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def social(request):
    return render(request, 'social.html')


