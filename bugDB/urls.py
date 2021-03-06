from django.conf.urls import url, include
from .views import *

# URLs specific to the 'bugDB' app

urlpatterns = [
    url(r'^$', allIssuesView, name="all_issues"),
    url(r'^analytics/$', analytics, name="analytics"),
    url(r'^create/$', createTicket, name="create_issue"),
    url(r'^view-issue/(?P<id>[0-9]+)/$', issueDetailedView, name="detailed_view"),
    url(r'^edit-issue/(?P<id>[0-9]+)/$', editIssue, name="edit_issue"),
    url(r'^resolve-issue/(?P<id>[0-9]+)/$', resolveIssue, name="resolve_issue"),
    url(r'^reopen-issue/(?P<id>[0-9]+)/$', reOpenIssue, name="reopen_issue"),
    url(r'^close-issue/(?P<id>[0-9]+)/$', closeIssue, name="resolve_issue"),
    url(r'^up-vote/(?P<id>[0-9]+)/$', upVoteIssue, name="upvote_issue"),
]