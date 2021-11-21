from typing import ContextManager
from django.core import paginator
from django.shortcuts import get_object_or_404, redirect, render
from app.models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.mail import send_mail
# from django.http import HttpResponse
# Create your views here.
def home(request):
    data = Home.objects.all()
    team = Team.objects.all()
    blog = Blog.objects.all()
    project = Project.objects.all()
    testimonial = Testimonials.objects.all()
    print('data:',data)
    context={
        "object":data,
        'team':team,
        'blog':blog,
        'project':project,
        'testimonial':testimonial,
    }
    return render(request, 'kitwosd/index.html',context)

def contact(request):
    if request.method =="POST":
        name = request.POST['fullName']
        email = request.POST['emailAddress']
        subject = request.POST['subject']
        comment = request.POST['comment']
        #send email
        # send_mail(
        #     subject,#subject
        #     comment,#message
        #     email,#from_mail
        #     ['bhishan51@gmail.com'],#to_Email
        # )
        contact_obj = Contact.objects.create(
            name =name,
            email= email,
            subject = subject,
            comments = comment
        ) 
        contact_obj.save()
    return render(request, 'kitwosd/contact.html')

def service(request):
    return render(request, 'kitwosd/service.html')

def portfolio(request, category_slug=None):
    categories = None
    projects = None
    print('category_slug',category_slug)

    if category_slug != None:
        categories = get_object_or_404(Category, category_slug=category_slug)
        projects = Project.objects.filter(category= categories)
        paginator = Paginator(projects,3)
        page = request.GET.get('page')
        paged_project = paginator.get_page(page)
    # projects = Project.objects.filter(category=categories)
    else:
        projects = Project.objects.all()
        paginator = Paginator(projects,3)
        page = request.GET.get('page')
        paged_project = paginator.get_page(page)

    context={
        'projects':paged_project,
        # 'single_project':project
    }
    return render(request, 'kitwosd/portfolio.html',context)

def package(request):
    package = Package.objects.all()

    context = {
        'package':package
    }
    return render(request, 'kitwosd/package.html',context)

def team(request):
    team = Team.objects.all()
    print('team:',team)
    context={
        'team':team
    }
    return render(request, 'kitwosd/teammember.html',context)

def product(request):
    return render(request, 'kitwosd/portfolio.html')

def faq(request):
    faq = Faq.objects.all()
    context = {
        'faq_data':faq
    }
    return render(request, 'kitwosd/faq.html',context)

def aboutus(request):
    return render(request, 'kitwosd/aboutus.html')

def terms_and_condition(request):
    return render(request, 'kitwosd/term_condition.html')

def privacy_policy(request):
    return render(request, 'kitwosd/privacy.html')

def blog(request):
    # blog=None
    # if blog_slug!=None:
        # blogs = get_object_or_404(Blog, blog_slug=blog_slug)
        # blog = Blog.objects.filter(slug=blogs)
        # print('blogs',blogs)
    # else:
    blog = Blog.objects.all()
    paginator = Paginator(blog,3)
    page = request.GET.get('page')
    paged_project = paginator.get_page(page)
    context={
        'blogs':paged_project
    }
    return render(request, 'kitwosd/blogs.html',context)

def blog_detail(request,blog_slug=None):
    blog=None
    print('blog_slug',blog_slug)
    if blog_slug!=None:
        blog = get_object_or_404(Blog, blog_slug=blog_slug)
    else:
        blog=Blog.objects.all()

    context={
        'blog':blog
    }
    return render(request, 'kitwosd/blog-read.html', context)

def quote(request):
    if request.method == 'POST':
        name = request.POST['fullName']
        email = request.POST['emailAddress']
        number = request.POST['phoneNumber']
        country = request.POST['countryName']
        budget = 10000     
        whatsappNumber = request.POST['whatsappNumber']
        field = "Web Development"
        description = request.POST['details']
        file = request.FILES['File']
        print('quote name:',name)
        quote_obj = Quote.objects.create(
            full_name= name,
            email= email,
            contact_number= number,
            country= country,
            whatsapp_number = whatsappNumber,
            budget = budget,
            field = field,
            description= description,
            document = file
        )
        quote_obj.save()
        

    return render(request, 'kitwosd/quote.html')

def gallery(request):
    image = Gallery.objects.all()
    context = {
        'image':image
    }
    return render(request, 'kitwosd/gallery.html', context)


def career(request):
    data = Careers.objects.all()
    context = {
        'data':data
    }
    return render(request, 'kitwosd/career.html',context)

def login(request):
    return render(request, 'kitwosd/login.html')

def package_order(request, pk=None):
    if request.method == 'POST':
        # if request.method =="POST":
        name = request.POST['fullName']
        email = request.POST['emailAddress']
        number = request.POST['phone_number']
        country = request.POST['country']
        city = request.POST['city']
        file = request.FILES['packageFile']
        print('name',name)
        # file = request.POST['country']
        # package_obj = package_order.objects.create(
        package_obj = Package_order.objects.create(
        # id=pk,
        package_field = "Web Development",
        name = name,
        email = email,
        number = number,
        country = country,
        city = city,
        document = file
        )
        package_obj.save()
        return redirect('home')
    # else:
    #     if pk!=None:
    #         package= Package.objects.get(id=pk)
    #         context={
    #         'package':package
    #     }
    return render(request,'kitwosd/package_order.html')

def subscribe(request):
    if request.method =="POST":
        email_address = request.POST['subscribeMail']
        subscribe_obj = Subscribe.objects.create(
            email_address = email_address
        )
        subscribe_obj.save()
        return redirect('home')