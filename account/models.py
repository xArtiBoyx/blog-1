# from django.db import models
# from django.conf import settings
#
#
# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE),
#     date_of_birth = models.DateField(blank=True, null=True),
#     about_me = models.TextField()
#
#     def __str__(self):
#         return f'Профиль пользователя {self.user.last_name} {self.user.first_name}'
