from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^login/$', 'accounts.views.login', {'template_name': 'accounts/login.html'}, name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'login'}, name="logout"),
)
