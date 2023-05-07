from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    # Add any other fields you want to include for your users
    class Meta:
        app_label = 'user_management'


class Session(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    session_id = models.CharField(max_length=255)

    class Meta:
        app_label = 'user_management'
