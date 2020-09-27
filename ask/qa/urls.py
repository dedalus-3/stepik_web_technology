from django.conf.urls import url
from .views import AllNewQuestion, AllPopularQuestion, QuestionDetail, CreateAsk, Signup, Login

urlpatterns = [
    url(r'^popular/.*$', AllPopularQuestion, name='popular'),
    url(r'^question/(?P<id>[0-9]+)/$', QuestionDetail, name='question_detail'),
    url(r'^$', AllNewQuestion, name='home'),
    url(r'^ask/.*$', CreateAsk, name='create_question'),
    url(r'^signup/.*$', Signup, name='signup'),
    url(r'^login/.*$', Login, name='login')
]