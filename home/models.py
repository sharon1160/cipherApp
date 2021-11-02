from django.db import models

# Create your models here.
class TextTrans(models.Model):
  key = models.TextField(blank=True)
  plain_text = models.TextField(blank=True)

class TextPlayfairForm(models.Model):
  key = models.TextField(blank=True)
  text_cipher = models.TextField(blank=True)

class TextCesarForm(models.Model):
  key = models.TextField(blank=True)
  text_cipher = models.TextField(blank=True)


