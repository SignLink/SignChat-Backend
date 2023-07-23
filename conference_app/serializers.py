from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

    def validate_password(self, value):
        return make_password(value)
    
    def validate_email(self, value):
        if Account.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email address already exists.")
        return value
    
    def validate(self, attrs):
        return attrs

        
class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Account.objects.all())]
    )
    

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Account
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password':'Password fields didnt match'})

        return attrs

    def create(self, validated_data):
        account = Account(
            email=validated_data['email'],
            username = validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],  
            sex=validated_data['sex'],  
            country=validated_data['country'],  
            state=validated_data['state'],  
        )
        account.set_password(validated_data['password'])
        account.save()
        
        return account