import pytest
import os
import sys
sys.path.insert(0, "D:/Testing_Udemy/blog")
import app
from blog import Blog
from unittest.mock import patch

@patch('builtins.print')
def test_print_blog(mocked_print):
    blog = Blog("Test", "Test Author")
    app.blogs = {"Test": blog}
    app.print_blogs()
    
    mocked_print.assert_called_with('- Test by Test Author (0 post)')