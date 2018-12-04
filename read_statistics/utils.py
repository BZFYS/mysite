# -*- coding:utf8 -*-
# @Time    : 18-12-4 上午10:50
# @Author  : 田科
# @Email   : sjztianke@hotmail.com
# @File    : utils.py
# @Software: PyCharm
from django.contrib.contenttypes.models import ContentType

from read_statistics.models import ReadNum


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
    # 返回key 用来写cookie
    return key
