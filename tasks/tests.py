from django.test import TestCase
from .models import Task

# Create your tests here.
class TodoModelTest(TestCase):
    
    def setUp(self):
        self.task = Task.objects.create(title='Learn Unit Test', body='How to write a unit test for an app')
    
    def test_task_created_successfully(self):
        self.assertEqual(self.task.title, 'Learn Unit Test')
        self.assertEqual(self.task.body, 'How to write a unit test for an app')
        self.assertFalse(self.task.completed)
        self.assertIsNotNone(self.task.created_at)
    
    def test_str_method_returns_title(self):
        """Kiểm tra __str__() trả về đúng tên"""
        self.assertEqual(str(self.task),'Learn Unit Test')
    
    def test_mark_done_method(self):
        """Kiểm tra method mark_done hoạt động đúng"""
        self.task.mark_done()
        self.task.refresh_from_db()
        self.assertTrue(self.task.completed)
