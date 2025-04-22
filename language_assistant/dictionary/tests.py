from django.test import TestCase, Client
from django.urls import reverse
from users.models import MyUser
from flashcard.models import Category, Flashcard

class DictionaryViewTests(TestCase):

    def setUp(self):
        # Tạo user và đăng nhập
        self.user = MyUser.objects.create_user(email='testemail@gmail.com', password='testpassword')
        self.client = Client()
        self.client.login(email='testemail@gmail.com', password='testpassword')

        # Tạo category cho user
        self.category = Category.objects.create(name='Test Category', user=self.user)

    def test_dictionary_view_get(self):
        # Kiểm tra truy cập GET vào view dictionary
        response = self.client.get(reverse('dictionary:dictionary'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dictionary/dictionary.html')
        self.assertIn('categories', response.context)
        self.assertEqual(len(response.context['categories']), 1)

    def test_dictionary_view_post(self):
        # Kiểm tra POST để tạo flashcard
        post_data = {
            'word': 'testword',
            'meaning': 'testmeaning',
            'category': self.category.id
        }
        response = self.client.post(reverse('dictionary:dictionary'), data=post_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], True)

        # Kiểm tra flashcard được tạo
        flashcard = Flashcard.objects.get(question='testword')
        self.assertEqual(flashcard.answer, 'testmeaning')
        self.assertEqual(flashcard.category, self.category)
        self.assertEqual(flashcard.user, self.user)

    def test_dictionary_view_post_invalid_category(self):
        # Kiểm tra POST với category không hợp lệ
        post_data = {
            'word': 'testword',
            'meaning': 'testmeaning',
            'category': 9999  # ID không tồn tại
        }
        response = self.client.post(reverse('dictionary:dictionary'), data=post_data)
        self.assertEqual(response.status_code, 400)