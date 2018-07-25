
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from . models import TestModel
from . serializers import TestModelSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from post.models import Post
# Create your views here.


class TestView(ListAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer


class LikedBool(ListAPIView):
    pass


@api_view(['POST'])
def likedboolapi(request):
    if request.method == 'POST':
        post_id = int(request.POST.get("object_id"))
        userprofile = request.user.userprofile
        post = Post.objects.get(id=post_id)

    return Response({"data": "data"})
