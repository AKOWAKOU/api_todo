# API de Gestion des Tâches

Cette API permet de gérer des tâches avec des utilisateurs assignés, des statuts et des dates d'échéance.


## Installation

1. Cloner le projet :

```bash
git clone git@github.com:AKOWAKOU/api_todo.git
cd api_todo
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install --upgrade pip
docker compose up --build

## Endpoints

1. Créer une Tâche
URL : http://localhost:5002/tasks
Méthode : POST
Description : Crée une nouvelle tâche.

2. Mettre à Jour une Tâche
URL :http://localhost:5002/tasks/<task_id>
Méthode : PUT
Description : Met à jour une tâche existante.

3. Supprimer une Tâche
URL : http://localhost:5002/tasks/<task_id>
Méthode : DELETE
Description : Supprime une tâche existante.

4. Récupérer les Tâches d'un Utilisateur

URL: http://localhost:5002/tasks/user/<user_id>
Méthode : GET
Description : Récupère toutes les tâches assignées à un utilisateur spécifique.

5. Mettre à Jour le Statut d'une Tâche
URL : http://localhost:5002/tasks/<task_id>/status
Méthode : PATCH
Description : Met à jour uniquement le statut d'une tâche.