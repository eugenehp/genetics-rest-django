from rest_framework import viewsets, mixins
from django.contrib.auth.models import User, Group
from backend.serializers import UserSerializer, GroupSerializer, OrderSerializer, OrderSequenceSerializer
from backend.models import Order, OrderSequence


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderSequenceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows order order sequences to be viewed or edited.
    """
    queryset = OrderSequence.objects.all()
    serializer_class = OrderSequenceSerializer