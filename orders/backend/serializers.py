from rest_framework import serializers

from backend.models import User,Shop


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'company', 'position')
        read_only_fields = ('id',)

class ShopSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Shop
        fields = '__all__'
