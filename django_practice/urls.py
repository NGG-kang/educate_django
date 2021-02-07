
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path('', RedirectView.as_view(
        pattern_name='instagram:post_list',
    ), name='root'),
    path('admin/', admin.site.urls),
    path('blog1/', include('blog1.urls')),
    path('instagram/', include('instagram.urls')),
    path('accounts/', include('accounts.urls')),
]

# 이미지 출력
if settings.DEBUG: # 디버그 체크 안해도 스태틱 함수는 자동으로 디버크 체크하여 빈 리스트를 반환한다
                   # 근데 가시성을 위해 넣었다고 한다
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]


# settings.MEDIA_URL
# settings.MEDIA_ROOT
# django에 파일 읽어오는게 없어서 URL 설정만 해도 안나온다