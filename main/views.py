from .forms import ProjectForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project, Contact


@login_required(login_url='login')
def home(request):
    print("User authenticated:", request.user.is_authenticated)
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'projects': projects})

@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProjectForm()

    return render(request, 'add_project.html', {'form': form})


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        return redirect('contact')

    return render(request, 'contact.html')