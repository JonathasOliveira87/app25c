from .models import Task
from datetime import datetime



def update_task_status_fail(sc):
    now = datetime.now()
    tasks = Task.objects.filter(EndTime__lt=now, done='doing')
    tasks.update(done='fail')

