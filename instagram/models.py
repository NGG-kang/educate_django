from django.db import models

# Create your models here.
class Post(models.Model):
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to="instagram/post/%Y/%m/%d")
    # upload_to를 사용하여 위치 지정이 가능하다
    # 동일한 media폴더로 시작하나 경로명이 달라짐
    # 동일 이름도 자동으로 더미 이름을 붙혀준다
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    models.OneToOneField
    def __str__(self):
        return self.message

    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = "메시지 글자수"