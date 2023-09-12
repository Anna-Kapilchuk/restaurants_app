from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from restaurants_app.filterset.address import AddressFilterSet
from restaurants_app.models import Address
from restaurants_app.serializer.address import AddressSerializer


class AddressViewSet(ModelViewSet):

    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    filterset_class = AddressFilterSet

    def get_permissions(self):

        if self.action in ('create', 'update', 'destroy'):
            return [IsAdminUser()]

        else:
            return []
