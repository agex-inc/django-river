Authorization
=============
``django-workflow_config`` provides system users an ability to configure the authorizations at three level. Those are permissions, user group or a specific user at any step. If the
user is not authorized, they are not entitled to see and approve those approvals. These three authorization mechanisms are also not blocking each other. An authorized user
by any of them is entitled to see and approve the approvals.


Permission Based Authorization
""""""""""""""""""""""""""""""
Multiple permission can be specified on the `transition approval metadata` admin page and ``django-workflow_config`` will allow only the users who have the given permission.
Given multiple permissions are issued in ``OR`` fashion meaning that it is enough to have one of the given permissions to be authorized for the user. This can be
configurable on the admin page provided by `django-workflow_config`

User Group Based Authorization
""""""""""""""""""""""""""""""
Multiple user group can be specified on the `transition approval metadata` admin page and ``django-workflow_config`` will allow only the users who are in the given user groups.
Like permission based authorization, given multiple user groups are issued in ``OR`` fashion meaning that it is enough to be in one of the given user groups to be
authorized for the user.This can be configurable on the admin page provided by `django-workflow_config`

User Based Authorization
""""""""""""""""""""""""
Only one specific user can be assigned and no matter what permissions the user has or what user groups the user is in, the user will be authorized. Unlike the other
methods, ``django-workflow_config`` doesn't provide an admin interface for that. But this can be handled within the repositories that is using `django-workflow_config`. The way how to do
this is basically setting the ``transactioner`` column of the related ``TransitionApproval`` object as the user who is wanted to be authorized on this approval either
programmatically or through a third party admin page on this model.
