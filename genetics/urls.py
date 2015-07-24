from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin
from backend import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'sequences', views.OrderSequenceViewSet)


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^', include('backend.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
