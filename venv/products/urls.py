from django.conf.urls import url

from .views import (
    ProductListView,
    # ProductDetailView,
    ProductDetailSlugView,
    # product_list_view,
    # product_detail_view,
    # ProductFeaturedListView,
    # ProductFeaturedDetailView,
)

urlpatterns = [
    url(r'^$', ProductListView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
]
