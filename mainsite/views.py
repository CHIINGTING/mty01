from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from datetime import datetime
from .models import Post

import templates


# Create your views here.

def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())

    # posts = Post.objects.all() #資料庫全部撈出 post_list =list() for count, post in enumerate(posts): post_list.append(
    # "No.{} ".format(str(count))+"<font color=red>"+str(post)+"</font>"+str(post.pub_date)+"<br>") post_list.append(
    # "<small>"+str(post.body)+"</small><br><br>")
    return HttpResponse(html)


def showPost(request, slug):
    template = get_template('post.html')
    try:
        posts = Post.objects.get(slug=slug)
        if posts is not None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')
