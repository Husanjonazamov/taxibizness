from category.models import Users, category
from .serializers import UserSerializers, CategorySerializers
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView



class UserView(ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializers


class UserGetView(RetrieveAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializers
    lookup_field = 'user_id'  


class CategoryView(ListAPIView):
    queryset = category.objects.all()
    serializer_class = CategorySerializers
