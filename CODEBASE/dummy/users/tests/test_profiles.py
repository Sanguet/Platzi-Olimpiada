# Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Utils
from dummy.utils.authenticate import get_tokens_for_user

# Model
from dummy.users.models import User, Profile


class ProfileAPITestCase(APITestCase):
    """Member invitation API test case."""

    def setUp(self):
        """Test case setup."""

        # URL
        self.url = '/profiles/'

        # Data

        self.user = User.objects.create_user(
            email='test@gmail.com',
            username='admin@testSRL',
            password='admin123',
            is_verified=True
        )

        self.profile = Profile.objects.create(
            user=self.user,
            first_name='Test profile'
        )

        # Auth
        self.token = get_tokens_for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(self.token))

    def test_create_profile(self):
        """Testeo de la creacion del perfil"""
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(Profile.objects.count(), 1)

    def test_list_profiles(self):
        """Testeo de la lista de perfiles"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_update_profile(self):
        """Testeo de actualizar el perfil"""
        url = self.url
        url = url + '{}/'.format(
            self.profile.pk
        )
        response = self.client.patch(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        update_data = {
            'first_name': 'UpdateTest'
        }

        response = self.client.patch(url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Caso 1
        update_data['points'] = 'Muchos puntos'
        response = self.client.patch(url, update_data, format='json')
        self.assertEqual(response.data['points'], 0)

    def test_delete_profile(self):
        """Testeo de la eliminacion de perfiles"""
        url = self.url
        url = url + '{}/'.format(
            self.profile.pk
        )
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(Profile.objects.count(), 1)
