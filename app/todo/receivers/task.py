from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from todo.models import Task

@receiver(post_save, sender=Task)
def handle_task_changes(sender, instance: Task, **kwargs):
    if instance.parent_task:
        update_parent_task_completion_recursively(instance)

    if not instance.is_public:
        update_subtasks_visibility_recursively(instance)


def update_parent_task_completion_recursively(task: Task):

    if not task.parent_task:
        return

    parent_task = task.parent_task
    all_subtasks_completed = all(sub_task.is_completed for sub_task in parent_task.sub_tasks.all())
    parent_task.is_completed = all_subtasks_completed
    parent_task.save()
    update_parent_task_completion_recursively(parent_task)


def update_subtasks_visibility_recursively(task: Task):

    if task.is_public:
        return
    
    if not task.sub_tasks.exists():
        return
    
    task.sub_tasks.update(is_public=False)

    for sub_task in task.sub_tasks.all():
        update_subtasks_visibility_recursively(sub_task)

