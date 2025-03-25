# flashcards/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Flashcard, Category
from .forms import FlashcardForm, CategoryForm

def flashcard_list(request):
    flashcards = Flashcard.objects.all()
    categories = Category.objects.all()
    return render(request, 'flashcard/flashcards_list.html', {
        'flashcards': flashcards,
        'categories': categories
    })

def flashcard_detail(request, pk):
    flashcard = get_object_or_404(Flashcard, pk=pk)
    return render(request, 'flashcard/flashcards_detail.html', {'flashcard': flashcard})

def flashcard_new(request):
    if request.method == "POST":
        form = FlashcardForm(request.POST)
        if form.is_valid():
            flashcard = form.save()
            return redirect('flashcard:flashcard_detail', pk=flashcard.pk)
    else:
        form = FlashcardForm()
    return render(request, 'flashcard/flashcards_edit.html', {'form': form})

def flashcard_edit(request, pk):
    flashcard = get_object_or_404(Flashcard, pk=pk)
    if request.method == "POST":
        form = FlashcardForm(request.POST, instance=flashcard)
        if form.is_valid():
            flashcard = form.save()
            return redirect('flashcard:flashcard_detail', pk=flashcard.pk)
    else:
        form = FlashcardForm(instance=flashcard)
    return render(request, 'flashcard/flashcards_edit.html', {'form': form})

def flashcard_delete(request, pk):
    flashcard = get_object_or_404(Flashcard, pk=pk)
    if request.method == 'POST':
        flashcard.delete()
        return redirect('flashcard:flashcard_list')
    return render(request, 'flashcard/flashcards_list.html', {'flashcard': flashcard})


def category_new(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flashcard:flashcard_list')
    else:
        form = CategoryForm()
    return render(request, 'flashcard/category_form.html', {'form': form})
