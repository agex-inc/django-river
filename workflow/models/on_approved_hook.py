from django.db import models
from django.db.models import CASCADE
from django.utils.translation import gettext_lazy as _

from workflow.models import TransitionApprovalMeta, TransitionApproval
from workflow.models.hook import Hook


class OnApprovedHook(Hook):
    class Meta:
        unique_together = [('callback_function', 'workflowmodel', 'transition_approval_meta', 'content_type', 'object_id', 'transition_approval')]

    transition_approval_meta = models.ForeignKey(
        TransitionApprovalMeta, verbose_name=_("Transition Approval Meta"), related_name='on_approved_hooks', on_delete=CASCADE)
    transition_approval = models.ForeignKey(
        TransitionApproval, verbose_name=_("Transition Approval"), related_name='on_approved_hooks', null=True, blank=True, on_delete=CASCADE)
