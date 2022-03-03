from django.shortcuts import render, redirect
import datetime
from .models import Note

# Create your views here.
def index(request):
    context = {}
    notes = Note.objects.all()
    context['notes'] = notes
    return render(request, "notiteApp/home.html", context)

def add(request):
    context = {}

    if request.method == "POST":
        title = request.POST['note-title']
        content = request.POST['note-content']
        importance = request.POST['note-importance']

        note = Note(title=title, content=content, importance=importance)
        note.save()
        return redirect('notiteApp:index')

    return render(request, "notiteApp/add.html", context)

def delete(request, id):
    context = {}

    if request.method == "POST":
        note = Note.objects.get(id=id)
        note.delete()
        return redirect('notiteApp:index')

    return redirect('notiteApp:index')