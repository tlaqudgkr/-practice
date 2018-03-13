from django.db import models

# Create your models here.
class GamePlay(models.Model):
    LEFT = 'LT'
    RIGHT = 'RT'
    LEFTRIGHT_CHOICES = (
        (LEFT, '왼쪽'),
        (RIGHT, '오른쪽')
    )
    leftright = models.CharField(max_length=2, choices=LEFTRIGHT_CHOICES)
    usr = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.leftright