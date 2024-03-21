from django.urls import path, include
#from AnAPI.views import storyList, storyDetail
from AnAPI.views import storyModelViewset #storyViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('story', storyModelViewset, basename="story")

#app_name = ""

urlpatterns = [
    #router
    path('', include(router.urls)),
    


    #Class Based View
    # path("story/", storyList.as_view()),
    # path("story/<slug:slug>/", storyDetail.as_view()),
    
    #Function Based View
    # path("story/", storyList),
    # path("story/<slug:slug>/", storyDetail),
]
