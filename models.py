from pymongo import MongoClient
from bson.objectid import ObjectId
from config import Config
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class Database:
    def __init__(self):
        try:
            self.client = MongoClient(Config.MONGO_URI)
            self.db = self.client.todo
            logger.info("Connexion à la base de données MongoDB réussie.")
        except errors.ConnectionFailure as e:
            logger.error(f"Échec de la connexion à MongoDB : {str(e)}")
            
    def create_user(self, name, email):
        user = {
            "name": name,
            "email": email
        }
        return self.db.users.insert_one(user).inserted_id

    def create_task(self, title, description, assigned_to, status, due_date):
        task = {
            "title": title,
            "description": description,
            "assigned_to": assigned_to,
            "status": status,
            "due_date": datetime.strptime(due_date, "%Y-%m-%d")
        }
        return self.db.tasks.insert_one(task).inserted_id
    
    @property
    def tasks(self):
        return self.db.tasks
    
    def get_users(self):
        return list(self.db.users.find())

    def get_tasks(self):
        return self.db.tasks

    def get_tasks_by_user(self, user_id):
        return list(self.db.tasks.find({"assigned_to": ObjectId(user_id)}))

    