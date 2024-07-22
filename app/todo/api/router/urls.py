from todo.api.router.user import urlpatterns as userAPI
from todo.api.router.project import urlpatterns as projectAPI
from todo.api.router.task import urlpatterns as taskAPI

api_urls = [
    *userAPI,
    *projectAPI,
    *taskAPI,
]