from django.urls import path,include
from . import views

urlpatterns = [
#登录、注册及个人中心方法路径、base跳转路径、我的自习、自习列表路径
    path('', views.login, name='login'),
    path('logining', views.logining, name='logining'),
    path('zhuce', views.zhuce, name='zhuce'),

    path('zhuceing', views.zhuceing, name='zhuceing'),
    path('meeting_personal/<str:name>', views.meeting_personal, name='meeting_personal'),
    path('edit_person/<str:name>', views.edit_person, name='edit_person'),
    path('dologout', views.dologout, name='dologout'),
    path('edit_person/<str:name>', views.edit_person, name='edit_person'),
    path('delet/<str:name>', views.delet, name='delet'),
    path('editdata/<str:name>', views.editdata, name='editdata'),
    # path('meeting_list/<int:pIndex>/<str:name>', views.meeting_list, name='meeting_list'),
    # path('meets_my/<int:pIndex>/<str:name>', views.meets_my, name='meets_my'),
    # path('meeting_create/<int:pIndex><str:name>', views.meeting_create, name='meeting_create'),
    path('top_personalcentre/<int:pIndex><str:name>', views.top_personalcentre, name='top_personalcentre'),
    path('manage/<int:id>/<str:name>',views.manage,name='manage'),
    path('tips/<str:name>',views.tips,name='tips'),
    #path('admin/', admin.site.urls),


#自习列表及我的自习方法路径
    path('index/<int:pIndex>/<str:name>', views.index, name='index'),
    # path('unonlion/<str:name>', views.unonlion, name='unonlion'),

    path('xianshangliebiao/<str:name>', views.xianshangliebiao, name='xianshangliebiao'),
    path('findpage<str:name>', views.findpage, name='findpage'),
    path('info/<int:id>/<str:name>', views.info, name='info'),
    path('operation/<int:id>/<str:name>', views.operation, name='operation'),
    path('mymeetings/<int:pIndex>/<str:name>', views.mymeetings, name='mymeetings'),

#申请自习室、管理自习路径
    path('createmeeting/<str:name>',views.createmeeting,name='createmeeting'),
    # path('offlinemeeting/<str:name>', views.offlinemeeting, name='offlinemeeting'),
    # path('onlinemeeting/<str:name>', views.onlinemeeting, name='onlinemeeting'),
    path('onmanagemeeting', views.onmanagemeeting, name='onmanagemeeting'),
    path('offmanagemeeting', views.offmanagemeeting, name='offmanagemeeting'),
    path('insert/<str:name>',views.insert,name='insert'),
    # path('create/<str:name>',views.create,name='create'),
    path('re_editmeet/<int:id>/<str:name>',views.re_editmeet,name='re_editmeet'),
    path('cancel_meet<int:id>/<str:name>/<int:pIndex>', views.cancel_meet, name='cancel_meet'),
    path('end_mycreate/<int:id>/<str:name>',views.end_mycreate,name='end_mycreate'),

    #打卡
    path('sign_carding/<int:id>/<str:name>', views.singn_carding, name='sign_carding'),
    path('show_join/<str:name>', views.show_join, name='show_join'),
    # path('card_return/<int:id><str:name>', views.card_return, name='card_return'),
    path('meetingroom/<str:name>', views.meetingroom, name='meetingroom'),
    path('sub_room/<str:room_id>/<str:name>',views.sub_room,name='sub_room'),

    # path('editon/<int:id>',views.editon,name='editon'),


    # path('editoff/<int:id>', views.editoff, name='editoff'),
    # path('edit_offline/<int:id>', views.edit_offline, name='edit_offline'),
    # path('canceloff', views.canceloff, name='canceloff'),

    #自习打卡
    # path('', views.sign_card, name='sign_card'),
    # path('sign_carding/<int:id>', views.singn_carding, name='sign_carding'),
    # path('show_join', views.show_join, name='show_join'),

    path('admin_base', views.admin_base, name='admin_base'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_logining', views.admin_logining, name='admin_logining'),
    path('manage_user', views.manage_user, name='manage_user'),
    path('user_delet/<int:id>', views.user_delet, name='user_delet'),
    path('admin_index', views.admin_index, name='admin_index'),
    path('admin_showdata/<int:pIndex>', views.admin_showdata, name='admin_showdata'),
    path('admin_findpage/<int:pIndex>', views.admin_findpage, name='admin_findpage'),
    path('admin_edit/<int:id>', views.admin_edit, name='admin_edit'),
    path('admin_delet/<int:id>', views.admin_delet, name='admin_delet'),
    path('admin_editdata/<int:id>', views.admin_editdata, name='admin_editdata'),
    path('admin_insert', views.admin_insert, name='admin_insert'),
    path('admin_adddata', views.admin_adddata, name='admin_adddata'),

    path('admi_adddata', views.admi_adddata, name='admi_adddata'),
    path('admi_edit/<int:id>', views.admi_edit, name='admi_edit'),
    path('admi_editdata/<int:id>', views.admi_editdata, name='admi_editdata'),
    path('admi_delet/<int:id>', views.admi_delet, name='admi_delet'),
    path('admi_adadat', views.admi_adddat, name='admi_adddat'),
    path('admi_insert', views.admi_insert, name='admi_insert'),
    path('admi_addroom', views.admi_addroom, name='admi_addroom'),

#通知路径
    path('message_insert', views.message_insert, name='message_insert'),
    path('message_edit/<int:id>', views.message_edit, name='message_edit'),
    path('message_editing/<int:id>', views.message_editing, name='message_editing'),
    path('message_delete/<int:id>', views.message_delete, name='message_delete'),

]
