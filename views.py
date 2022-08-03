from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is a boy view which is created by home")

def paths(request):
    # Displays paths of all the blogposts inside the django website
    # fetch all the slugs from the blog post table
    context = {
        'heading': "django tutorial 1",
        'content': "this is the best django tutorial on youtube"
    }
    return HttpResponse("This is a path view which is created by home")
