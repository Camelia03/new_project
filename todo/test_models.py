from django.test import TestCase
from .models import Task


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        task = Task.objects.create(name='Test Todo Task', done=False)
        self.assertFalse(task.done)

    def test_task_string_method_returns_name(self):
        task = Task.objects.create(name='Test Todo Task', done=True)
        self.assertEqual(str(task), 'Test Todo Task')
