# Language-Learning-Assistant-2/language_assistant/assistant/tests.py
from django.test import TestCase
from django.urls import reverse
import json

class AssistantViewsTestCase(TestCase):
    def setUp(self):
        # Thiết lập dữ liệu cần thiết cho các test case
        self.home_url = reverse('chatbot_view')
        self.voice_api_url = reverse('voice_api')

    def test_home_view(self):
        # Kiểm tra xem view home có trả về mã trạng thái 200 không
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'assistant/chatbot.html')

    def test_voice_api_valid_request(self):
        # Kiểm tra API voice với yêu cầu hợp lệ
        response = self.client.post(self.voice_api_url, 
                                    json.dumps({"text": "Hello", "lang": "en"}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'audio/wav')  # Kiểm tra kiểu nội dung
        self.assertGreater(len(response.content), 0)  # Đảm bảo rằng có dữ liệu trong phản hồi
        
    def test_voice_api_invalid_request(self):
        # Kiểm tra API voice với yêu cầu không hợp lệ (JSON không hợp lệ)
        response = self.client.post(self.voice_api_url, 
                                     "invalid json",
                                     content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {"error": "Invalid JSON"})

    def test_voice_api_no_text(self):
        # Kiểm tra API voice với yêu cầu không có văn bản
        response = self.client.post(self.voice_api_url, 
                                     json.dumps({"text": "", "lang": "en"}),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {"error": "No text provided"})

    def test_voice_api_unsupported_language(self):
        # Kiểm tra API voice với ngôn ngữ không được hỗ trợ
        response = self.client.post(self.voice_api_url, 
                                     json.dumps({"text": "Hello", "lang": "fr"}),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {"error": "Unsupported language"})