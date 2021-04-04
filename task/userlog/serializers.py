from rest_framework import serializers
#from .models import Student
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, min_length=5)
    username = serializers.CharField(max_length=50, min_length=5)
    password = serializers.CharField(max_length=150, write_only=True)


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        if User.objects.filters(email=email).exista():
            raise serializers.validationError({'email':('email already exists')})
        if User.objects.filters(username=username).exista():
            raise serializers.validationError({'username':('username already exists')})
        return super().validate(args)

    def create(self,validated_data):
        return User.objects.create_user(validated_data)
