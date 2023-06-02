from datetime import datetime, date
from django.db import models

EndTime = models.DateTimeField()

now = datetime.now()
print(now)
print(EndTime)


