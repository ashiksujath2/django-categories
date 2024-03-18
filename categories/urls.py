from django.urls import path
from django.views.generic import ListView
from .models import Category
from . import views


categorytree_dict = {
    'queryset': Category.objects.filter(level=0)
}

urlpatterns = (
    path(
        '', ListView.as_view(**categorytree_dict), name='categories_tree_list'
    ),
)

urlpatterns += (
    path('<path:path>/', views.category_detail, name='categories_category'),
)
