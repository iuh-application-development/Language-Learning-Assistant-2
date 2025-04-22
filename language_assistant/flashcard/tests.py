from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Flashcard, Category

class FlashcardTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='testemail@gmail.com',
            password='password123'
        )
        self.category = Category.objects.create(name='Test Category', user=self.user)
        self.flashcard = Flashcard.objects.create(
            question='What is Django?',
            answer='A web framework for Python.',
            category=self.category,
            user=self.user
        )

    def test_flashcard_list_view(self):
        self.client.login(email='testemail@gmail.com', password='password123')
        response = self.client.get(reverse('flashcard:flashcard_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'What is Django?')

    def test_flashcard_detail_view(self):
        self.client.login(email='testemail@gmail.com', password='password123')
        response = self.client.get(reverse('flashcard:flashcard_detail', args=[self.flashcard.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A web framework for Python.')

    def test_flashcard_create_view(self):
        self.client.login(email='testemail@gmail.com', password='password123')
        response = self.client.post(reverse('flashcard:flashcard_new'), {
            'question': 'What is Python?',
            'answer': 'A programming language.',
            'category': self.category.pk
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Flashcard.objects.filter(question='What is Python?').exists())

    def test_flashcard_edit_view(self):
        self.client.login(email='testemail@gmail.com', password='password123')
        response = self.client.post(reverse('flashcard:flashcard_edit', args=[self.flashcard.pk]), {
            'question': 'What is Django?',
            'answer': 'A high-level Python web framework.',
            'category': self.category.pk
        })
        self.assertEqual(response.status_code, 302)
        self.flashcard.refresh_from_db()
        self.assertEqual(self.flashcard.answer, 'A high-level Python web framework.')

    def test_flashcard_delete_view(self):
        self.client.login(email='testemail@gmail.com', password='password123')
        response = self.client.post(reverse('flashcard:flashcard_delete', args=[self.flashcard.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Flashcard.objects.filter(pk=self.flashcard.pk).exists())
