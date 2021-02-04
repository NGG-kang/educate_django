from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # 어드민 화면에 출력
    list_display = ['id', 'photo_tag', 'message', 'message_length', 'is_public', 'created_at', 'updated_at']
    # 어드민 오브젝트 링크 지정
    list_display_links = ['message']
    # 어드민 오브젝트 필터 지정
    list_filter = ['created_at', 'is_public']
    # 어드빈 오브젝트 검색 기능
    search_fields = ['message']

    # models의 self딴에서도 할 수 있으나 어드민에서도 지정이 가능하다
    # post로 넘어오므로 self, post로 지정해야한다
    def message_length(self, post):
        return len(post.message)

    def photo_tag(self,post):
        if post.photo:
            # 보통 html태그는 그냥 텍스트로 나오는데
            # mark_safe라는 유틸을 사용하면 태그가 적용된다
            return mark_safe(f'<img src="{post.photo.url}" style="width:75px;" />')
        return None