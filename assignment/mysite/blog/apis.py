from django.views import View
from .models import Blog
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(csrf_exempt, name='dispatch')
class BlogAPIView(View):
    def get(self, request,  *args, **kwargs):
        if 'blog_id' in kwargs:
            blog_id = kwargs.get('blog_id')
            blog = Blog.objects.get(pk=blog_id)
            data = {'id': blog.id, 'name': blog.name, 'tagline': blog.tagline}
            return JsonResponse({'blog': data})
        else:
            blogs = Blog.objects.all()
            data = [{'id': blog.id, 'name': blog.name, 'tagline': blog.tagline} for blog in blogs]
            return JsonResponse({'blogs': data})

    def post(self, request):
        data = request.POST
        name = data.get('name')
        tagline = data.get('tagline')

        blog = Blog.objects.create(name=name, tagline=tagline)

        return JsonResponse({'id': blog.id, 'name': blog.name, 'tagline': blog.tagline})

    def put(self, request, *args, **kwargs):
        blog_id = kwargs.get('blog_id')
        blog = Blog.objects.get(pk=blog_id)

        data = request.POST
        blog.name = data.get('name', blog.name)
        blog.tagline = data.get('tagline', blog.tagline)

        blog.save()

        return JsonResponse({'id': blog.id, 'name': blog.name, 'tagline': blog.tagline})

    def delete(self, request, *args, **kwargs):
        blog_id = kwargs.get('blog_id')
        blog = Blog.objects.get(pk=blog_id)
        blog.delete()
        return JsonResponse({'message': 'Blog deleted successfully'})