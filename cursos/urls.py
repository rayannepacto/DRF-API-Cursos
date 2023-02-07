from django.urls import path

from .views import CursoAPIView, AvaliacaoAPIView, CursosAPIView, AvaliacoesAPIView, CursoViewSet, AvaliacaoViewSet
from rest_framework.routers import SimpleRouter




router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)



urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name= 'cursos'),
    path('cursos/<int:pk>/',CursoAPIView.as_view(), name='curso'),
    path('cursos/<int:curso_pk>/avaliacoes/',AvaliacoesAPIView.as_view(), name='cursos_avaliacoes'),
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/',AvaliacaoAPIView.as_view(), name='curso_avaliacao'),
    path('avaliacoes/<int:pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
]
