from django.conf.urls import url
from meiduo_mall.apps.verifications import views
urlpatterns = [
    url(r"^sms_codes/(?P<mobile>1[358]\d{9})/$", views.SMSCodeView.as_view())
]
