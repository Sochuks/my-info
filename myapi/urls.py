from django.urls import path,  include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'details', views.DetailsViewSet)

# wire up our API using automatic URL routing
# Additionally we include login URL's for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]