from django .db import models

class Division(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    code = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name