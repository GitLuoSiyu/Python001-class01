from django.urls import path
from . import views

# register_converter(converters.IntConverter,'myint')
# register_converter(converters.FourDigitYearConverter,'yyyy')

urlpatterns = [
    path('', views.index),

    ### 带变量的URL
    # path('<int:year>', views.year),
    # path('<int:year>/<str:name>', views.name),

    ### 正则匹配
    # re_path('(?P<year>[0-9]{4}).html', views.yaers, name='urlyear'),
    # re_path('(?)')

    ### 自定义过滤器
    ### path('<myint:year>', views.year),


]






