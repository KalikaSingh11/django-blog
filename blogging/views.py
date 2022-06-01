from django.shortcuts import render
from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import Http404


# Create your views here..
from django.http import HttpResponse, HttpResponseRedirect, Http404


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")


class PostListView(ListView):
    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date")
    template_name = "list.html"


class PostDetailView(DetailView):
    template_name = "blogging/detail.html"
    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date")

    def post(self, request, *args, **kwargs):
        try:
            post = self.queryset.get(post_id=self.kwargs.get("post_id"))

        except Post.DoesNotExist:
            raise Http404
        context = {"object": post}
        return render(request, "blogging/detail.html", context)
