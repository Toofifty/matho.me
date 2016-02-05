from django.contrib import admin

from .models import Question, Choice

# Create inline choices builder
# Allows adding of new choices to a question
# when it is being created, rather than
# manually creating choices and assigning them
# to questions.
class ChoiceInline(admin.TabularInline):
    # Object model to use
    model = Choice
    # Default amount
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # Layout of creation page
    fieldsets = [
        (None, {'fields': ['question_text']}),
        # Name of section of fields
        ('Date', {
            # List of fields in the section
            'fields': ['pub_date'], 
            # List of classes to use on the section.
            # 'collapse' collapses the entire section by
            # default, and can be expanded
            'classes': ['collapse']
            }),
    ]
    # Inline creation of other models, as a list
    inlines = [ChoiceInline]
    
    # Information to show on the 'select
    # question to change' page, in columns
    # Column headers are generated as best as
    # possible if not assigned in the model
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    
    # Filter options that show on the right
    # side of the page
    list_filter = ['pub_date']
    
    # Adds a search bar at the top, which
    # is able to search the following fields
    search_fields = ['question_text']
    
# Register a Question as an editable model,
# with QuestionAdmin as the formatting, access,
# etc (meta) about the Question model
admin.site.register(Question, QuestionAdmin)