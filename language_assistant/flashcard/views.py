# flashcards/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Flashcard, Category
from .forms import FlashcardForm, CategoryForm

@login_required
def flashcard_list(request):
    # Lấy flashcards và categories của user hiện tại
    flashcards = Flashcard.objects.filter(user=request.user).order_by('-created_at')
    categories = Category.objects.filter(user=request.user)
    
    # Lọc theo category nếu có
    category_id = request.GET.get('category')
    if category_id:
        flashcards = flashcards.filter(category_id=category_id)
    
    return render(request, 'flashcard/flashcards_list.html', {
        'flashcards': flashcards,
        'categories': categories,
        'selected_category': category_id
    })

@login_required
def flashcard_detail(request, pk):
    # Chỉ cho phép xem flashcard của user hiện tại
    flashcard = get_object_or_404(Flashcard, pk=pk, user=request.user)
    return render(request, 'flashcard/flashcards_detail.html', {'flashcard': flashcard})

@login_required
def flashcard_new(request):
    if request.method == "POST":
        form = FlashcardForm(request.POST)
        if form.is_valid():
            flashcard = form.save(commit=False)
            flashcard.user = request.user
            flashcard.save()
            messages.success(request, 'Flashcard đã được tạo thành công!')
            return redirect('flashcard:flashcard_detail', pk=flashcard.pk)
        else:
            messages.error(request, 'Vui lòng kiểm tra lại thông tin nhập vào.')
    else:
        form = FlashcardForm()
    
    # Chỉ hiển thị categories của user hiện tại trong form
    form.fields['category'].queryset = Category.objects.filter(user=request.user)
    
    return render(request, 'flashcard/flashcards_edit.html', {
        'form': form,
        'title': 'Tạo Flashcard Mới'
    })

@login_required
def flashcard_edit(request, pk):
    # Chỉ cho phép edit flashcard của user hiện tại
    flashcard = get_object_or_404(Flashcard, pk=pk, user=request.user)
    if request.method == "POST":
        form = FlashcardForm(request.POST, instance=flashcard)
        if form.is_valid():
            flashcard = form.save()
            messages.success(request, 'Flashcard đã được cập nhật thành công!')
            return redirect('flashcard:flashcard_detail', pk=flashcard.pk)
        else:
            messages.error(request, 'Vui lòng kiểm tra lại thông tin nhập vào.')
    else:
        form = FlashcardForm(instance=flashcard)
    
    # Chỉ hiển thị categories của user hiện tại trong form
    form.fields['category'].queryset = Category.objects.filter(user=request.user)
    
    return render(request, 'flashcard/flashcards_edit.html', {
        'form': form,
        'flashcard': flashcard,
        'title': 'Chỉnh Sửa Flashcard'
    })

@login_required
def flashcard_delete(request, pk):
    # Chỉ cho phép xóa flashcard của user hiện tại
    flashcard = get_object_or_404(Flashcard, pk=pk, user=request.user)
    if request.method == 'POST':
        flashcard.delete()
        messages.success(request, 'Flashcard đã được xóa thành công!')
        return redirect('flashcard:flashcard_list')
    return render(request, 'flashcard/flashcard_confirm_delete.html', {'flashcard': flashcard})

@login_required
def category_new(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            try:
                category.save()
                messages.success(request, 'Category đã được tạo thành công!')
                return redirect('flashcard:flashcard_list')
            except:
                messages.error(request, 'Category này đã tồn tại!')
        else:
            messages.error(request, 'Vui lòng kiểm tra lại thông tin nhập vào.')
    else:
        form = CategoryForm()
    return render(request, 'flashcard/category_form.html', {'form': form})

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk, user=request.user)
    if request.method == 'POST':
        # Xóa tất cả flashcards thuộc category này
        category.flashcard_set.all().delete()
        # Xóa category
        category.delete()
        messages.success(request, 'Category đã được xóa thành công!')
        return redirect('flashcard:flashcard_list')
    return render(request, 'flashcard/category_confirm_delete.html', {'category': category})
