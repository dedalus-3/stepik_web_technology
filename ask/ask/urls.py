from django.conf.urls import include, url
from django.contrib import admin
from qa.views import AllNewQuestion, AllPopularQuestion, QuestionDetail

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', AllNewQuestion, name='new_questions'),
    #url(r'^popular/.*$', AllPopularQuestion, name='popular_questions'),
    #url(r'^question/(?P<id>[0-9]+)/$', QuestionDetail, name='question_detail'),
    url(r'', include('qa.urls')),
]