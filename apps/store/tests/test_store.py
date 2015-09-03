from uuid import uuid4

from django.test import TestCase
from django.db import IntegrityError, transaction
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import Group



from rest_framework.test import APIRequestFactory
from apps.common.tests.test_user import LiveTestBase

factory = APIRequestFactory()
request = factory.post('/stores/', {'name': 'Test Store Name'}, format='json')



from rest_framework.test import APIClient

client = APIClient()
client.login(username='lauren', password='secret')

response = client.post('/api/stores/', {'name': 'Test Store Name'})

client.logout()




from apps.store.views.store import StoreViewSet

# view = StoreViewSet.as_view()
# request = factory.get('/users/4')
# response = view(request, pk='4')
# response.render()  # Cannot access `response.content` without this.
# self.assertEqual(response.content, '{"username": "lauren", "id": 4}')



class StoreTests(APITestCase):

  def __init__(self):
    self.client = APIClient()

    #create and login as a User



    user_tester = LiveTestBase()
    self.user = user_tester.create_django_user(
                  email='john.doe@example.com',
                  given_name='John',
                  surname='Doe',
                  password='TestPassword123!')
    self.client.login(username='test.user@email.com', password='TestPassword123!')

  def create_new_user(self):
    UserModel = get_user_model()
    user = UserModel.objects.create_user(
            email='test.user@email.com',
            given_name='John',
            surname='Doe',
            password='TestPassword123!')

  def test_create_store(self):

    response = self.client.post('/api/stores/', {'name': 'Test Store Name'})
    self.assertEqual(response.data, {'name': 'Test Store Name'})





from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('stores')
        data = {'name': 'Test Store Name'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)



