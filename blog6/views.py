from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Category
from .serializer import PostSerializer, CategorySerializer
# from rest_framework import generics
# Create your views here


class CreatePostView(APIView):
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CreatePostView(generics.CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class UpdatePostView(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class ListPostView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class DeletePostView(generics.DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class CreateCategoryView(generics.CreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


# class UpdateCategoryView(generics.UpdateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


# class ListCategoryView(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


# class DeleteCategoryView(generics.DestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


class ListPostView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeletePostView(APIView):
    def delete(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        post.delete() 
        return Response({"message": "Post deleted successfully"}, status=status.HTTP_204_NO_CONTENT) 


class UpdatePostView(APIView):
    def put(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PostSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
