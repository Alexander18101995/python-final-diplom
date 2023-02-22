from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Shop
from .serializers import ShopSerializer


class ShopView(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [IsAuthenticated]

    def permorm_create(self,serializer):
        serializer.save(user=self.request.user)

