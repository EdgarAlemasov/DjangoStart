from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOrReadOnly
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    def get_queryset(self):
        queryset = Advertisement.objects.filter(status='OPEN')
        creator = self.request.query_params.get('creator', None)
        if creator:
            queryset_closed = Advertisement.objects.filter(status='CLOSED')
            queryset = queryset_closed
        return queryset

    # queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter = [AdvertisementFilter]
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in 'create':
            return [IsAuthenticated()]
        elif self.action == 'update':
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return [IsOwnerOrReadOnly()]
