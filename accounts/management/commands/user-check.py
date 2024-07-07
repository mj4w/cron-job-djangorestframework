from typing import Any
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from datetime import timedelta, date

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        today = date.today()
        
        users = User.objects.filter(is_active=False)
        
        for user in users:
            
            date_start = user.date_joined.date()
            date_end = date_start + timedelta(days=3)
            
            print(f'{date_start} >>> {date_end}')
            
            if date_end < today:
                User.objects.get(pk=user.id).delete()
                print(f'User Deleted {user.username}')
            
            
            