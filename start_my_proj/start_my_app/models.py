from django.db import models
from django.utils.timezone import now

my_choices = (
    ('Hiking', 'Hiking'),
    ('Rafting', 'Rafting'),
    ('Treking', 'Treking'),
    ('Roadtrips', 'Roadtrips')
)

# Create your models here.
class UserPosts(models.Model):
    name = models.CharField(max_length=100)
    date_time = models.DateField(default=now)
    data = models.TextField(max_length=300)
    category = models.CharField(choices=my_choices, max_length=50, )


    def __str__(self):
        return "{} : {} : {} : {}".format(self.name, self.date_time, self.data, self.category)