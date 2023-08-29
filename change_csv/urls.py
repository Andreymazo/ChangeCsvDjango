from django.urls import path
from change_csv.apps import ChangeCsvConfig
from change_csv.views import CreateField, DeleteField, UpdateField, get_form, read_file_create_model, upldfile


app_name = ChangeCsvConfig.name

urlpatterns = [

    path('', upldfile, name='upload_file'),
    path('read_file_create_model/', read_file_create_model, name='read_file_create_model'),
    path('get_form/', get_form, name='get_form'),
    path('csv_model_create/', CreateField.as_view(), name='csv_model_create'),
    path('csv_model_update/', UpdateField.as_view(), name='csv_model_update'),
    path('csv_model_delete/', DeleteField.as_view(), name='csv_model_delete'),

]