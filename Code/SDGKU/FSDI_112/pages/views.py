from django.views.generic import TemplateView, AboutPageView


urlpatterns = [
    path(''. HomePageView.as_view(), name='home'),
    path('about/', HomePageView.as_view(), name='about'),

]
