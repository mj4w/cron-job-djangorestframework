# CRON JON (DjangoRestFramework) 
- removing user <b>is_active=False</b> and expire in 3 days

## Command
- python manage.py loaddata user-fixtures
- python manage.py user-check
## Postman 
```
    METHOD: GET
    localhost:8000/accounts/user/
```
