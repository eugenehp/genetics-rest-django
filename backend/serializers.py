from django.contrib.auth.models import User, Group
from rest_framework import serializers
from backend.models import Order, OrderSequence

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('id','name', 'user', 'date', 'status')

class OrderSequenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderSequence
        fields = ('id','name','librarySequence','vectorSequence','upstreamSequence','downstreamSequence','order')