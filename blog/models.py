from django.db import models
from django.contrib.auth.models import User

#博客类型表
class BlogType(models.Model):
    # 博客类型,unique=True代表唯一的
    type_name = models.CharField(max_length=10,unique=True)

    def __str__(self):
        return self.type_name

# Create your models here.
#博客表
class Blog(models.Model):
    # 标题 最大长度50
    title = models.CharField(max_length=50)
    # 内容
    content = models.TextField()
    # # 博客类型（外键），删除时，不删除关联，to_field代表关联哪个列
    # blog_type = models.ForeignKey(BlogType,on_delete=models.DO_NOTHING,to_field='type_name')
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    # 用户
    auth = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    # 是否删除
    is_delete = models.BooleanField(default=False)
    # 创建时间
    create_time = models.DateField(auto_now_add=True)
    # 更新时间
    update_time = models.DateField(auto_now=True)

    def __str__(self):
        return "<Blog: %s>" % self.title

    #定义个排序规则,否则会有警告,改完需要重新同步数据库
    class Meta:
        ordering = ['-create_time']
