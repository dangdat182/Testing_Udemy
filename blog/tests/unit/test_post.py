import unittest
import os
import sys
sys.path.insert(0, 'D:/Testing_Udemy/blog')
from post import Post
 
class Test_post(unittest.TestCase):
    def test_create_post(self):
        p = Post("Test", "Test Content")
        self.assertEqual("Test", p.title)
        self.assertEqual("Test Content", p.content)
 
    def test_json(self):
        p = Post("Test", "Test Content")
        
        expected = {"title": "Test", "content": "Test Content"}
        
        json = p.json()
        
        self.assertDictEqual(expected, json)