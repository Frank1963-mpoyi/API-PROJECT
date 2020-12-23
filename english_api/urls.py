
from django.urls import path

# 1st method
#from .views import WordList

# 2nd method
#from . import generic_views

# 3rd method
from rest_framework import routers
#from . import viewsets

# 4th 
from . import mixins


router = routers.DefaultRouter()
#router.register('english_api', viewsets.WordViewSet)

# 4th for mixins
router.register('english_api', mixins.WordViewSet)





urlpatterns = [
    
    # 1st
    #path('words/', WordList.as_view(), name="word_list" ),
    
    # 2nd
    #path('', generic_views.ListCreateWords.as_view(), name='word_list' ),
    #path('<int:pk>', generic_views.RetriveUpdateDestroyWord.as_view(), name='word_detail')

    #3rd
    

]

urlpatterns += router.urls