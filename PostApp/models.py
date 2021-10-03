from django.db import models


class Postman(models.Model):
    Username = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)
    Full_Name = models.CharField(max_length=200)
    Age = models.IntegerField(default=20)
    Birthday = models.DateTimeField('Birthday')
    Postman_Title = models.CharField(max_length=200)

    def __str__(self):
        return self.Full_Name


class Post(models.Model):
    Post_Name = models.CharField(max_length=200)
    Postal_code = models.CharField(max_length=200)
    Post_longitude = models.CharField(max_length=200)
    Post_latitude = models.CharField(max_length=200)
    Post_city = models.CharField(max_length=200)
    Post_current_Number = models.CharField(max_length=200)
    Postman_working_in = models.ForeignKey(Postman, blank=True, null=True, on_delete=models.DO_NOTHING,)

    def __str__(self):
        return "{}: {}".format(self.Post_Name, self.Postal_code)
