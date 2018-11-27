from database import Database
from models.blog import Blog
from models.post import Post

Database.initialize()

blog = Blog(author="NImaz",
            title="Sample title",
            description="Sample Description")
blog.new_post()
blog.save_to_mongo()
from_database = Blog.from_mongo(blog.id)

print(blog.get_post())