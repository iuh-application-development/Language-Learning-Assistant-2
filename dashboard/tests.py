from django.test import Client, TestCase
from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class DashboardViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('dashboard:home')  # Replace with your actual URL name

    def test_dashboard_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)  # Check if the response is OK (200)

    def test_dashboard_view_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'dashboard/index.html')  # Replace with your actual template name

    def test_home_reverse_url(self):
        url = reverse('dashboard:home')  # Replace with your actual URL name
        self.assertEqual(url, '/')  # hoặc đường dẫn bạn đã set

    # TEST ABOUT PAGE

    def test_about_view_status_code(self):
        response = self.client.get(reverse('dashboard:about'))  # Replace with your actual URL name
        self.assertEqual(response.status_code, 200)  # Check if the response is OK (200)

    def test_about_view_template_used(self):
        response = self.client.get(reverse('dashboard:about'))  
        self.assertTemplateUsed(response, 'dashboard/about.html')

    def test_about_reverse_url(self):
        url = reverse('dashboard:about')  
        self.assertEqual(url, '/about/')

    # TEST CONTACT PAGE

    def test_contact_view_status_code(self):
        response = self.client.get(reverse('dashboard:contact'))  # Replace with your actual URL name
        self.assertEqual(response.status_code, 200)

    def test_contact_view_template_used(self):
        response = self.client.get(reverse('dashboard:contact'))  
        self.assertTemplateUsed(response, 'dashboard/contact.html')

    # TEST LOGIN PAGE

    def test_login_view_status_code(self):
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)

    def test_login_view_template_used(self):
        response = self.client.get(reverse('users:login'))
        self.assertTemplateUsed(response, 'users/login.html')

    def test_login_reverse_url(self):
        url = reverse('users:login')
        self.assertEqual(url, '/login/')

    # TEST REGISTER PAGE

    def test_register_view_status_code(self):
        response = self.client.get(reverse('users:register'))
        self.assertEqual(response.status_code, 200)

    def test_register_view_template_used(self):
        response = self.client.get(reverse('users:register'))
        self.assertTemplateUsed(response, 'users/signup.html')

    def test_register_reverse_url(self):
        url = reverse('users:register')
        self.assertEqual(url, '/register/')

    
