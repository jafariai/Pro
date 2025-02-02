from django.contrib import admin
from .models import (
    User, Staff, Exercise, Coach, ProgramRequest, Membership, Approval, Blog, Comment,
    SportProgram, Food, NutrientProgram
)

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('staff_id', 'name', 'email')
    search_fields = ('name', 'email')
    list_filter = ('email',)

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('exercise_id', 'exercise_name', 'repetitions_per_set', 'number_of_sets')
    search_fields = ('exercise_name',)
    list_filter = ('exercise_name',)

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('coach_id', 'name', 'email')
    search_fields = ('name', 'email')
    list_filter = ('email',)

@admin.register(ProgramRequest)
class ProgramRequestAdmin(admin.ModelAdmin):
    list_display = ('program_id','first_name', 'request_time')
    search_fields = ('user__name',)
    list_filter = ('request_time',)

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('membership_id', 'user')
    search_fields = ('user__name',)
    filter_horizontal = ('staff',)

@admin.register(Approval)
class ApprovalAdmin(admin.ModelAdmin):
    list_display = ('approval_id', 'user', 'staff', 'approval_date')
    search_fields = ('user__name', 'staff__name')
    list_filter = ('approval_date',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_id', 'author', 'title', 'publication_time')
    search_fields = ('title', 'author__name')
    list_filter = ('publication_time',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_id', 'blog', 'user', 'publication_time')
    search_fields = ('blog__title', 'user__name')
    list_filter = ('publication_time',)


@admin.register(SportProgram)
class SportProgramAdmin(admin.ModelAdmin):
    list_display = ('program_id', 'name', 'category', 'price', 'fit_nutrient_program')
    search_fields = ('name', 'category')
    list_filter = ('category', 'fit_nutrient_program')
    filter_horizontal = ('exercises',)  

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('food_id', 'name', 'time', 'volume')
    search_fields = ('name',)
    list_filter = ('time',)

@admin.register(NutrientProgram)
class NutrientProgramAdmin(admin.ModelAdmin):
    list_display = ('program_id', 'name', 'category', 'price')
    search_fields = ('name', 'category')
    list_filter = ('category',)
    filter_horizontal = ('foods',)