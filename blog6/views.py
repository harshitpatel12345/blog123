# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
from .models import Post
from .serializer import PostSerializer
from rest_framework import generics
# Create your views here


# class CreatePostView(APIView):
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreatePostView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
