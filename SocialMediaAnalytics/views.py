from rest_framework import generics
from rest_framework.response import Response
from .models import SocialMediaPost
from .serializers import SocialMediaPostSerializer


class SocialMediaPostCreateView(generics.CreateAPIView):
    queryset = SocialMediaPost.objects.all()
    serializer_class = SocialMediaPostSerializer


class SocialMediaPostAnalysisView(generics.RetrieveAPIView):
    queryset = SocialMediaPost.objects.all()
    serializer_class = SocialMediaPostSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        content = instance.content
        word_count = len(content.split())
        average_word_length = sum(len(word) for word in content.split()) / word_count

        analysis_data = {
            'word_count': word_count,
            'average_word_length': average_word_length
        }
        return Response(analysis_data)
