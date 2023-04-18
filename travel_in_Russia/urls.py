from django.urls import path

from travel_in_Russia import views

urlpatterns = [
    path('', views.CityListView.as_view()),
    path("filter/", views.FilterCityView.as_view(), name="filter"),
    path("search/", views.Search.as_view(), name="search"),
    path('add-rating/', views.AddStarRating.as_view(), name='add-rating'),
    path('<slug:slug>', views.CityDetailView.as_view(), name='city_detail'),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add-review"),
    path("profile/<int:pk>/", views.ProfileView.as_view(), name="profile"),
    path("profile/redact/<int:pk>/", views.RedactProfile.as_view(), name="redact"),
    path("profile/update/", views.UpdateProfile.as_view(), name="update"),
]
