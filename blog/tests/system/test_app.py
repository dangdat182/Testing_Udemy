import pytest
import unittest
import os
import sys
sys.path.insert(0, "D:/Testing_Udemy/Testing_Udemy/blog")
import app
from blog import Blog
from unittest.mock import patch

MENU_PROMPT = "Enter 'c' to create a blog, 'l' to list blogs, 'r' to read one, 'p' to  create a post, 'q' to quit"

@pytest.fixture
def sample_blog():
    blog = Blog("Test", "Test Author")
    app.blogs = {"Test": blog}

@patch('builtins.input')
def test_menu(mocked_input):
    mocked_input.return_value= 'q'
    app.menu() 
  
    mocked_input.assert_called_with(app.MENU_PROMPT)
  

@patch('builtins.input')
def test_menu_calls_print_blogs(mocked_input):
    mocked_input.side_effect = ('c', 'Test Create Blog', 'Test Title', 'q')
    app.menu()
    
    assert app.blogs['Test Create Blog'] is not None
    
      
@patch('builtins.print')
def test_print_blogs(mocked_print, sample_blog):
    app.print_blogs()
    
    mocked_print.assert_called_once_with('- Test by Test Author (0 posts)')    
    
@patch('builtins.input')
def test_ask_create_blog(mocked_input, sample_blog):
    mocked_input.side_effect = ('Test', 'Author')
    
    app.ask_create_blog() 
    assert app.blogs.get('Test') is not None
    assert app.blogs['Test'].author == 'Author'
    
@patch('app.print_posts')    
@patch('builtins.input')
def test_ask_read_blog(mocked_input, mocked_print_posts, sample_blog):
    
    mocked_input.return_value = 'Test'
    
    app.ask_read_blog()
    
    mocked_print_posts.assert_called_once_with(app.blogs['Test'])
    
@patch('app.print_post')
def test_print_posts(mocked_print_posts, sample_blog):

    app.blogs['Test'].create_post('Post title', 'Post content')

    
    app.print_posts(app.blogs['Test'])
    
    mocked_print_posts.assert_called_once_with(app.blogs['Test'].posts[0])

@patch('builtins.print')   
def test_print_post(mocked_print, sample_blog):
    app.blogs['Test'].create_post('Post title', 'Post content')

    
    app.print_post(app.blogs['Test'].posts[0])
    
    assert mocked_print.call_args == (('Post title Post content',),)
   
@patch('builtins.input')    
def test_ask_create_post(mocked_input, sample_blog):
    mocked_input.side_effect = ('Test', 'Test Title', 'Test Content')
    
    app.ask_create_post()
    
    assert app.blogs['Test'].posts[0].title == 'Test Title'
    assert app.blogs['Test'].posts[0].content == 'Test Content'
    
    