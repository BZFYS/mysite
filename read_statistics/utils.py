# -*- coding:utf8 -*-
# @Time    : 18-12-4 上午10:50
# @Author  : 田科
# @Email   : sjztianke@hotmail.com
# @File    : utils.py
# @Software: PyCharm
import datetime

from django.contrib.contenttypes.models import ContentType
from django.db.models import Sum
from django.utils import timezone

from read_statistics.models import ReadNum, ReadDetail


# 增加页面访问次数统计,判断用户是否有这个cookie，如果没有，则计数
def read_statistics_once_read(request, obj):
    ct = ContentType.objects.get_for_model(obj)
    key = '%s_%s_readed' % (ct.model, obj.pk)
    if not request.COOKIES.get(key):

        if ReadNum.objects.filter(content_type=ct, object_id=obj.pk).count():
            # 如果存在记录
            readnum = ReadNum.objects.get(content_type=ct, object_id=obj.pk)
        else:
            # 不存在对应记录
            readnum = ReadNum(content_type=ct, object_id=obj.pk)
        # 技术+1
        readnum.read_num += 1
        readnum.save()
    date = timezone.now()
    if ReadDetail.objects.filter(content_type=ct, object_id=obj.pk, date=date).count():
        readDetail = ReadDetail.objects.get(content_type=ct, object_id=obj.pk, date=date)
    else:
        readDetail = ReadDetail(content_type=ct, object_id=obj.pk, date=date)
    readDetail.read_num += 1
    readDetail.save()
    # 返回key 用来写cookie
    return key


# 用于统计一周内访问量
def get_seven_days_read_data(content_type):
    today = timezone.now().date()
    dates = []
    read_nums = []
    for i in range(6, -1, -1):
        date = today - datetime.timedelta(days=i)
        dates.append(date.strftime('%m/%d'))
        read_details = ReadDetail.objects.filter(content_type=content_type, date=date)
        # 对read_num 进行求和计算,返回一个字典
        result = read_details.aggregate(read_num_sum=Sum('read_num'))
        # 将对应的value放到一个列表
        read_nums.append(result['read_num_sum'] or 0)
    # 返回列表
    return dates, read_nums


# 获取当天阅读数量
def get_today_hot_date(content_type):
    today = timezone.now().date()
    read_details = ReadDetail.objects.filter(content_type=content_type, date=today).order_by('-read_num')
    return read_details[:3]  # 获取前三条


# 获取昨天阅读数量
def get_yesterday_hot_date(content_type):
    yesterday = timezone.now().date() - datetime.timedelta(days=1)
    read_details = ReadDetail.objects.filter(content_type=content_type, date=yesterday).order_by('-read_num')
    return read_details[:3]  # 获取前三条
