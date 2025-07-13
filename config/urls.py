from django.contrib import admin
from django.urls import path
from app import views  # Certifique-se de que o app se chama "app"

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('pacientes/', views.listar_pacientes, name='listar_pacientes'),
    path('', views.listar_pacientes, name='listar_pacientes'),  # Opcional: redireciona a raiz "/" para a mesma view
]
