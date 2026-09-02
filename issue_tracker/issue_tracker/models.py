from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = [
    ("1", "Draft"),
    ("2", "Open"),
    ("3", "In Progress"),
    ("4", "Closed"),
]

PRIORITY_CHOICES = [
    (1, "Miniscule"),
    (2, "Slight"),
    (3, "Mild"),
    (4, "Needs Attention"),
    (5, "Severe"),
    ]


# Choices do not get enforced at the DB level, in order to enforce a ceiling you must use CheckConstraint (something to maybe consider adding later)

class Project(models.Model): 
    project_name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Issue(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    status = models.CharField(
        choices = STATUS_CHOICES,
        default = STATUS_CHOICES[1][0],
        max_length=20,
    )
    priority = models.IntegerField(
        choices = PRIORITY_CHOICES, 
        default = PRIORITY_CHOICES[0][0],
        )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)



class Comment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

