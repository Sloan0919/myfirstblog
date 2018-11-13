from django.shortcuts import render
from blog.models import Blog
import markdown
# Create your views here.

def index(request):
    blogs = Blog.objects.all()
    # blog_content=markdown.markdown(blog.content)
    return render(request,"Blog.html",{"blogs":blogs})
