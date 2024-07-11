from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
import datetime
from django.db.models import Q


# Create your views here.
from myapp.models import Conference,Message,My_list,User,Card,Manage_rooms,admin

# 首页
def index(request,pIndex,name):
    meeting_list = Conference.objects.all()
    for meeting_dict in meeting_list:
        time1=datetime.datetime.strftime(meeting_dict.start_time,'%Y-%m-%d%H:%M')
        print(meeting_dict.statu)
        print('这里是开始时间')
        print(time1)
        time2=datetime.datetime.strftime(meeting_dict.end_time,'%Y-%m-%d%H:%M')
        print(time2)
        if time2 < time1:
            print('time2小于time1')
        print('time2不小于time1')
        n_time=datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d%H:%M')
        print(n_time)
        if n_time > time1 and n_time < time2:
            meeting_dict.statu=True
            meeting_dict.save()
            print('自习正在进行中')
        else:
            meeting_dict.statu = False
            meeting_dict.save()


    meeting_list = Conference.objects.all()
    p = Paginator(meeting_list, 10)
    if pIndex<1:
        pIndex=1
    if pIndex>p.num_pages:
        pIndex=p.num_pages
    ulist=p.page(pIndex)
    page_list=p.page_range
    context = {
        'meeting_list': meeting_list,
        'name': name,
        'ulist':ulist,
        'pIndex':pIndex,
        'page_list':page_list,
    }
    return render(request,'myapp/index.html',context)


# def unonlion(request,name):
#     unonlion_rooms=Conference.objects.filter(meet_type='线下自习')

    # print(unonlion_rooms)

    # p=Paginator(unonlion_rooms,10)
    # if pIndex<1:
    #     pIndex=1
    # if pIndex>p.num_pages:
    #     pIndex=p.num_pages
    # ulist=p.page(pIndex)
    # page_list=p.page_range
    #
    # for h in unonlion_rooms:
    #     print(h.id,h.idm,h.allow_num,h.statu)

    #
    # context = {
    #     'rooms': unonlion_rooms,
    #     'name':name,
    #     # 'unonlion':ulist,
    #     # 'pIndex':pIndex,
    #     # 'page_list':page_list,
    # }
    # return render(request,'myapp/unonlion.html',context)





def xianshangliebiao(request,name):
    xianshangliebiao=Conference.objects.filter(meet_type='线上自习')
    context={
        'xianshangliebiao':xianshangliebiao,
        'name':name,
    }
    return render(request,'myapp/xianshangliebiao.html',context)
# 查找
def findpage(request,name):
    idm=request.POST.get('find1',None)
    ports=Conference.objects.filter(idm__contains=idm)
    context={
        'name':name,
        'xianshangliebiaos':ports
    }
    return render(request,'myapp/findpage.html',context)

# 自习信息
def info(request,id,name):
    room = Conference.objects.get(id=id)#通过自习id，找到要预约的自习室
    meet_name=room.meet_name
    if room.president==name:
        return HttpResponse("您是自习的发起者，不用预约自习！")#获得自习室的主题，判断是否是发起人
    # print(meet_name)
    # allow_num = room.allow_num

    # name_joinmeetperson=request.POST.get('yuyuename',None)#从表单获取参与者的名字

    sub_joinmeetperson = My_list.objects.filter(meet_name=meet_name)#在预约表中找到所有预约该主题的人名
    if len(sub_joinmeetperson)!=0:#有多人预约该自习
        for sub_p in sub_joinmeetperson:
            if name == sub_p.sub_name:
                return HttpResponse('你已经预约')

    sub_new=My_list()
    # sub_new.idm=room.idm
    sub_new.room_id=room.room_id
    # sub_new.open_time=room.open_time
    sub_new.allow_num=room.allow_num
    sub_new.statu=room.statu
    sub_new.meet_name=meet_name
    sub_new.operation=room.operation
    sub_new.president=room.president
    sub_new.start_time=room.start_time
    sub_new.end_time=room.end_time
    sub_new.sub_name=name
    # sub_new.meet_type=room.meet_type
    sub_new.meet_kind=room.meet_kind
    sub_new.save()
    room.allow_num = room.allow_num - 1  # 没有预约的再减1
    room.save()
    return HttpResponse('预约成功')

# room.allow_num = room.allow_num-1# 没有预约的再减1
#
#
#         sub_joinmeetperson.sub_name=name
#         sub_joinmeetperson.meet_name=meet_name
#         sub_joinmeetperson.save()


# 操作
def operation(request,id,name):
    room = Conference.objects.get(id=id)
    # name=room.name
    # meet_name=room.meet_name
    # yuyuestarttime=room.yuyuestarttime
    # yuyueendtime=room.yuyueendtime
    context={
        'room_sub':room,
        'name':name,
    }

    print(name)
    return  render(request,'myapp/sub.html',context)



#我的自习列表——方法
def mymeetings(request,pIndex,name):
    mymeetinglist=My_list.objects.filter(sub_name=name)
    if not mymeetinglist:
        mymeetinglist = My_list.objects.filter(president=name)
    print(mymeetinglist)
    # mymeetlist=[]
    # # my_sub=SUB_NAMES.objects.filter(sub_name=name)
    # # sub_temp=my_sub.meet_name#属于我的自习的名称
    # # for h in sub_temp:
    # #     mine = Conference.objects.get(meet_name=h.meet_name)#遍历当前登录者预约的所有自习
    # #     mymeetlist.append(mine)
    # #     print(mymeetlist[h])
    # # print(mymeetlist)
    #
    # my_sub = SUB_NAMES.objects.filter(sub_name__contains=name).values()
    # myall=SUB_NAMES.objects.all()
    # print(myall)
    # if len(my_sub)==0:
    #     context={
    #         'name':name,
    #         'pIndex':pIndex,
    #     }
    #     return render(request,'myapp/tips.html',context)
    # for h in my_sub:
    #     mymeetlist.append(h["meet_name"])
    #
    #
    # mine = Conference.objects.filter(meet_name__contains=mymeetlist)

    p=Paginator(mymeetinglist,10)
    if pIndex<1:
        pIndex=1
    if pIndex>p.num_pages:
        pIndex=p.num_pages
    ulist=p.page(pIndex)
    page_list=p.page_range
    print(name)
    context={'ulist':ulist,
             'pIndex':pIndex,
             'page_list':page_list,
             'name':name,
             # 'meet_kind':mine.meet_kind,
    }
    # # print(con)
    return render(request,'myapp/mymeetings.html',context)

#管理自习

def  manage(request,id,name):
        meeting = My_list.objects.get(id=id)
        # if meet_type==meeting.meet_type:
        #     context = {
        #         'id': meeting.id,
        #         'idm': meeting.idm,
        #         'president': meeting.president,
        #         'meet_name': meeting.meet_name,
        #         'start_time': meeting.start_time,
        #         'end_time': meeting.end_time,
        #         'allow_num': meeting.allow_num,
        #         'meet_type': meeting.meet_type,
        #         'meet_kind':meeting.meet_kind,
        #         'name':name,
        #     }
        #     print(meeting.start_time,meeting.meet_name)
        #     return render(request, 'myapp/onmanagemeeting.html', context)
        # print(meeting.values())
        context = {
                'meeting':meeting,
                'name':name,
            }
        return render(request, 'myapp/managemeeting.html', context)

#取消自习

def cancel_meet(request,id,name,pIndex):
    meeting = My_list.objects.get(id=id)

    add_num = Conference.objects.get(meet_name=meeting.meet_name,president=meeting.president,start_time=meeting.start_time,end_time=meeting.end_time)
    add_num.allow_num=add_num.allow_num+1
    add_num.save()
    meeting.delete()
    context={
        'name':name,
        'pIndex':pIndex,
    }

    return render(request,'myapp/cancel_meet.html',context)




#管理自习(获取表单信息，赋值给Conference和My_list保存，
def re_editmeet(request,id,name):
    meet_name = request.POST.get('meet_name', None)
    print(meet_name)
    meet_kind = request.POST.get('meet_kind', None)
    # meet_type=request.POST.get('meet_type','线下自习')
    room_id = request.POST.get('room_id', None)
    # president = request.POST.get('president', None)
    start_time = request.POST.get('start_time', None)
    # print(start_time)
    end_time = request.POST.get('end_time', None)
    # sub_name = request.POST.get('president', None)
    # statu = request.POST.get('statu', False)
    # operation = request.POST.get('operation', '预约')
    allow_num = request.POST.get('allow_num', None)
    print(meet_name)
    my_creat = My_list.objects.get(id=id)
    print(my_creat)
    meeting = Conference.objects.get(meet_name=my_creat.meet_name, room_id=my_creat.room_id, start_time=my_creat.start_time,
                         end_time=my_creat.end_time)
    print(meeting)
    my_creat.meet_name = meet_name
    # my_creat.president = president
    my_creat.meet_kind = meet_kind
    my_creat.room_id = room_id
    # print(my_creat.room_id)
    my_creat.start_time = start_time
    my_creat.end_time = end_time
    my_creat.sub_name = name
    # my_creat.statu = statu
    # my_creat.operation = operation
    my_creat.allow_num = allow_num

    meeting.meet_name = meet_name
    meeting.meet_kind = meet_kind
    meeting.room_id = room_id
    # meeting.president = president
    meeting.start_time = start_time
    meeting.end_time = end_time
    # meeting.sub_name = sub_name
    # meeting.statu = statu
    # meeting.operation = operation
    # meeting.open_time=open_time
    meeting.allow_num = allow_num
    # meeting.meet_type=meet_type
    # if meeting.president == name:

    meeting.save()
    my_creat.save()
    context={
        'name':name,
        'pIndex':1,
    }
    return  render(request,'myapp/re_editsuccessful.html',context)

def end_mycreate(request,id,name):
    end_mymeeting=My_list.objects.get(id=id)
    meet_name=end_mymeeting.meet_name
    room_id=end_mymeeting.room_id
    start_time=end_mymeeting.start_time
    end_time=end_mymeeting.end_time
    end_meeting=Conference.objects.get(president=name,meet_name=meet_name,room_id=room_id,start_time=start_time,end_time=end_time)
    end_meeting.delete()
    # end_mymeeting.delete()
    return HttpResponse('您已结束自习！')


#登录方法
def login(request):
    return render(request,'myapp/login.html')


def logining(request):
    message = Message.objects.all()
    name=request.POST.get('name',None)
    password=request.POST.get('password',None)
    print(name,password)
    user = User.objects.filter(name=name, password=password)
    print(user)
    if name and password:
        user = User.objects.filter(name=name, password=password)
        if user:
            context = {
                'info': "登陆成功",
                'name': name,
                'message':message,
            }
            request.session['airport_user'] = {'name': name, 'password': password}
        else:
            context = {
                'info': "登录失败/用户名、密码错误"
            }
            return render(request, 'myapp/login_info.html', context)
    else:
        context = {
            'info': "用户名或者密码不能为空"
        }
        return render(request, 'myapp/login_info.html', context)
    # print('登录人名'+name)
    return render(request,'myapp/meeting_personal.html',context)
# def logining(request):
#     return render(request,'myapp/zhuce.html')

#注册方法
def zhuce(request):
    return render(request,'myapp/zhuce.html')


def zhuceing(request):
    name=request.POST.get('name',None)
    password=request.POST.get('password',None)
    repassword=request.POST.get('repassword',None)
    sex=request.POST.get('sex',None)
    city=request.POST.get('city',None)
    tel=request.POST.get('tel',None)
    if name and password and  repassword:
        old_user = User.objects.filter(name=name)
        if old_user.count() != 0:
            return HttpResponse('用户已存在')
        else:
            if (password == repassword):
                user = User()
                user.name = name
                user.password = password
                user.repassword = repassword
                user.sex = sex
                user.city = city
                user.tel = tel
                user.save()
                context = {
                    'info': "注册成功"
                }
            else:
                return HttpResponse('两次密码不一致')
    else:
        return HttpResponse('用户名或者密码为空')
    return render(request,'myapp/login_info.html',context)


#登录到个人中心
def meeting_personal(request,name):
    mess=Message.objects.all()
    context = {
        'name': name,
        'mess':mess,
    }
    return render(request,'myapp/meeting_personal.html',context)



def dologout(request):
    # del request.session['airport_user']
    request.session.flush()
    return render(request,'myapp/login.html')


def edit_person(request,name):
    # print(name)
    port=User.objects.filter(name=name)[0]
    context={
        'name': port.name,
        'password': port.password,
        'repassword': port.repassword,
        'sex':port.sex,
        'city':port.city,
        'tel':port.tel,
    }
    return  render(request,'myapp/edit_person.html',context)


#删除个人信息

def delet(request,name):
    port=User.objects.get(name=name)
    s=port.name+"已注销"
    port.delete()
    context={
        'info':s
    }
    return render(request,'myapp/login_info.html',context)


#返回个人中心
def ret_per(request,name):
    context={
        'name':name,
    }
    return render(request,'myapp/meeting_personal.html',context)



#修改个人信息
def editdata(request,name):
    port=User.objects.get(name=name)
    port.name=request.POST.get('name',None)
    port.password=request.POST.get('password',None)
    port.repassword=request.POST.get('repassword',None)
    port.sex=request.POST.get('sex',None)
    port.city=request.POST.get('city',None)
    port.tel=request.POST.get('tel',None)
    port.save()

    context={
        'info':"已修改完成"
    }

    return render(request,'myapp/login_info.html',context)

#顶部大按钮跳转方法
def meeting_list(request,pIndex,name):
    context = {
        'name': name,
        'pIndex':pIndex,
    }
    return render(request, 'myapp/index.html',context)

def top_personalcentre(request,pIndex,name):
    message = Message.objects.all()
    context={
        'name':name,
        'pIndex':pIndex,
        'message':message,
    }
    return render(request,'myapp/meeting_personal.html',context)


#申请自习室方法路径
def createmeeting(request,name):
    context={
        'name':name
    }
    return render(request,'myapp/createmeeting.html',context)

def onlinemeeting(request,name):
    context = {
        'name': name
    }
    return render(request,'myapp/onlinemeeting.html',context)


def onmanagemeeting(request):
    return render(request,'myapp/onmanagemeeting.html')

def offmanagemeeting(request):
    return render(request,'myapp/offmanagemeeting.html')


#创建线下自习
def insert(request,name):
    meet_name=request.POST.get('meet_name',None)
    meet_kind=request.POST.get('meet_kind',None)
    # meet_type=request.POST.get('meet_type','线下自习')
    room_id=request.POST.get('room_id',None)
    president = request.POST.get('president',None)
    start_time = request.POST.get('start_time',None)
    print(start_time)
    end_time = request.POST.get('end_time',None)
    sub_name = request.POST.get('president',None)
    statu = request.POST.get('statu',False)
    operation = request.POST.get('operation','预约')
    meeting_room = Manage_rooms.objects.filter(room_id=room_id).values()
    if not meeting_room:
        return HttpResponse('【%s】自习室不存在或者管理员还没放出，请输入或者选择目前存在的自习室'%room_id)
    print("===%s"%meeting_room)
    allow_num = request.POST.get('allow_num',None)
    print(room_id)
    meeting=Conference()
    print(meeting)
    meeting.meet_name=meet_name
    meeting.meet_kind=meet_kind
    meeting.room_id=room_id
    meeting.president=president
    meeting.start_time=start_time
    meeting.end_time=end_time
    meeting.sub_name=sub_name
    meeting.statu=statu
    meeting.operation=operation
    # meeting.open_time=open_time
    meeting.allow_num=allow_num
    # meeting.meet_type=meet_type


    if meeting.president==name:
        my_creat=My_list()
        my_creat.meet_name=meet_name
        my_creat.president=president
        my_creat.meet_kind=meet_kind
        my_creat.room_id=room_id
        my_creat.start_time=start_time
        my_creat.end_time=end_time
        my_creat.sub_name=name
        my_creat.statu=statu
        my_creat.operation=operation
        my_creat.allow_num=allow_num
        my_creat.save()
    meeting.save()
    context={
        'name':name,
    }
    return render(request, 'myapp/createmeet_successful.html',context)



def tips(request,name):
    context={
        'name':name
    }
    return render(request, 'myapp/createmeeting.html',context)


#打卡

#打卡存入信息到Card

def singn_carding(request,id,name):
    my_card=My_list.objects.get(id=id)

    room_id=my_card.room_id
    meet_name=my_card.meet_name
    card_name=name
    now=datetime.datetime.now()
    card_time=now.strftime("%Y-%m-%d %H:%M:%S")
    card=Card()
    card.room_id=room_id
    card.meet_name=meet_name
    card.card_time=card_time
    card.card_name=card_name
    card.save()
    meeting = Conference.objects.get(meet_name=my_card.meet_name, room_id=my_card.room_id,
                                     start_time=my_card.start_time,
                                     end_time=my_card.end_time)
    print("剩余预约人数：%s"%meeting.allow_num)
    if meeting.allow_num == 0:
        meeting.delete()
    my_card.delete()
    context={
        'card_time':card_time,
        'info':"打卡成功",
        'name':name,
        'card':card,
    }
    return render(request,'myapp/sign_card.html',context)

#个人中心我参加过的自习中显示
def show_join(request,name):
    card = Card.objects.all()
    context={
        'name':name,
        'cards':card
    }
    return render(request,'myapp/show_join.html',context)


# 管理员登录
def admin_login(request):
    return render(request,'myapp/admin_login.html')

def admin_logining(request):
    name = request.POST.get('name', None)
    password = request.POST.get('password', None)
    print(name,password)
    if name and password:
        admin_user = admin.objects.filter(name=name, password=password)
        if admin_user:
            context = {
                'info': "登陆成功",
                'name': name,
            }
        else:
            context = {
                'info': "登录失败/用户名、密码错误"
            }
            return render(request, 'myapp/login_info.html', context)
    else:
        context = {
            'info': "用户名或者密码不能为空"
        }
        return render(request, 'myapp/login_info.html', context)

    return render(request, 'myapp/admin_index.html', context)

# 管理用户
def manage_user(request):
    manage_user=User.objects.all()

    context={
        'user':manage_user,
    }

    return render(request,'myapp/manage_user.html',context)
# 删除用户
def user_delet(request, id):
        a = User.objects.get(id=id)
        a.delete()
        context = {
            'info': "用户" + a.name + "已删除"
        }
        return render(request, 'myapp/info.html', context)


#自习室浏览界面
def meetingroom(request,name):
    meeting_rooms = Manage_rooms.objects.all()

    context = {
        'name':name,
        'meeting_rooms': meeting_rooms,
               }
    return render(request,'myapp/meetingroom.html',context)

def admin_base(request):
    return render(request,'myapp/admin_base.html')

def admin_adddata(request):
    return render(request, 'myapp/admin_adddata.html')

def admin_index(request):
    return render(request,'myapp/admin_index.html')

def admin_showdata(request,pIndex=1):
    conferences=Conference.objects.all()
    p=Paginator(conferences,5)
    if pIndex<1:
        pIndex=1
    if pIndex>p.num_pages:
        pIndex=p.num_pages
    ulist=p.page(pIndex)
    page_list=p.page_range
    context={'conferences':ulist,
             'pIndex':pIndex,
             'page_list':page_list}
    return render(request,'myapp/admin_showdata.html',context)

def admin_findpage(request,pIndex=1):
    meet_name=request.POST.get('find1',None)
    ports=Conference.objects.filter(meet_name__contains=meet_name)
    p=Paginator(ports,5)
    if pIndex<1:
        pIndex=1
    if pIndex>p.num_pages:
        pIndex=p.num_pages
    page_list=p.page_range
    ulist=p.page(pIndex)
    context={
        'conferences':ulist,
        'pIndex':pIndex,
        'page_list':page_list
    }
    return render(request,'myapp/admin_findpage.html',context)

def admin_delet(request,id):
    port=Conference.objects.get(id=id)
    s=port.meet_name+"已删除"
    port.delete()
    context={
        'info':s
    }
    return render(request,'myapp/info.html',context)

def admi_adddata(request):
    b=Manage_rooms.objects.all()
    context={
        "shujus":b,
    }
    return render(request,'myapp/admi_adddata.html',context)

def admin_editdata(request,id):
    port=Conference.objects.get(id=id)
    port.room_id=request.POST.get('room_id',None)
    port.allow_num=request.POST.get('allow_num',None)
    port.statu=request.POST.get('statu',None)
    port.meet_name=request.POST.get('meet_name',None)
    port.operation=request.POST.get('operation',None)
    port.president=request.POST.get('president',None)
    port.start_time=request.POST.get('start_time',None)
    port.end_time=request.POST.get('end_time',None)
    port.sub_name=request.POST.get('sub_name',None)
    port.meet_kind=request.POST.get('meet_kind',None)
    port.save()

    return HttpResponse(port.meet_name+'已更新完毕')
    # return render(request,'myapp/admin_showdata.html')

def admin_edit(request,id):
    port=Conference.objects.get(id=id)
    context={
        'id':port.id,
        'room_id':port.room_id,
        'allow_num':port.allow_num,
        'statu':port.statu,
        'meet_name':port.meet_name,
        'operation':port.operation,
        'president':port.president,
        'start_time':port.start_time,
        'end_time':port.end_time,
        'sub_name':port.sub_name,
        'meet_kind':port.meet_kind,
    }
    return render(request,'myapp/admin_edit.html',context)

def admin_insert(request):
    room_id=request.POST.get('room_id',None)
    allow_num=request.POST.get('allow_num',None)
    statu=request.POST.get('statu',None)
    meet_name=request.POST.get('meet_name',None)
    operation=request.POST.get('operation',None)
    president=request.POST.get('president',None)
    start_time=request.POST.get('start_time',None)
    end_time=request.POST.get('end_time',None)
    sub_name = request.POST.get('sub_name', None)
    meet_kind = request.POST.get('meet_kind', None)

    port=Conference()
    port.room_id=room_id
    port.allow_num=allow_num
    port.statu=statu
    port.meet_name=meet_name
    port.operation=operation
    port.president=president
    port.start_time=start_time
    port.end_time=end_time
    port.sub_name=sub_name
    port.meet_kind=meet_kind
    port.save()

    return HttpResponse(meet_name+'添加完毕')

def admi_adddata(request):
    shujus=Manage_rooms.objects.all()

    context={
        'shujus':shujus
    }
    return render(request,'myapp/admi_adddata.html',context)

def admi_editdata(request,id):
    port=Manage_rooms.objects.get(id=id)
    context={
        'id':port.id,
        'room_id':port.room_id,
        'room_statu':port.room_statu,
        'allow_num':port.allow_num,
        'open_starttime':port.open_starttime,
        'open_endtime':port.open_endtime,
    }
    return render(request,'myapp/admi_editdata.html',context)

def admi_edit(request,id):
    port = Manage_rooms.objects.get(id=id)
    port.room_id = request.POST.get('room_id', None)
    port.room_statu = request.POST.get('room_statu', None)
    port.allow_num = request.POST.get('allow_num', None)
    port.open_starttime = request.POST.get('open_starttime', None)
    port.open_endtime = request.POST.get('open_endtime', None)
    port.save()
    return HttpResponse("更新完成")

def admi_delet(request,id):
    port=Manage_rooms.objects.get(id=id)
    s=port.room_id+"已删除"
    port.delete()

    HttpResponse("删除成功")
    return render(request,'myapp/admi_adddata.html')

def admi_adddat(request):
    return render(request, 'myapp/admi_adddat.html')

def admi_insert(request):
    room_id=request.POST.get('room_id',None)
    room_statu=request.POST.get('room_statu',None)
    allow_num=request.POST.get('allow_num',None)
    open_starttime=request.POST.get('open_starttime',None)
    open_endtime=request.POST.get('open_endtime',None)
    print(room_statu,allow_num,open_starttime,open_endtime,)

    port=Manage_rooms()
    port.room_id=room_id
    port.room_statu=room_statu
    port.allow_num=allow_num
    port.open_starttime=open_starttime
    port.open_endtime=open_endtime
    port.save()

    return HttpResponse(room_id+'添加完毕')

def admi_addroom(request):
    room_id=request.POST.get('room_id1',None)
    room_statu=request.POST.get('room_statu1',None)
    allow_num=request.POST.get('allow_num1',None)
    open_starttime=request.POST.get('open_starttime1',None)
    open_endtime=request.POST.get('open_endtime1',None)
    print(room_statu,allow_num,open_starttime,open_endtime,)

    port=Manage_rooms()
    port.room_id=room_id
    port.room_statu=room_statu
    port.allow_num=allow_num
    port.open_starttime=open_starttime
    port.open_endtime=open_endtime
    port.save()

    return HttpResponse(room_id+'添加完毕')

#预约自习室
def sub_room(request,room_id,name):
    room=Manage_rooms.objects.get(room_id=room_id)
    # print(room)
    print(room_id,name)
    room.room_statu=False
    room.save()
    context={
        'name':name,
        'room':room,
    }

    return render(request,'myapp/createmeeting.html',context)



#信息通知栏
def message_insert(request):
    message_content=request.POST.get('message_content',None)
    now=datetime.datetime.now()
    message_time=now.strftime("%Y-%m-%d %H:%M:%S")
    message=Message()
    message.message_time=message_time
    message.message_content=message_content
    message.save()
    show_message=Message.objects.all()

    context={
        'info':"发布成功",
        'show_message':show_message,
    }
    return render(request,'myapp/show_message.html',context)



def message_edit(request,id):
    port=Message.objects.get(id=id)
    context={
        'id':port.id,
        'message_time':port.message_time,
        'message_content':port.message_content,
    }

    return  render(request,'myapp/message_edit.html',context)

def message_editing(request,id):
    message=Message.objects.get(id=id)
    message.message_time=request.POST.get('message_time',None)
    message.message_content=request.POST.get('message_content',None)
    message.save()
    context = {
        'info': "修改成功！"
    }
    return render(request,'myapp/admin_index.html', context)

def message_delete(request,id):
    message=Message.objects.get(id=id)
    message.delete()
    context={
        'info':"消息删除成功！"
    }
    return render(request,'myapp/admin_index.html',context)