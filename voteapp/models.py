from django.db import models

# Models for the artist awards
class Award(models.Model):
    award_name = models.CharField(max_length=200, blank=True, null=True)
    artistNum = models.IntegerField(default=0)
    created_date = models.DateTimeField()

    def __str__(self):
        return self.award_name
    

# Model for the choice of the artist on each of the category of the awards
class Choice(models.Model):
    award = models.ForeignKey(Award, related_name='awards', on_delete=models.CASCADE)
    artist = models.CharField(max_length=200, blank=True, null=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.artist


# Triva classes for the random infos on the pages
class Triva(models.Model):
    info = models.CharField(max_length=500)

    def __str__(self):
        return self.info


class Voted(models.Model):
    userVoted = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.userVoted



   
