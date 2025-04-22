from django.test import Client, TestCase
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