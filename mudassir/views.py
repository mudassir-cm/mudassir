from django.shortcuts import render, redirect
from mudassir.form import PersonForm
from mudassir.models import Person

def welcome(request):
    return render(request, 'mudassir/welcome.html')

def create(request):
    person = PersonForm
    return render(request, 'mudassir/create.html', {'person': person})

def add(request):
    form = PersonForm(request.POST)
    form.save()
    return redirect('/abc/show')

def show(request):
    list = Person.objects.all()
    return render(request, 'mudassir/show.html', {'list': list})

def delete(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    return redirect('/abc/show')

def edit(request, id):
    person = Person.objects.get(id=id)
    return render(request, 'mudassir/edit.html', {'person': person})

def update(request, id):
    person = Person.objects.get(id=id)
    form = PersonForm(request.POST, instance=person)
    form.save()
    return redirect('/abc/show')
# Create your views here.
