import os
import json
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
DB_NAME = os.getenv('MONGO_DB_NAME', 'cortex_lmh')

class Database:
    def __init__(self):
        self.use_mongo = False
        if MONGO_URI:
            try:
                self.client = MongoClient(MONGO_URI)

                self.client.admin.command('ping')
                self.db = self.client[DB_NAME]
                self.reports = self.db.reports
                self.users = self.db.users
                self.use_mongo = True
                print("Using MongoDB Atlas for storage.")
            except Exception as e:
                print(f"Error connecting to MongoDB: {e}. Falling back to local JSON files.")
        
        if not self.use_mongo:
            print("Using local JSON files for storage.")
            self.REPORTS_FILE = 'reports.json'
            self.USERS_FILE = 'users.json'
            self._init_local_files()

    def _init_local_files(self):
        for file in [self.REPORTS_FILE, self.USERS_FILE]:
            if not os.path.exists(file):
                with open(file, 'w') as f:
                    json.dump([], f)


    def get_all_reports(self):
        if self.use_mongo:
            return list(self.reports.find({}, {'_id': 0}))
        else:
            try:
                with open(self.REPORTS_FILE, 'r') as f:
                    return json.load(f)
            except:
                return []

    def save_report(self, report_data):
        if self.use_mongo:
            self.reports.insert_one(report_data.copy())
            return True
        else:
            try:
                reports = self.get_all_reports()
                reports.append(report_data)
                with open(self.REPORTS_FILE, 'w') as f:
                    json.dump(reports, f, indent=4)
                return True
            except Exception as e:
                print(f"Error saving report: {e}")
                return False

    def get_report_by_id(self, report_id):
        if self.use_mongo:
            return self.reports.find_one({"id": report_id}, {'_id': 0})
        else:
            reports = self.get_all_reports()
            return next((r for r in reports if r.get('id') == report_id), None)


    def get_all_users(self):
        if self.use_mongo:
            return list(self.users.find({}, {'_id': 0}))
        else:
            try:
                with open(self.USERS_FILE, 'r') as f:
                    return json.load(f)
            except:
                return []

    def save_user(self, user_data):
        if self.use_mongo:

            self.users.update_one(
                {"email": user_data.get('email')},
                {"$set": user_data},
                upsert=True
            )
            return True
        else:
            try:
                users = self.get_all_users()

                existing_index = next((i for i, u in enumerate(users) if u.get('email') == user_data.get('email')), None)
                if existing_index is not None:
                    users[existing_index] = user_data
                else:
                    users.append(user_data)
                
                with open(self.USERS_FILE, 'w') as f:
                    json.dump(users, f, indent=4)
                return True
            except Exception as e:
                print(f"Error saving user: {e}")
                return False

    def get_user_by_email(self, email):
        if self.use_mongo:
            return self.users.find_one({"email": email}, {'_id': 0})
        else:
            users = self.get_all_users()
            return next((u for u in users if u.get('email') == email), None)

db = Database()
