from todo.api.router.user import urlpatterns as userAPI
from todo.api.router.project import urlpatterns as projectAPI

api_urls = [
    *userAPI,
    *projectAPI
]