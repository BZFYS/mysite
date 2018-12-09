from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect, render
from django.urls import reverse

from comment.models import Comment


# Create your views here.

def update_comment(request):
    # 重定向回到原来页面
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    user = request.user
    # 数据检查
    if user is None:
        return render(request, 'error.html', {'massage': '用户未登录', 'rediect_to': referer})
    # strip() 方法用于移除字符串头尾指定的字符(默认为空格或换行符)或字符序列
    text = request.POST.get('text', '').strip()
    if text == '':
        return render(request, 'error.html', {'massage': '内容为空', 'rediect_to': referer})
    try:
        content_type = request.POST.get('content_type', '')
        object_id = int(request.POST.get('object_id', ''))
        # 这里不太懂
        model_class = ContentType.objects.get(model=content_type).model_class()
        model_obj = model_class.objects.get(pk=object_id)
    except Exception as e:
        return render(request, 'error.html', {'massage': '评论对象不存在', 'rediect_to': referer})

    # 写数据库，
    coment = Comment()
    coment.user = user
    coment.text = text
    coment.content_object = model_obj
    coment.save()

    return redirect(referer)
