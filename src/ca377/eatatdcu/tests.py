from django.test import TestCase
from django.urls import reverse
from django.core.urlresolvers import get_resolver

class A0Tests(TestCase):
   
    def test_welcome(self):
      """
      An appropriate welcome message is displayed once the page is loaded
      """
      response = self.client.get(reverse('eatatdcu:index'))
      self.assertEqual(response.status_code, 200)
      self.assertContains(response, "Eat at DCU!")

    def test_restaurants(self):
      """
      An appropriate message is displayed once the restaurants page is loaded
      """
      response = self.client.get(reverse('eatatdcu:restaurants'))
      self.assertEqual(response.status_code, 200)
      self.assertContains(response, "No restaurants found")



