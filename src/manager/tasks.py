# Create your tasks here
from time import sleep


from celery import shared_task



@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

# @shared_task
# def sleep_task(pause, id):
#     sleep(pause)
#     Table.objects.create(result=pause * 2, user_id=id)
#     return 'hello-world'

@shared_task
def hello():
    return "hello task"