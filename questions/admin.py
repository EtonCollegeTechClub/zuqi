from django.contrib import admin
from nested_inlines.admin import NestedModelAdmin, NestedStackedInline, NestedTabularInline
from questions.models import *


class ChoiceInLine(NestedTabularInline):
  model = Choice
  extra = 2

class QuestionInLine(NestedStackedInline):
  model = Question
  extra = 1
  inlines = [ChoiceInLine, ]

class QuizAdmin(NestedModelAdmin):
  inlines = [QuestionInLine, ]

admin.site.register(Quiz, QuizAdmin)