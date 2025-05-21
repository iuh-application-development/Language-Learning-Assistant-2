# Language-Learning-Assistant-2/language_assistant/dictionary/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from flashcard.models import Category, Flashcard
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

@login_required
def dictionary(request):
    categories = Category.objects.filter(user=request.user)  # Lấy danh sách category của user hiện tại
    if request.method == "POST":
        word = request.POST.get('word')
        vietnamese_meaning = request.POST.get('meaning')  # Lấy nghĩa từ POST
        category_id = request.POST.get('category')
        try:
            category = Category.objects.get(id=category_id)
        except ObjectDoesNotExist:
            return JsonResponse({'success': False, 'error': 'Category does not exist'}, status=400)

        # Tạo flashcard
        flashcard = Flashcard.objects.create(
            question=word,
            answer=vietnamese_meaning,
            category=category,
            user=request.user
        )
        return JsonResponse({'success': True, 'flashcard_id': flashcard.id, 'meaning': vietnamese_meaning})

    return render(request, 'dictionary/dictionary.html', {
        'categories': categories,
    })