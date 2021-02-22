# Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Utils
from dummy.utils.authenticate import get_tokens_for_user
from dummy.taskapp.tasks import gen_verification_token

# Model
from dummy.users.models import User, Profile


class UserAPITestCase(APITestCase):
    """Member invitation API test case."""

    def setUp(self):
        """Test case setup."""

        # URL
        self.url = '/users/'

        # Data base

        self.data = {
            'email': 'test@gmail.com',
        }

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

    def test_list_user(self):
        """Testeo de la lista de usuarios para el admin"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_create_user(self):
        """Testeo de la creacion de un user por un admin"""

        # User
        create_data = {
            'email': 'test2@gmail.com',
            'username': 'pedro',
            'work_range': 'E'
        }

        response = self.client.post(self.url, create_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(Profile.objects.count(), 2)

    def test_signup_user(self):
        """Testeo de la creacion de cuenta"""
        url = self.url
        url = url + 'signup/'

        create_data = {
            'email': 'test2@gmail.com',
        }

        response = self.client.post(url, create_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

        # Profile test
        self.assertEqual(Profile.objects.count(), 2)

        # Case 2
        self.data['email'] = 'test2@gmail.com'
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_verify_user(self):
        """Testeo de la verificacion de cuenta"""
        # Verificar la cuenta
        url = self.url
        url = url + 'verify/'

        verify_data = {
            'token': '232dasnj2ihhuihda9823jaiskd'
        }

        response = self.client.post(url, verify_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Token creation
        user = User.objects.get()
        token = gen_verification_token(user=user, type_token='email_confirmation')

        # Final case
        verify_data['token'] = token
        response = self.client.post(url, verify_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_user(self):
        """Testeo de la obtencion del usuario"""

        # Retrieve
        url = self.url
        url = url + '{}/'.format(
            self.user.username,
        )

        response = self.client.get(url)
        profile_id = Profile.objects.get().pk
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user']['username'], self.user.username)
        self.assertEqual(response.data['profile']['id'], profile_id)

    def test_update_user(self):
        # Update
        url = self.url
        url = url + '{}/'.format(
            self.user.username,
        )
        response = self.client.patch(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        update_data = {
            'username': 'TestFall',
            'email': 'testfall@gmail.com',
        }

        response = self.client.patch(url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], update_data['username'])
        self.assertEqual(response.data['email'], update_data['email'])

    def test_change_password_user(self):
        """Testeo del cambio de contraseña"""
        # Change password
        url = self.url
        url = url + 'change_password/'
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.user.set_password('admin123')
        self.user.save()

        password_data = {
            'old_password': 'admin123',
            'new_password': 'admin1234',
            'new_password_confirmation': 'admin1234'
        }

        response = self.client.post(url, password_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = User.objects.get()
        self.assertEqual(user.check_password('admin1234'), True)

        # Caso 1
        response = self.client.post(url, password_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Caso 2
        password_data = {
            'old_password': 'admin1234',
            'new_password': 'admin1234567',
            'new_password_confirmation': 'admin1234'
        }
        response = self.client.post(url, password_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_email_reset_passoword(self):
        """Testeo del envio de email reset password"""
        # Enviar email de reset password
        url = self.url
        url = url + 'email_password/'
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        email_data = {
            'email': self.user.email,
        }

        response = self.client.post(url, email_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Caso 1
        email_data['email'] = 'fallo@gmail.com'
        response = self.client.post(url, email_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_rest_password(self):
        """Testeo del reseteo de contraseña"""
        # Reseteo de contraseña falso
        url = self.url
        url = url + 'reset_password/'
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Crear token
        user = User.objects.get()
        token = gen_verification_token(user=user, type_token='reset_password')

        # Reset
        password_data = {
            'token': token,
            'new_password': 'admin1234',
            'new_password_confirmation': 'admin1234'
        }

        response = self.client.post(url, password_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user = User.objects.get()
        self.assertEqual(user.check_password(password_data['new_password']), True)

        # Caso 1
        password_data['token'] = 'asdawyu12tyghjdnaw7832y1uhjnads'
        response = self.client.post(url, password_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Caso 2
        password_data['token'] = token
        password_data['new_password'] = 'testfallido'
        response = self.client.post(url, password_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_user(self):
        """Testeo de eliminacion de cuenta"""
        # Eliminar cuenta
        url = self.url
        url = url + '{}/'.format(
            self.user.username,
        )
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        user = User.objects.get()
        self.assertEqual(user.is_active, False)
