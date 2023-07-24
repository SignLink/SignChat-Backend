from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fiellds):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fiellds)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fiellds):
#         extra_fiellds.setdefault('is_staff', True)
#         extra_fiellds.setdefault('is_superuser', True)

#         if extra_fiellds.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fiellds.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_staff=True.')

#         return self.create_user(email, password, **extra_fiellds)

class UserManager(BaseUserManager):
    def create_user(self, email:str, password:str, **other_fields):
        if not email:
            raise ValueError('User must have email')
        if not password:
            raise ValueError('User must have password')
        
        
        
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            **other_fields
        )
        user.set_password(password)
        user.save()
        return user

    
    def create_superuser(self,  email:str, password:str, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True'
            )
        if other_fields.get('is_active') is not True:
            raise ValueError(
                'Superuser must be assigned to is_active=True'
            )
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True'
            )

        user = self.create_user(
            email=email,
            **other_fields
        )

        return user
    
class User(AbstractUser):
    email = models.EmailField(unique=True)

    
    
    # The 'email' field will be used for authenticaton.
    USERNAME_FIELD = 'email'
    # other required fields  for the Account model
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)


    def __str__(self) -> str:
        return self.first_name
    

