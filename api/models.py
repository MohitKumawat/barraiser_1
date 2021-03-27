from django.db import models
from django.db.models import Model

from django_auth.constants import FAILURE, SUCCESS


class Team(Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name + "_" + self.id

    @classmethod
    def add_team(cls, team_name):
        try:
            obj = cls.objects.create(name=team_name)
            return {
                'status': SUCCESS,
                'data': obj
            }
        except Exception as e:
            return {
                'status': FAILURE,
                'message': f'Error: {e}'
            }


class Developers(Model):
    name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=30, blank=True)
    team = models.ForeignKey(Team,
                             on_delete=models.CASCADE)

    class Meta:
        unique_together = (('name', 'phone_number'),)

    @classmethod
    def add_developer(cls, dev_data, team_id):
        try:
            obj = cls.objects.create(name=dev_data.get('name', ''), phone_number=dev_data.get('phone_number', ''),
                                     team_id=team_id)
            return {
                'status': SUCCESS,
                'data': obj
            }
        except Exception as e:
            return {
                'status': FAILURE,
                'message': f'Error: {e}'
            }