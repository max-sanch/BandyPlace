from django.urls import path
from shop import views

# URL shop app
urlpatterns = [
	path('all/', views.AllProductsView.as_view(), name='all_prods'),
	path('add/', views.AddProductView.as_view(), name='add_prod'),
	path('update/<int:pk>/', views.UpdateProductView.as_view(), name='update_prod'),
	path('delete/<int:pk>/', views.DeleteProductView.as_view(), name='delete_prod'),
]
