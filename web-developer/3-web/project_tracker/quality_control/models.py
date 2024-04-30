from django.db import models
from tasks.models import Project, Task

# Create your models here.

class BugReport(models.Model):
    STATUS_CHOISES = [
        ('New', 'Новая'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершена')
    ]

    PRIORITY_CHOISES = [
        ('Low', 'Низкий'),
        ('Middle', 'Средний'),
        ('Height', 'Высокий'),
        ('Very_height', 'Очень высокий'),
        ('Critical', 'Критический')
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name='bugs',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOISES,
        default='New'
    )
    priority = models.CharField(
        max_length=50,
        choices=PRIORITY_CHOISES,
        default='Middle'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class FeatureRequest(models.Model):
    STATUS_CHOISES = [
        ('Consideration', 'Рассмотрение'),
        ('Accepted', 'Принято'),
        ('Rejected', 'Отклонено')
    ]

    PRIORITY_CHOISES = [
        ('Low', 'Низкий'),
        ('Middle', 'Средний'),
        ('Height', 'Высокий'),
        ('Very_height', 'Очень высокий'),
        ('Critical', 'Критический')
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name='requests',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOISES,
        default='Consideration'
    )
    priority = models.CharField(
        max_length=50,
        choices=PRIORITY_CHOISES,
        default='Middle'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
