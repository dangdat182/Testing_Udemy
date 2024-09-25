blogs = dict()

def menu():
    print_blogs
    selection = input("Enter 'c' to create a blog, 'l' to list blogs, 'r' to read one, 'p' to  create a post, 'q' to quit")
    
def print_blogs():
    for key, blog in blogs.items():
        print(f"- {blog}")