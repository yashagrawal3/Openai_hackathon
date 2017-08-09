from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'openAI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'',include('ai.urls',namespace = "ai")),
    url(r'^admin/', include(admin.site.urls)),
]
