from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView, CreateView, UpdateView, \
    DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
# Create your views here.
from .forms import PostForm

# @login_required
# def post_new(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             messages.success(request, '포스팅을 저장했습니다')
#             return redirect(post)
#     else:
#         form = PostForm()
#
#     return render(request, 'instagram/post_form.html', {
#         'form': form,
#         'post': None,
#     })


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('instagram:post_list')
    # def get_success_url(self):
    #     return reverse('instagram:post_list')


post_delete = PostDeleteView.as_view()


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        messages.success(self.request, '포스팅을 수정했습니다')
        return super().form_valid(form)


post_edit = PostUpdateView.as_view()


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        messages.success(self.request, '포스팅을 저장했습니다')
        return super().form_valid(form)


post_new = PostCreateView.as_view()

# @login_required
# def post_edit(request, pk):
#     post = get_object_or_404(Post,pk=pk)
#     if post.author != request.user:
#         messages.error(request, '작성자만 수정할 수 있습니다.')
#         return redirect(post)
#
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             post = form.save()
#             messages.success(request, '포스팅을 수정했습니다')
#             return redirect(post)
#     else:
#         form = PostForm(instance=post)
#
#     return render(request, 'instagram/post_form.html', {
#         'form': form,
#         'post': post,
#     })

# @login_required
# def post_delete(request, pk):
#     post = get_object_or_404(Post,pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         messages.success(request,'포스팅을 삭제했습니다.')
#         return redirect('instagram:post_list')
#     return render(request, 'instagram/post_confirm_delete.html', {
#         'post': post,
#     })

# post_list= ListView.as_view(model=Post, paginate_by=10)

# @login_required
# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q', '')
#     if q:
#         qs = qs.filter(message__icontains=q)
#
#     messages.info(request, 'messages 테스트')
#     # instagram/templates/instagram/post_list.html
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#         'q': q,
#     })
@method_decorator(login_required, name='dispatch')
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