from django.shortcuts import render,get_object_or_404
from AnAPI.models import Story
from AnAPI.serializerz import StorySerializerz
from rest_framework.parsers import JSONParser
from django.http import JsonResponse, HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from AnAPI.permissions import IsCreator

# Create your views here.

class storyModelViewset(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializerz
    lookup_field = "slug"
    #authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated, IsCreator]

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)



"""
class storyViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    lookup_field = "slug"
    queryset =Story.objects.all()
    serializer_class = StorySerializerz
"""


# class storyViewSet(viewsets.ViewSet):
#     def list(self, request):
#         storiez = Story.objects.all()
#         serializered = StorySerializerz(storiez, many=True)
#         return Response(serializered.data)
    
#     def create(self, request):
#         serializered = StorySerializerz(data =request.data)
#         if serializered.is_valid():
#             serializered.save()
#             return Response(serializered.data, status=status.HTTP_201_CREATED)
#         return Response(serializered.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #Failed Try for Detail view
    # def get(self, request, slug):
    #     lookup_field = "slug"
    #     story = Story.objects.get(slug=slug)
    #     serializered = StorySerializerz(story)
    #     return Response(serializered.data)

    # def getStory(self, slug):
    #     try:
    #         return Story.objects.get(slug=slug)
    #     except Story.DoesNotExist:
    #         raise Http404
    
    # def retrieve(self, request, pk=None):
    #     lookup_field = "slug"
    #     story = Story.objects.all()
    #     thisStory = get_object_or_404(story, pk=pk)
    #     serializered = StorySerializerz(thisStory)
    #     return Response(serializered.data)


    #Failed attempt at get/retrieve
    # def retrieve(self, request, slug):
    #     lookup_field = 'slug'
    #     story = Story.objects.get(slug=slug)
    #     serializered = StorySerializerz(story)
    #     return Response(serializered.data)
    
    #Failed Try for Update view
    # def update(self, request, slug):
    #     lookup_field = "slug"
    #     story = Story.objects.get(slug=slug)
    #     serializered = StorySerializerz(data=request.data)
    #     if serializered.is_valid():
    #         serializered.save()
    #         return Response(serializered.data, status=status.HTTP_201_CREATED)
    #     return Response(serializered.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk=None):
    #      lookup_field = "slug"
    #      story = Story.objects.get(pk=pk)
    #      story.delete()
    #      return Response(status=status.HTTP_204_NO_CONTENT)



"""
class storyList(generics.ListCreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializerz

class storyDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    queryset = Story.objects.all()
    serializer_class = StorySerializerz
"""



"""
class storyList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializerz

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class storyDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializerz
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

"""

# class storyList(APIView):
#     def get(self, request):
#         storiez = Story.objects.all()
#         serializered = StorySerializerz(storiez, many=True)
#         return Response(serializered.data)
    
#     def post(self, request):
#         serializered = StorySerializerz(data=request.data)
#         if serializered.is_valid():
#             serializered.save()
#             return Response(serializered.data, status=status.HTTP_201_CREATED)
#         return Response(serializered.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class storyDetail(APIView):
#     def getStory(self, slug):
#         try:
#             return Story.objects.get(slug=slug)
#         except Story.DoesNotExist:
#             raise Http404
        
        
#     def get(self, request, slug):
#         story = self.getStory(slug)
#         serializered = StorySerializerz(story)
#         return Response(serializered.data)
        
#     def put(self, request, slug):
#         story = self.getStory(slug)
#         serializered = StorySerializerz(story, data=request.data)
#         if serializered.is_valid():
#             serializered.save()
#             return Response(serializered.data)
#         return Response(serializered.errors, status=status.HTTP_400_BAD_REQUEST)

#     # Failed PUT function attempt
#     # def PUT(self, request, slug):
#     #     story = Story.objects.get(slug=slug)
#     #     serializered = StorySerializerz(story, data=request.data)
#     #     if serializered.is_valid():
#     #         serializered.save()
#     #         return Response(serializered.data)
#     #     return Response(serializered.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, slug):
#         story = self.getStory(slug)
#         story.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    




"""
@api_view(['GET', 'POST'])
def storyList(request):
    if request.method == "GET":
        storiez = Story.objects.all()
        serializered = StorySerializerz(storiez, many=True)

        return Response(serializered.data)
    
    elif request.method == "POST":
        serializered = StorySerializerz(data = request.data)
        if serializered.is_valid():
            serializered.save()
            return Response(serializered.data, status=status.HTTP_201_CREATED)
        return Response(serializered.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def storyDetail(request, slug):
    try:
        story = Story.objects.get(slug=slug)
    except Story.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializered = StorySerializerz(story)
        return Response(serializered.data)
    
    elif request.method == 'PUT':
        serializered = StorySerializerz(story, data=request.data)
        if serializered.is_valid():
            serializered.save()
            return Response(serializered.data)
        return Response(serializered.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        story.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""



""" 
@csrf_exempt
def storyList(request):
    if request.method == "GET":
        storiez = Story.objects.all()
        serializered = StorySerializerz(storiez, many=True)

        return JsonResponse(serializered.data, safe=False)
    
    elif request.method == "POST":
        mata = JSONParser().parse(request)
        serializered = StorySerializerz(data=mata)
        if serializered.is_valid():
            serializered.save()
            return JsonResponse(serializered.data, status=201)
        return JsonResponse(serializered._errors, status=400)

@csrf_exempt
def storyDetail(request, slug):
    try:
        storiez = Story.objects.get(slug=slug)
    except Story.DoesNotExist:
        return HttpResponse(satus=404)
    
    if request.method == "GET":
        serializered = StorySerializerz(storiez)
        return JsonResponse(serializered.data)
    
    elif request.method == "PUT":
        mata = JSONParser().parse(request)
        serializered = StorySerializerz(storiez, data=mata)

        if serializered.is_valid():
            serializered.save()
            return JsonResponse(serializered.data)
        return JsonResponse(serializered._errors, status=400)
    
    elif request.method == "DELETE":
        storiez.delete()
        return HttpResponse(status=204)
"""