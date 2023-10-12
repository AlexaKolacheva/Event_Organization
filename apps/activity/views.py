from rest_framework import viewsets

from . models import Comments, Review
from .serializers import CommentsSerializer, ReviewSerializer


class CommentsViewSet(viewsets.ModelViewSet):
     queryset = Comments.objects.all()
     serializer_class = CommentsSerializer



class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer



