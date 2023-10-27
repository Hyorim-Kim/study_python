from django.urls.conf import path
from myvote import views

urlpatterns = [  # name에 의한 매핑
    path('', views.DispFunc, name='disp'),  # gogo/ 이면 얘 만남
    path('<int:question_id>', views.DetailFunc, name='detail'),  # 인자 컨버터 <type:name>, gogo/1 or 2 이면 얘를 만남
    path('<int:question_id>/vote', views.VoteFunc, name='vote'),  # gogo/5/vote
    path('<int:question_id>/results', views.ResultFunc, name='results'),  # gogo/5/results
    # /gogo/2/vote -> VoteFunc -> redirect(reverse 함수 사용) -> /gogo/2/results -> ResultFunc
]