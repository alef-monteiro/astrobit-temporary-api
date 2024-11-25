from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import LoginUserView, RegisterUserView, LogoutUserView
from .viewset import UserViewSet, SubjectViewSet, UserSubjectViewSet, QuestionViewSet, ScoreViewSet

# Criação do roteador e registro dos viewsets
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'user-subjects', UserSubjectViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'scores', ScoreViewSet)

# URLs da API
urlpatterns = [
    # URLs de API com o roteador
    path('api/', include(router.urls)),

    # Endpoints da API para login, registro e logout
    path('api/register/', RegisterUserView.as_view(), name='user_register'),  # Registro de usuário via API
    path('api/login/', LoginUserView.as_view(), name='login_user'),  # Login de usuário via API
    path('api/logout/', LogoutUserView.as_view(), name='logout_user'),  # Logout via API (no lado do cliente)
]
