## Django在使用中的一些技巧





## 常用小操作

### format格式化
```python
>>>"{} {}".format("hello", "world")    # 不设置指定位置，按默认顺序
'hello world'
 
>>> "{0} {1}".format("hello", "world")  # 设置指定位置
'hello world'
 
>>> "{1} {0} {1}".format("hello", "world")  # 设置指定位置
'world hello world'
```

### http数据传给前端
```python
from django.http import HttpResponseRedirect, JsonResponse

return JsonResponse({})
```

### FORM 字段单独验证
```python
class RegisterPostForm(forms.Form):
    mobile = forms.CharField(required=True, min_length=11, max_length=11)
    code = forms.CharField(required=True, min_length=4, max_length=4)
    password = forms.CharField(required=True)

    # 验证手机号是否已注册
    def clean_mobile(self):
        mobile = self.data.get("mobile")
        user = UserProfile.objects.filter(mobile=mobile)
        if user:
            raise forms.ValidationError("该手机号已被注册")
        return mobile
```

### 防止basemodel字段生成表
```python
class BaseModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        # 防止BaseModel生成表
        abstract = True
```

### django内置用户密码加密方法
```python
user = UserProfile(mobile=mobile)
user.set_passdjangoword(password)  # set_password生成加密后的密码
```

### HttpResponseRedirect页面重定向跳转
```python
if user is not None:
    # 查询到用户
    login(request, user)
    # HttpResponseRedirect页面重定向
    return HttpResponseRedirect(reverse("index"))
```

### model外键定义
```python
class Lesson(BaseModel):
    # on_delete表示对应的外键数据被删除后，当前的数据应该怎么办
    # 值为models.SET_NULL不级联删除，还需参数null=True, blank=True。值为models.CASCADE会级联删除
    # course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="章节名", max_length=100)
    learn_times = models.IntegerField(verbose_name="学习时长(分钟数)", default=0)

    class Meta:
        verbose_name = "课程章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
```

### 分页
```python
class CourseListView(View):
    def get(self, request, *args, **kwargs):
        # 获取课程列表
        all_courses = Course.objects.all().order_by("-add_time")

        # 对课程数据进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_courses, per_page=5, request=request)

        courses = p.page(page)

        return render(request, "course-list.html", {
            "all_courses": courses
        })


# 注意 all_courses.object_list
{% for course in all_courses.object_list %}
{% endfor %}

<div class="pageturn">
    <ul class="pagelist">

        {% if all_courses.has_previous %}
            <li class="long"><a href="?{{ all_courses.previous_page_number.querystring }}">上一页</a>
            </li>
        {% endif %}
        {% for page in all_courses.pages %}
            {% if page %}
                {% ifequal page all_courses.number %}
                    <li class="active"><a href="?{{ page.querystring }}">{{ page }}</a></li>
                {% else %}
                    <li><a href="?{{ page.querystring }}" class="page">{{ page }}</a></li>
                {% endifequal %}
            {% else %}
                <li class="none">...</li>
            {% endif %}
        {% endfor %}
        {% if all_courses.has_next %}
            <li class="long"><a
                    href="?{{ all_courses.next_page_number.querystring }}">下一页</a></li>
        {% endif %}
    </ul>
</div>
```

### 取外键属性值
```python
<!--外键查找属性 查找课程外键课程机构的名称-->
<a href="course-detail.html">
    <span class="fl">来自{{ course.course_org.name }}</span>
</a>
```

### model数据查询倒序
```python
# order_by 倒序字段前加“-”
all_courses = Course.objects.all().order_by("-add_time")
```

### template对model charfiled choices取值
```python
# model
class Course(BaseModel):
    degree = models.CharField(verbose_name="难度", choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")), max_length=2)

# html
难度：<i class="key">{{ course.get_degree_display }}</i>
```

### template media_url拼接
```python
<img src="{{ course.image.url }}"/>
# 等同于
<img src="{{ MEDIA_URL }}{{ course.image }}"/>
```

### url中设置参数字段获取
```python
urlpatterns = [
    url(r'(?P<course_id>\d+)/detail/$', CourseDetailView.as_view(), name='detail'),
]

class CourseDetailView(View):
    def get(self, request, course_id, *args, **kwargs):
        pass
```

### 字典循环取数据快捷写法
```python
user_courses = UserCourse.objects.filter(course=course)
user_ids = [user_course.user.id for user_course in user_courses]
```

### template for循环取索引下标
```python
{% for teacher in hot_teachers %}
# forloop.counter0 会得到从0开始计算的下标
# forloop.counter 会得到从1开始计算的下标
<span class="num fl">{{ forloop.counter }}</span>
{% endfor %}
```

### template过滤处理
```python
<input type="text" value="{{ user.birthday|default_if_none:''|date:'Y-m-d' }}"/>
```






