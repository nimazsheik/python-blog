from database import Database
from models.post import Post

Database.initialize()

# post = Post(blog_id="123",
#            title="Another great post",
#            content="Some content",
#            author="Nimaz")

# post.save_to_mongo()

## post= Post.from_mongo("97939165e8784a53b400e2fa6a959521")
## print(post)
posts = Post.from_blog('123')

for post in posts:
    print(post)