from django.db import models

# Create your models here.
class Person(models.Model):
    tgID = models.CharField(max_length=30)
    Name = models.TextField()

    def __str__(self):
        return self.Name

class Tasks(models.Model):
    tgID = models.CharField(max_length=30)
    Task = models.TextField()
    Description = models.TextField()
    StartDate = models.DateTimeField()
    Deadline = models.DateTimeField()
    Status = models.CharField(max_length=30)

    def __str__(self):
        return self.Task
    
class NewTask(models.Model):
    tgID = models.CharField(max_length=30)
    Task = models.TextField()
    Description = models.TextField()
    Deadline = models.DateTimeField()

    def __str__(self):
        return self.Task