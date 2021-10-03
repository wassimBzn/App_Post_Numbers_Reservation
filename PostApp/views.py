from django.http import HttpResponse
from .models import *
from django.template import loader


def index(request):
    post_Currect_number = Post.objects.all()
    template = loader.get_template('index.html')
    context = {
        'post_Currect_number': post_Currect_number,
    }
    return HttpResponse(template.render(context, request))

def detail(request, Post_id):
    return HttpResponse("You're looking at post id %s." % Post_id)

def results(request, Post_id):
    post = Post.objects.get(id=Post_id)
    response = "You're looking at the current number in the post %s."
    return HttpResponse(response % post.Post_current_Number)
    return HttpResponse(template.render(context, request))

def vote(request, Post_id):
    post = Post.objects.get(id=Post_id)
    response ="You're looking for postal_code %s."
    return HttpResponse(response % post.Postal_code)


