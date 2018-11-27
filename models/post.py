import uuid
import datetime
from database import Database


class Post(object):
    def __init__(self, blog_id, title, content, author, created_date=datetime.datetime.utcnow(), id=None):
        # automatically generated date and id
        # date is +00 timezone so easy to convert
        self.blog_id = blog_id  # id of the blogger
        self.title = title
        self.content = content
        self.author = author
        self.created_date = created_date
        self.id = uuid.uuid4().hex if id is None else id  # generate id of each post using uuid if id is not specified

# saving data to mongodb
    def save_to_mongo(self):
        Database.insert(collection='students',
                        data=self.json())

    def json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }

    @staticmethod
    def from_mongo(id):
        # Post.from_mongo('123')
        return Database.find_one(collection='students', query={'id': id})
        # returns only one record so no need list comprehension

    # returning all posts belonging to specific blog
    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='students', query={'blog_id': id})]
        # this will return a cursor because more than one posts, so have to use list comprehension