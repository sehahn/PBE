from django.conf.urls import *
from dbe.questionnaire.views import *
from dbe.mcbv.base import TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns("dbe.questionnaire.views",
    (r"^$", login_required(Questionnaires.as_view()), {}, "questionnaires"),

    (r"^questionnaire/(?P<dpk>\d+)/(?P<section>\d+)/$",
     login_required( ViewQuestionnaire.as_view() ), {}, "questionnaire"),

    (r"^questionnaire/(?P<dpk>\d+)/$",
     login_required( ViewQuestionnaire.as_view() ), {}, "questionnaire"),

    (r"^user-questionnaires/(?P<dpk>\d+)/$",
     login_required( UserQuests.as_view() ), {}, "user_questionnaires"),

    (r"^user-questionnaire/(?P<dpk>\d+)/$",
     login_required( UserQuest.as_view() ), {}, "user_questionnaire"),

    (r"^quest-stats/(?P<dpk>\d+)/$",
     login_required( QuestStats.as_view() ), {}, "quest_stats"),
)

urlpatterns += patterns("",
    (r"^done/$", TemplateView.as_view(template_name="questionnaire/done.html"), {}, "done"),
)
