from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from student_App import forms
from student_App.forms import studentRegistration, updateForm
from student_App.models import stud


def add_student(request):

    form = studentRegistration()

    if request.method =="POST":
        form = studentRegistration(request.POST)
        if form.is_valid():
            form.save()

            form = studentRegistration

    return render(request, 'std/add.html', {'form': form})

def student_list(request):
    obj = stud.objects.all()
    return render(request,'std/list.html',{'obj':obj}) 

def delete(request,id):
    obj = stud.objects.get(pk=id)
    obj.delete()
    return redirect("/std/list/")

def update(request,id):
    
    obj = stud.objects.get(pk=id)
    form = updateForm(instance=obj)
    if request.method =="POST":
        form = updateForm(request.POST, instance=obj)
        if form.is_valid:
        
            form.save()

            return redirect("/std/list/")
    return render(request,"std/update.html",{"form": form})
   