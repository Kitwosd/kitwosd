from app.models import Blog, Category

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)

# def blog_links(request):
#     blogs= Blog.objects.all()
#     return dict(blogs=blogs)

