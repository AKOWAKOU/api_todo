RIGHT COM

# **API TODO-LIST**


# **Introduction**

Ce projet est une API de gestion de tâches développée en Flask et utilisant MongoDB comme base de données. Ce document décrit les étapes nécessaires pour configurer l'environnement de développement, exécuter l'application localement, et la dockeriser pour une utilisation en production.

PREREQUIS

* [Python 3.8+](https://www.python.org/downloads/)  
* [Pip](https://pip.pypa.io/en/stable/installation/)  
* Docker  
* Docker Compose

**Installation**

Cloner le dépôt: **git clone [git@github.com](mailto:git@github.com):AKOWAKOU/api\_todo.git**

cd api\_todo

python \-m venv venv

source venv/bin/activate  \# Sur Windows utilisez \`venv\\Scripts\\activate\`

pip install \-r requirements.txt

Configuration de la base de données

Vous pouvez exécuter MongoDB localement ou utiliser un service cloud. Pour une installation locale :

1. Téléchargez et installez [MongoDB Community Server](https://www.mongodb.com/try/download/community).  
2. Démarrez le serveur MongoDB.  
3. app.config\['MONGO\_URI'\]='mongodb://localhost:27017/  
4. flask run

Avec Postman Pour tester l'API, vous pouvez utiliser Postman. Voici quelques points de terminaison à tester :

 POST /tasks – Créer une nouvelle tâche 

PUT /tasks/tasks_id – Modifier une tâche existante 

DELETE /tasks/tasks_id – Supprimer une tâche 

 GET /tasks/user/user_id – Récupérer les tâches assignées à un utilisateur 

.PATCH /tasks/tasks_id/status – Changer le statut d'une tâche :

Création du Dockerfile


### **Création du fichier `docker-compose.yml`**

