from django.db import models
from django.contrib.auth.models import User


class studenttasks(models.Model):
    choices = (
        ('solved','solved'),
        ('unsolved','unsolved')
    )
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="studenttask")
    master = models.ForeignKey(User, on_delete=models.CASCADE,related_name="mastersolvedtasks",null=True)
    left_number = models.IntegerField()
    right_number = models.IntegerField()
    operator = models.CharField(max_length= 5)
    calculation = models.CharField(max_length=100)
    result = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=choices, default='unsolved')

    def __str__(self):
        return self.student.username
