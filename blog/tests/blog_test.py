import unittest
from blog.models import User, Post
from blog import db


class PostModelTest(unittest.TestCase):

    def setUp(self):
        self.user_Blair = User(
            username="BLAIRCARSON", password="1234567", email="engineervinceblair@gmail.com")
        self.new_post = Post(
            title="code", body="coding rocks", user_id=self.user_Blair.id)

    def tearDown(self):
        Post.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post, Post))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_post.title, 'Coding ')
        self.assertEquals(self.new_post.body, "coding is tedious but enjoyable")
        self.assertEquals(self.new_post.user_id, self.user_abdi.id)

    def test_save_blog(self):
        self.new_post.save_post()
        self.assertTrue(len(Post.query.all()) > 0)

    def test_get_posts(self):

        self.new_post.save_blog()
        posts = Post.get_posts()
        self.assertTrue(len(posts) == 1