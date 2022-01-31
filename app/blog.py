from lib2to3.pgen2.token import TILDE
from models.post import Post
import uuid
import datetime

from mydatabase import Database


class Blog(object):
    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input("Enter post title: ")
        content = input("Enter post content: ")
        date = input("Enter post date, or leave black for today (in format DDMMYY): ")
        post = Post(blog_id=self.id,
                    title=title,
                    content=content,
                    author=self.author,
                    date=datetime.datetime.strptime(date, "%d%m%Y"))
    Post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self.id)
    
    def save_to_mongo(self):
        return {
            'author': self.author,
            'title': self.title,
            'description': self.description,
            'id': self.id
        }
    
    @staticmethod
    def get_from_mongo(self):
        blog_data = Database.find_one(collection='blogs',
                                        query={'id': id})
        return blog_data
