from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View

import django_filters
from rest_framework import routers, serializers, viewsets, filters
from rest_framework import generics, mixins

from .serializers import DvdApiSerializer
from .forms import DvdApiFilter
from .models import Dvd


class RentalRestApi(generics.ListAPIView, mixins.CreateModelMixin):
    # permission_classes = (IsAuthenticated,)
    queryset = Dvd.objects.order_by('updated')
    serializer_class = DvdApiSerializer
    filter_class = DvdApiFilter
    search_fields = ('title',)
    ordering_fields = ('title')
    filter_backends = (
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DvdDetailView(DetailView):
    template_name = 'dvd_detail.html'

    def get_object(self):
        id_ = self.kwargs.get('id')

        return get_object_or_404(Dvd, id=id_)