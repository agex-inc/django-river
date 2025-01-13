from django.contrib import admin
from django import forms

from workflow_config.models.transitionapprovalmeta import TransitionApprovalMeta


class TransitionApprovalMetaForm(forms.ModelForm):
    class Meta:
        model = TransitionApprovalMeta
        fields = ('workflow', 'transition_meta', 'permissions', 'groups', 'priority')


class TransitionApprovalMetaAdmin(admin.ModelAdmin):
    form = TransitionApprovalMetaForm
    list_display = ('workflow', 'transition_meta', 'priority')


admin.site.register(TransitionApprovalMeta, TransitionApprovalMetaAdmin)
