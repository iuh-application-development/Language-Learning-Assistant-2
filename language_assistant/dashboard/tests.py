from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class DashboardViewTests(TestCase):

    # TEST HOME PAGE
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

    