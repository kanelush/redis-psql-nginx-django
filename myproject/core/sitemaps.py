from django.contrib import sitemaps
from django.shortcuts import reverse
from core.models import Category, Negocio

class StaticViewSitemap(sitemaps.Sitemap):
      changefreq = "weekly"
      priority = 0.5
      protocol = 'https'


      def items(self):
          return ['base', 'contact']

      def location(self, item):
          return reverse(item)

class NegocioSitemap(sitemaps.Sitemap):
      changefreq = "weekly"
      priority = 0.5
      protocol = 'https'

      def items(self):
          return Negocio.objects.all()

      def location(self, obj):
          return '/%s' % (obj.negocio_slug)

   
class CategorySitemap(sitemaps.Sitemap):
      changefreq = "weekly"
      priority = 0.5
      protocol = 'https'

      def items(self):
          return Category.objects.all()

      def location(self, obj):
          return '/categoria/%s' % (obj.id)
