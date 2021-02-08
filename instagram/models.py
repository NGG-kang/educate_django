from django.conf import settings
from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField(validators=[MinLengthValidator(10)])
    photo = models.ImageField(blank=True, upload_to="instagram/post/%Y/%m/%d")
    tag_set = models.ManyToManyField('Tag', blank=True)
    # upload_to를 사용하여 위치 지정이 가능하다
    # 동일한 media폴더로 시작하나 경로명이 달라짐
    # 동일 이름도 자동으로 더미 이름을 붙혀준다
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    models.OneToOneField

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('instagram:post_detail', args=[self.pk])

    class Meta:
        ordering = ['-id']

    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = "메시지 글자수"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             limit_choices_to={'is_public':True})
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    # post_set = models.ManyToManyField(Post)
    # M:N 관계에서는 어느쪽에서든 필드 지정 가능하다

    def __str__(self):
        return self.name