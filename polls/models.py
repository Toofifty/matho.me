from django.db import models

import datetime
from django.utils import timezone

# Models are created with classes
# which extend models.Model
# These generate their own database
# tables
class Question(models.Model):
    # Attribute   = an explicit type, 
    # with validation options
    question_text = models.CharField(max_length=200)
    
    # First parameter of field is the 
    # human-name of the attribute, since
    # pub_date is not user-friendly
    pub_date = models.DateTimeField('date published')
    
    # String representation, very important
    def __str__(self):
        return self.question_text
        
    # Can have arbitrary methods
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        
    # Can set options for methods and attributes
    
    # When clicked to order, will order by pub_date
    # (since a boolean value can't really be sorted)
    was_published_recently.admin_order_field = 'pub_date'
    # Displays a small tick or cross rather than 
    # 'true' or 'false' 
    was_published_recently.boolean = True
    # Column name
    was_published_recently.short_description = 'Published recently?'
    
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text