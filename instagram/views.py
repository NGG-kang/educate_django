from django.http import HttpResponse, Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

# post_list= ListView.as_view(model=Post)
def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(message__icontains=q)
    # instagram/templates/instagram/post_list.html
    return render(request, 'instagram/post_list.html', {
        'post_list': qs,
        'q': q,
    })

# def post_detail(requset: HttpResponse, pk: int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#     return render(requset, 'instagram/post_detail.html', {
#         'post': post
#     })

post_detail = DetailView.as_view(model=Post)

def archives_year(request, year):
    return HttpResponse(f"{year} archives")