from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password'] #only write required fields
        extra_kwargs = {
            'password': {'write_only': True} #password encrypted not shown to everyone
        }
    def create(self, validated_data):  #override default create function
        password = validated_data.pop('password', None) #extracted password
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password) #set_password is inbuilt
        instance.save() #password will be hashed
        return instance