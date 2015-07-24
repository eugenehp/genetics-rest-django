import uuid
from django.contrib.auth.models import User
from django.db import models

class Order(models.Model):
    RECEIVED = 'Received'
    INPRGORESS = 'In Progress'
    COMPLETED = 'Completed'
    SHIPPED = 'Shipped'
    STATUS_CHOICES = (
        (RECEIVED, 'Received'),
        (INPRGORESS, 'In Progress'),
        (COMPLETED, 'Completed'),
        (SHIPPED, 'Shipped'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='+')
    date = models.DateTimeField(auto_now_add=False)
    status = models.CharField(max_length=20,
                                      choices=STATUS_CHOICES,
                                      default=RECEIVED)

    class Meta:
        ordering = ('created',)

class OrderSequence(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    librarySequence = models.TextField()
    vectorSequence = models.TextField()
    upstreamSequence = models.TextField()
    downstreamSequence = models.TextField()
    order = models.ForeignKey(Order,related_name='sequence')
    # , related_name='+'

    class Meta:
        ordering = ('created',)