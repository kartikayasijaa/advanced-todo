from todo.api.router.user import urlpatterns as userAPI
from todo.api.router.project import urlpatterns as projectAPI
from todo.api.router.task import urlpatterns as taskAPI
from todo.api.router.task_assignment import urlpatterns as taskAssignmentAPI

api_urls = [
    *userAPI,
    *projectAPI,
    *taskAPI,
    *taskAssignmentAPI,
]