import unittest
import sys
import os
sys.path.insert(0, 'D:/Testing_Udemy/blog')
from blog import Blog
class Test_blog(unittest.TestCase):
    def test_create_post(self):
        blog = Blog("Test", "Test Author")
        blog.create_post("First", "Hello")

        self.assertEqual(len(blog.posts), 1)
        self.assertEqual(blog.posts[0].title, "First")
        self.assertEqual(blog.posts[0].content, "Hello")

    def test_json(self):
        blog = Blog("Test", "Test Author")
        blog.create_post("First", "Hello")
        json = blog.json()
        expected = {"title": "Test", "author" : "Test Author", "posts": [{"title": "First", "content": "Hello"}]}

        self.assertDictEqual(json, expected)

    def test_json_nopost(self):
        blog = Blog("Test", "Test Author")
        json = blog.json()
        expected = {"title": "Test", "author": "Test Author", "posts": []}

        self.assertEqual(expected, json)

if __name__ == "__main__":
    unittest.main()