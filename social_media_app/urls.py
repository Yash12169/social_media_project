from social_media_app.views import index_view, sign_up_view, sign_in_view
from django.urls import path
urlpatterns = [
    path('',index_view),
    path('sign_up/',sign_up_view),
    path('sign_in/',sign_in_view),

]
