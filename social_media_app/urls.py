from social_media_app.views import index_view, sign_up_view, sign_in_view
from django.urls import path
urlpatterns = [
    path('',index_view ,name="index"),
    path('sign-up/',sign_up_view,name="sign_up"),
    path('sign-in/',sign_in_view,name="sign_in"),

]

