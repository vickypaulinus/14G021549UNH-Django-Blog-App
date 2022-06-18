from django.db import models
from django.contrib.auth.models import Users

# Create your models 

STATUS = (
        (0, 'Draft')
        (1, 'Publish')
)

class Post (models.Model) :
            Title = models.CharField(max_length = 200, unique = True)
            Text = models. TextField()
            Author = models. Foreignkey(User, on_delete=model. CASCADE,    related_name= 'Blog_post')
            created_date = model.DateTimeField(auto_now_add= True)
            published_date = model.DateTimeField(auto_now = True)
            
            
            class Meta:
                    ordering ['-create_date']
                    
                    
            def _str_(self):
                    return self.title
                    
