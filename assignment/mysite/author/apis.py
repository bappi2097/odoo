from django.views import View
from .models import Author
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

    
@method_decorator(csrf_exempt, name='dispatch')
class AuthorAPIView(View):
    def get(self, request, *args, **kwargs):
        if 'author_id' in kwargs:
            author_id = kwargs.get('author_id')
            author = Author.objects.get(pk=author_id)
            data = {'id': author.id, 'name': author.name, 'email': author.email}
            return JsonResponse({'author': data})
        else:
            authors = Author.objects.all()
            data = []
            for author in authors:
                data.append({'id': author.id, 'name': author.name, 'email': author.email})
            return JsonResponse({'authors': data})

    def post(self, request):
        data = request.POST
        name = data.get('name')

        # print(name)

        email = data.get('email')

        # print(data)

        author = Author.objects.create(name=name, email=email)

        return JsonResponse({'id': author.id, 'name': author.name, 'email': author.email})
    
    def put(self, request, author_id):
        author = Author.objects.get(pk=author_id)

        data = request.POST
        author.name = data.get('name', author.name)
        author.email = data.get('email', author.email)
        # print(author, data)
        author.save()

        return JsonResponse({'id': author.id, 'name': author.name, 'email': author.email})

    def delete(self, request, author_id):
        author = Author.objects.get(pk=author_id)
        author.delete()
        return JsonResponse({'message': 'Author deleted successfully'})