from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, PostComment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . form import CreatePost, UpdatePost
from django.urls import reverse_lazy
from core.models import UserProfile
from django.http import JsonResponse


class HomeView(ListView):
    model = Post
    template_name = 'post/home.html'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data()
        object_list = context['object_list']
        object_cmd_obj = {}
        object_like_obj = {}

        for object in object_list:
            object_cmd_obj[object.slug] = {'post_comment': object.postcomment_set.all(),
                                           'post_userprofile': object.userprofile,
                                           'post_like': object.like_set.all()}
            object_like_obj[object.slug] = {'post_like': object.like_set.all()}
            context['comment'] = object_cmd_obj
            context['like'] = object_like_obj
            context.update(kwargs)
        return context


class CreatePost(CreateView):
    model = Post
    template_name = 'post/create_post.html'
    success_url = '/'
    form_class = CreatePost

    # def __init__(self, * args, **kwargs):
    #     super(Createpost, self).__init__(*args, **kwargs)
    #     self.initial['userprofile'] = UserProfile.objects.get(pk=2)


class UpdatePost(UpdateView):
    model = Post
    form_class = UpdatePost
    success_url = '/home'
    template_name = 'post/update_post.html'


class ListPost(ListView):
    model = Post
    template_name = 'post/list_post.html'

    def get_queryset(self):
        return Post.objects.filter(userprofile__user=self.request.user)


class DetailPostView(DetailView):
    model = Post
    template_name = 'post/detailpostview.html'
    context_object_name = 'detail_post'


class DeletePostView(DeleteView):
    model = Post
    success_url = reverse_lazy('post:listpost')

    def get(self, *args, **kwargs):
        return self.post(self, *args, **kwargs)


def post_comment_post(request):
    if request.method == "POST":
        if request.POST.get("comment") and request.POST.get("object_id"):
            comment_text = request.POST.get("comment")
            object_id = int(request.POST.get("object_id"))
            comment_post_object = Post.objects.get(id=object_id)
            to_be_add_comment = PostComment.objects.create(
                post_comment=comment_text,
                userprofile=request.user.userprofile)
            to_be_add_comment.save()
            comment_post_object.postcomment_set.add(to_be_add_comment)
            data = {"true": "ture"}
        else:
            data = "ture"
    return JsonResponse(data)
