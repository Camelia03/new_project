from django.test import TestCase
from .models import Task

# Create your tests here.


class TestViews(TestCase):

    def test_get_todo_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_task_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_task.html')

    def test_get_edit_task_page(self):
        task = Task.objects.create(name='Test Todo Task', done=True)
        response = self.client.get(f'/edit/{task.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_task.html')

    def test_can_add_task(self):
        response = self.client.post('/add', {'name': 'Test Added Task'})
        self.assertRedirects(response, '/')

    def test_can_delete_task(self):
        task = Task.objects.create(name='Test Todo Task', done=True)
        response = self.client.get(f'/delete/{task.id}')
        self.assertRedirects(response, '/')
        existing_tasks = Task.objects.filter(id=task.id, done=True)
        self.assertEqual(len(existing_tasks), 0)

    def test_can_toggle_task(self):
        task = Task.objects.create(name='Test Todo Task', done=True)
        response = self.client.get(f'/toggle/{task.id}')
        self.assertRedirects(response, '/')
        updated_task = Task.objects.get(id=task.id)
        self.assertFalse(updated_task.done)

    def test_can_edit_task(self):
        task = Task.objects.create(name='Test Todo Task', done=False)
        response = self.client.post(
            f'/edit/{task.id}', {'name': 'Updated Name'})
        self.assertRedirects(response, '/')
        updated_task = Task.objects.get(id=task.id, done=False)
        self.assertEqual(updated_task.name, 'Updated Name')
