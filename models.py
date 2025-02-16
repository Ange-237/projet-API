from django.db import models

class translate(models.Model):
    source_text = models.TextField()
    translated_text = models.TextField()
    target_language = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    # https://openrouter.ai/api/v1

# Create your models here.
