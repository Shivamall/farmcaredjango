from rest_framework import routers
from article.viewsets import ArticleViewSet

router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet)
router.register(r'vuechart', ArticleViewSet)
router.register(r'', ArticleViewSet)
router.register(r'plants', ArticleViewSet)
router.register(r'statics', ArticleViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'weather', ArticleViewSet)
router.register(r'contact', ArticleViewSet)
router.register(r'aboutus', ArticleViewSet)
router.register(r'profile', ArticleViewSet)
router.register(r'header-nav', ArticleViewSet)
router.register(r'footer', ArticleViewSet)
