from django.contrib import admin
from accounting.models import CustomUser
from django.contrib.auth.models import Group
from group.models import GroupCustom, GroupMember

admin.site.unregister(Group)
admin.site.register(CustomUser)
admin.site.register(GroupCustom)
admin.site.register(GroupMember)
# Register your models here.
