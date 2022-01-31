import uuid
from mydatabase import Database
import datetime


class Post(object):
    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.date = date
        self.id = uuid.uuid4().hex if id is None else id
    
    def json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'date': self.date,
        }

    def save_to_mongo(self):
        Database.insert(collection='posts', data=self.json())

    @staticmethod
    def from_mongo(id):
        return Database.find_one(collection='posts', query={ 'id': id })
    #zwraca post z bazy danych

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={ 'blog_id': id})]
    #zwraca post z konkretnego bloga
