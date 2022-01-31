from mydatabase import Database
from models.post import Post

Database.initialize()

post = Post("Post1 title", "Post1 content", "Post1 author")