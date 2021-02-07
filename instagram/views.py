from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView
from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.


# post_list= ListView.as_view(model=Post, paginate_by=10)
# @login_required
# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q', '')
#     if q:
#         qs = qs.filter(message__icontains=q)
#     # instagram/templates/instagram/post_list.html
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#         'q': q,
#     })
# @method_decorator(login_required, name='dispatch')
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 10

post_list = PostListView.as_view()
# def post_detail(request, pk):
# def post_detail(requset: HttpResponse, pk: int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#     return render(requset, 'instagram/post_detail.html', {
#         'post': post,
#         'object': post
#     })

# post_detail = DetailView.as_view(
#     model=Post,
#     queryset=Post.objects.filter(is_public=True)
# )
class PostDetailView(DetailView):
    model = Post
    # queryset = Post.objects.filter(is_public=True)
    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)
        return qs

# def archives_year(request, year):
#     return HttpResponse(f"{year} archives")

post_archive = ArchiveIndexView.as_view(model=Post, date_field='created_at', paginate_by=10)

post_archive_year = YearArchiveView.as_view(model=Post, date_field='created_at', make_object_list=True)