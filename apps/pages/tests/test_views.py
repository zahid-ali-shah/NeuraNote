from django.test import TestCase
from django.urls import reverse


class PagesViewsTest(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home.html')

    def test_contact_us_view(self):
        response = self.client.get(reverse('contact_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/contact_us.html')

    def test_privacy_policy_view(self):
        response = self.client.get(reverse('privacy_policy'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/privacy_policy.html')

    def test_terms_of_service_view(self):
        response = self.client.get(reverse('terms_of_service'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/terms_of_service.html')
