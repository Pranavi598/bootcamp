from django.db import models

class Paper(models.Model):
    pmc_id = models.CharField(max_length=50, unique=True)
    title = models.TextField(blank=True)
    abstract = models.TextField(blank=True)

    def __str__(self):
        return self.pmc_id


class Figure(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name="figures")
    caption = models.TextField()

    def __str__(self):
        return f"Figure for {self.paper.pmc_id}"


class Entity(models.Model):
    figure = models.ForeignKey(Figure, on_delete=models.CASCADE, related_name="entities")
    entity = models.TextField()

    def __str__(self):
        return self.entity
