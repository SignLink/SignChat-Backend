from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from conference_app.models import UserProfile



class UserProfileSerializer(RegisterSerializer):
    username = None
    first_name = serializers.CharField(max_length =50)
    last_name = serializers.CharField(max_length =50)
    sex = serializers.CharField(max_length =20)
    country = serializers.CharField(max_length =20)
    state = serializers.CharField(max_length =20)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()

        extra_data = {

            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'sex': self.validated_data.get('sex', ''),
            'country': self.validated_data.get('country', ''),
            'state': self.validated_data.get('state', ''),
            
        }
        data.update(extra_data)

        return data
    

    def save(self, request):
        user = super().save(request)

        user.username = user.email

        user.save()

        userprofile = UserProfile(user=user, first_name=self.cleaned_data.get(
            'first_name'), last_name=self.cleaned_data.get('last_name'),
            sex=self.cleaned_data.get('sex'),
            country=self.cleaned_data.get('country'),
            state=self.cleaned_data.get('state'),
            
            )

        userprofile.save()

        return user