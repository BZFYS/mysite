# -*- coding:utf8 -*-


from django.shortcuts import render_to_response,get_object_or_404
from blog.models import *
from django.core.paginator import Paginator

# default_encoding = 'utf-8'
# if sys.getdefaultencoding() != default_encoding:
#     reload(sys)
#     sys.setdefaultencoding(default_encoding)

# Create your views here.
def home(request):

    blogs_list_all = Blog.objects.filter(is_delete=False)
    paginator = Paginator(blogs_list_all,10) # 每10篇博客为一页
    page_number = request.GET.get('page',1) #获取页码参数get请求参数,括号里面，前面是参数后面是默认值
    page_of_blogs = paginator.get_page(page_number) #使用get_page的方式可以保证如果返回来的参数异常自动显示为默认值
    # home_page = page_of_blogs.object_list   #返回所有内容（未分页情况）

    current_page_num = page_of_blogs.number #获取当前页码
    # range 可以控制开始和结束（for i in range(1,10)代表1到10之间），max用来取得current_page_num -2 和1的最大值,然后通过list将生成器改为列表
    # +号后面，通过最小值的方式找到页面最后一个页数，然后进行查询
    page_range = list(range(max(current_page_num -2 ,1),current_page_num)) + list(range(current_page_num,min(current_page_num+2,paginator.num_pages)+1))

    #增加省略号
    # 如果page_range的第一个元素不是1，则在第二个字符增加省略号
    if page_range[0] - 1 >= 2:
        page_range.insert(0,'...')

    # 如果page_range的最后一个元素不是最后一页，则在倒数第二个字符增加省略号
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append("...")
    # print(page_range)  #
    # 增加首页和尾页
    #只要第一个不是1, page_range[0] - 1 >= 2:不会执行，所以上面的判断对这个判断不生效
    if page_range[0] != 1:
        page_range.insert(0,1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)
    # print(page_range)

    content = {}
    # content['home_page'] = home_page   # 返回所有页面
    content['page_of_blogs'] = page_of_blogs #根据页面返回
    content['type_page'] = BlogType.objects.all()
    content['page_range'] = page_range
    return render_to_response('home.html',content)

#选择具体博客
def get_page(request,blog_page):
    page = get_object_or_404(Blog,pk=blog_page,is_delete=False)
    content = {}
    content['page'] = page
    return render_to_response('page.html',content)

#根据类型查找博客
def get_type(request,blog_type):
    type_page = get_object_or_404(Blog,pk=blog_type,is_delete=False)
    print(type_page)
    content = {}
    content['type_page'] = type_page
    content['blogs'] = Blog.objects.filter(blog_type_id=blog_type,is_delete=False)
    content['blog_types'] = BlogType.objects.all()
    return render_to_response('type_page.html',content)

def index(request):
    return render_to_response('index.html')