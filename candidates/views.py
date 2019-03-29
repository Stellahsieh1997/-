from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages

from core.forms import DeleteConfirmform

from .models import Candidate
from .forms import CandidateForm


def index(request):
    candidates = Candidate.objects.all()
    return render(request, 'candidates/index.html', {
        'candidates': candidates,
    })


def add(request):
    form = CandidateForm(request.POST or None)
    if form.is_valid():
        form.save()
        message.success(request, '新增成功')
        return redirect('/candidates/')

    return render(request, 'candidates_add.html', {
        'form': form,
    })


def edit(request, pk):
    #select * from candidate where id=<pk>
    #candidate=candidate.object.get(pk=pk)
    candidate= get_object_or_404(Candidate,pk=pk)
    form = CandidateForm(request.POST or None, instance=candidate)
    if form.is_valid():
        form.save()
        message.success(request, '編輯成功')
        return redirect('/candidates/')

    return render(request, 'candidates_edit.html', {
        'form': form,
    })

def delete(request, pk):
    candidate=get_object_or_404(Candidate,pk=pk)
    form=DeleteConfirmform(request.POST or None)
    if form.is_valid():
        candidate.delete()
        message.success(request, '刪除成功')
        return redirect('/candidates')

    return render(request, 'candidates_delete.html',{
        'form':form,
    })


def show(request, pk):
    candidate = get_object_or_404(candidate, pk=pk)
    return render(request, 'candidate/show.html' ,{
        'candidate'
    }