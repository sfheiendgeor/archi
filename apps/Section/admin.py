from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from .models import  FB_data, R_data, I_data, H_data, LH_data, CT_data, C_data, RC_data, O_data, P_data, L_data
# Register your models here.


admin.site.register(FB_data)
admin.site.register(R_data)
admin.site.register(I_data)
admin.site.register(H_data)
admin.site.register(LH_data)
admin.site.register(CT_data)
admin.site.register(C_data)
admin.site.register(RC_data)
admin.site.register(O_data)
admin.site.register(P_data)
admin.site.register(L_data)

