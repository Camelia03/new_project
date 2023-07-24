from django.test import TestCase
from .models import Task


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        task = Task.objects.create(name='Test Todo Task', done=False)
        self.assertFalse(task.done)
