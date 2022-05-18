# add these imports
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from blogging.models import Post

# and this view
def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    template = loader.get_template('blogging/list.html')
    context = {'posts': posts}
    body = template.render(context)
    return HttpResponse(body, content_type="text/html")