from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationTestCase(TestCase):
    def setUp(self):
        self.valid_user_data = {
            'email' : 'exampletest@gmail.com',
            'password1' : '0987pa$$w0rd',
            'password2' : '0987pa$$w0rd',
        }
    # Test 1
    def test_user_registration(self):
        response = self.client.post(reverse('users:register'), data=self.valid_user_data)
        self.assertEqual(response.status_code, 302) 
        
        # sử dụng 302 thay vì 200 vì : Django thường sẽ redirect (mã trạng thái 302) sau khi đăng ký thành công.
        # Nếu bạn vẫn muốn giữ assertEqual(status_code, 200) thì nên dùng nó trong test form lỗi (ví dụ: nhập sai password), 
        # còn với form hợp lệ thì Django sẽ redirect và cần dùng 302.
        
        
        self.assertEqual(response.url, reverse('users:login'))  # Kiểm tra xem có chuyển hướng đến trang đăng nhập không
        self.assertTrue(User.objects.filter(email='exampletest@gmail.com').exists())


    # Test 2
    def test_registration_with_mismatched_passwords(self):
        response = self.client.post(reverse('users:register'), {
            'email': 'newuser@example.com',
            'password1': 'securepassword123',
            'password2': 'differentpassword',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The two password fields didn’t match.")
        self.assertFalse(User.objects.filter(email='newuser@example.com').exists())

    # Test 3
    def test_registration_with_existing_username(self):
        User.objects.create_user(email='existingmail@gmail.com', password='password123#')
        response = self.client.post(reverse('users:register'), {
   
            'email': 'existingmail@gmail.com',
            'password1': 'securepassword123',
            'password2': 'securepassword123',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "User with this Email already exists.")

    # Test 4
    def test_registration_with_invalid_email(self):
        response = self.client.post(reverse('users:register'), {

            'email': 'invalid-email@',
            'password1': 'securepassword123',
            'password2': 'securepassword123',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Enter a valid email address.")
        self.assertFalse(User.objects.filter(email='invalid-email@').exists())

    # Test 5
    def test_registration_with_empty_fields(self):
        response = self.client.post(reverse('users:register'), {
            'email': '',
            'password1': '',
            'password2': '',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required.")
        self.assertFalse(User.objects.filter(email='').exists())

    # Test 6
    def test_registration_with_short_password(self):
        response = self.client.post(reverse('users:register'), {
            'email': 'exampletest6@gmail.com',
            'password1': '1',
            'password2': '1',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This password is too short. It must contain at least 8 characters.")
        self.assertContains(response, "This password is too common.")
        self.assertContains(response, "This password is entirely numeric.")

    def test_create_user(self):
        user = User.objects.create_user(email='testcreateuser@gmail.com', password='12345')
        self.assertEqual(user.email, 'testcreateuser@gmail.com')
        self.assertTrue(user.check_password('12345'))


# LOGIN TEST CASES
class UserLoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('users:login')  
        self.email = 'testuser@gmail.com'
        self.password = '$$strongPassword123'
        self.user = User.objects.create_user(email=self.email, password=self.password)

    # Test 1
    def test_login_page_loads(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)

    # Test 2
    def test_login_success(self):
        response = self.client.post(self.login_url, {
            'email': self.email,
            'password': self.password
        })
        self.assertEqual(response.status_code, 302)  # Thường redirect khi login thành công

    # Test 3
    def test_login_invalid_password(self):
        response = self.client.post(self.login_url, {
            'email': self.email,
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Email or password is not correct")
    
    # Test 4
    def test_login_invalid_email(self):
        response = self.client.post(self.login_url, {
            'email': 'invalid@mail',
            'password': self.password,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Enter a valid email address.")
        self.assertContains(response, "Email or password is required")

    # Test 5
    def test_login_empty_fields(self):
        response = self.client.post(self.login_url, {
            'email': '',
            'password': '',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Email or password is required")
