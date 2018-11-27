from database import Database
from models.blog import Blog


class Menu(object):
    def __init__(self):
        # Ask user for author name
        # Check if they've already got an account
        # If not, prompt them to create one
        self.user = input("Enter the author name; ")
        self.user_blog = None
        # underscore before method name means private method
        if self._user_has_account():
            print("Welcome back {} ".format(self.user))
        else:
            self._prompt_user_for_account()
        pass

    def _user_has_account(self):
        blog = Database.find_one('blogs', {'author': self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False
    # is not None is used to return true or false if account is there without returning the data

    def _prompt_user_for_account(self):
        title = input("Enter blog title : ")
        description = input("Enter blog description : ")
        blog = Blog(author = self.user,
                    title =title,
                    description =description)
        blog.save_to_mongo()
        self.user_blog= blog


    def run_menu(self):
        #  User read or write blogs
        read_or_write = input("Do you want to read (r) or write (w) blogs??")
        if read_or_write == 'r':
            # list blogs in db and allow user to pick one
            # display posts
            self._list_blogs()
            self._view_blog()
            pass
        elif read_or_write == 'w':
            # check if user has blogs, if do
            # prompt to write post
            # if not, prompt to create new blog
            self.user_blog.new_post()
            pass
        else:
            print("Thank you for blogging")



    def _list_blogs(self):
        blogs = Database.find(collection='blogs',
                              query={})
        for blog in blogs:
            print("ID {}, Title {}, Author: {}".format(blog['id'], blog['title'], blog['author']))

    def _view_blog(self):
        blog_to_see = input("Enter the ID of the blog you'd like to read: ")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_post()
        for post in posts:
            print("Date: {}, title: {}\n\n{}".format(post['created_date'], post['title'],post['content']))