from django.urls import path, re_path, register_converter

from . import views
from .converters import YearConverter, MonthConverter, DayConverter


register_converter(YearConverter, 'year')
register_converter(MonthConverter, 'month')
register_converter(DayConverter, 'day')
app_name = 'instagram' # URL reverse 에서 namespace 역할을 하게 된다

urlpatterns=[
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name="post_detail"),
    # path('/archives/<int:year>/', views.archives_year),
    # re_path(r'archives/(?P<year>\d{4})/', views.archives_year)
    # path('archives/<year:year>/', views.archives_year),
    # re_path(r'(?P<pk>\d+)/$', views.post_detail),
    path('archive/', views.post_archive),
    path('archive/<year:year>', views.post_archive_year, name='post_archive_year'),
    # path('archive/<year:year>/<month:month>/<day:day>', views.post_archive_day, name='post_archive_day'),
]