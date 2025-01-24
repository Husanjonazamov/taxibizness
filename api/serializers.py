from rest_framework import serializers
from category.models import Users, category




class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        
        
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'