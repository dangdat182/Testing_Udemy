MENU_PROMPT = "Enter 'c' to create a blog, 'l' to list blogs, 'r' to read one, 'p' to  create a post, 'q' to quit"

import os
import sys
sys.path.insert(0, "D:/Testing_Udemy/Testing_Udemy/blog")
from blog import Blog
from post import Post

blogs = dict()
def menu():
    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post() 
        selection = input(MENU_PROMPT)  
    
def print_blogs():
    for key, blog in blogs.items():
        print(f"- {blog}")
        
def ask_create_blog():
    title = input('Enter your blog title: ')
    author = input('Enter your name: ')
    
    blogs[title] = Blog(title, author)

def ask_read_blog():
    title = input('Enter the blog title you want to read')
    print_posts(blogs[title])
    
def print_posts(blog):
    for post in blog.posts:
        print_post(post)
       
def print_post(post):
    print(f'{post.title} {post.content}')        

def ask_create_post():
    blog_name = input('Enter the blog title you want to write a post in: ')
    title = input('Enter your post title: ')
    content = input('Enter your post content')
    
    blogs[blog_name].create_post(title, content)