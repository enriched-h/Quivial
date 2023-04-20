from django.contrib import admin
from .models import Question, Choice, AttemptedQuestion


admin.site.register(Question) 
admin.site.register(Choice) 
admin.site.register(AttemptedQuestion) 

