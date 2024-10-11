import unittest
import json
from bson.objectid import ObjectId
from app import app  # Importez votre application Flask ici

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        # Créez un utilisateur et une tâche pour les tests
        self.user_id = ObjectId()  # Remplacez par un ID d'utilisateur valide
        self.task_data = {
            "title": "Test Task",
            "description": "This is a test task.",
            "assigned_to": str(self.user_id),
            "status": "à faire",
            "due_date": "2024-10-09"
        }

    def test_create_task(self):
        response = self.app.post('/tasks', data=json.dumps(self.task_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('task_id', json.loads(response.data))

    def test_update_task(self):
        # Créer d'abord une tâche
        response = self.app.post('/tasks', data=json.dumps(self.task_data), content_type='application/json')
        task_id = json.loads(response.data)['task_id']

        # Mise à jour de la tâche
        updated_data = {
            "title": "Updated Task",
            "status": "en cours"
        }
        response = self.app.put(f'/tasks/{task_id}', data=json.dumps(updated_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('msg', json.loads(response.data))

    def test_get_user_tasks(self):
        response = self.app.get(f'/tasks/user/{self.user_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data), list)  # Vérifie que la réponse est une liste

    def test_delete_task(self):
        # Créer d'abord une tâche
        response = self.app.post('/tasks', data=json.dumps(self.task_data), content_type='application/json')
        task_id = json.loads(response.data)['task_id']

        # Suppression de la tâche
        response = self.app.delete(f'/tasks/{task_id}')
        self.assertEqual(response.status_code, 204)

        # Vérifiez que la tâche a bien été supprimée
        response = self.app.get(f'/tasks/{task_id}')
        self.assertEqual(response.status_code, 404)  # Vérifie que la tâche n'existe plus

    def test_get_user_tasks_no_tasks(self):
        # Teste pour un utilisateur sans tâches
        response = self.app.get('/tasks/user/non_existing_user_id')
        self.assertEqual(response.status_code, 404)
        self.assertIn('Aucune tâche assignée à cet utilisateur.', json.loads(response.data)['message'])

if __name__ == '__main__':
    unittest.main()
