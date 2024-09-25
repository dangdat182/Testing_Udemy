import unittest
import sys
import os
sys.path.insert(0, 'D:/Testing_Udemy/blog')
from blog import Blog
class Test_Blog(unittest.TestCase):
    def test_create_blog(self):
        blog = Blog("Test", "Test Author")

        self.assertEqual("Test", blog.title)
        self.assertEqual("Test Author", blog.author)
        self.assertListEqual([], blog.posts)

    def test_repr(self):
        blog1 = Blog("Test", "Test Author")
        blog2 = Blog("My Day", "Rolf")

        self.assertEqual("Test by Test Author (0 posts)", blog1.__repr__())
        self.assertEqual("My Day by Rolf (0 posts)", blog2.__repr__())

    def test_multi_repr(self):
        blog1 = Blog("Test", "Test Author")
        blog1.posts = ["test", "hello"]
        self.assertEqual(blog1.__repr__(), "Test by Test Author (2 posts)")

