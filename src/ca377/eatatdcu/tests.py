from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class IndexTests(TestCase):

    def test_welcome(self):
        """
        An appropriate welcome message is displayed once the page is loaded
        """
        response = self.client.get(reverse('eatatdcu:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Eat at DCU!")


