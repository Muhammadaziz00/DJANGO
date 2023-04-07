from django.test import TestCase, Client
from django.urls import reverse


class HelloViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_hello(self):
        response = self.client.get(reverse("index-page"))
        expected_date = "Hello"
        self.assertEqual(expected_date, response.connect.decode())
        self.assertEqual(500, response.status_code)
        self.assertEqual(response["Name"], "Alex")

    def test_about(self):
        response = self.client.get(reverse('about-views'))
        excepted_data = "как-то так"
        self.assertEqual(excepted_data, response.content.decode())


    
    def test_contacts(self):
        response = self.client.get(reverse('contacts-views'))
        excepted_data = "как-то так2"
        self.assertEqual(excepted_data, response.content.decode())
