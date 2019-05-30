from django.http import JsonResponse
from django.views.generic import View
import json
from api.models import *
from api.serializers import LogoModelSerializer


def api(request):
    return JsonResponse({
        "Urls": [
            {
                "Method": "GET",
                "URL": "api/logos",
                "To-DO": "View all logos"
            },
            {
                "Method": "POST",
                "URL": "api/logos",
                "To-DO": "Add logo"
            },
            {
                "Method": "GET",
                "URL": "api/logo/id",
                "To-DO": "View logo"
            },
            {
                "Method": "DELETE",
                "URL": "api/logos",
                "To-DO": "Delete logo"
            },
            {
                "Method": "PUT",
                "URL": "api/logos",
                "To-DO": "Update logo"
            },
            {
                "To-Do": "You can add category and tags from admin",
                "URL": "/admin",
                "Login@Password": "desmond@1",
                "Reason": "Because the theme is the same, the same function will have both of them like logo",
                "Thanks": "Thank you for checking",
                "Made by": "Yuldashev Nuriddin"
            }
        ]
    })


class DeleteOrUpdateOrView(View):
    def get(self, request, logo_id):
        try:
            data = LogoModel.objects.get(id=logo_id)
            return JsonResponse(LogoModelSerializer(data, False))
        except Exception:
            return JsonResponse({"Error": "Object doesn't exist"})

    def put(self, request, logo_id):
        try:
            data = json.loads(request.body.decode("utf-8"))
        except Exception:
            return JsonResponse({"Error": "Data should be in JSON Format"})
        try:
            obj = LogoModel.objects.get(id=logo_id)
        except Exception:
            return JsonResponse({"Error": "Object doesn't exist"})
        # Here is the code of update
        for key,x in data.items():
            if key == "title":
                obj.title = x
            elif key == "category":
                try:
                    category = CategoryModel.objects.get(title=data['category'])
                except Exception:
                    return JsonResponse({"Error": "There is no such category in database"})
                obj.category = category
            elif key == "tags":
                try:
                    tags = []
                    for x in data['tags']:
                        tags.append(TagsModel.objects.get(title=x))
                except Exception:
                    return JsonResponse({"Error": "There is no such tags in database"})
                obj.tags.set(tags)
            elif key == "images":
                for z in data['images']:
                    try:
                        value = z['format']
                        value = z['width']
                        value = z['height']
                        value = z['size']
                        value = z['url']
                    except KeyError:
                        return JsonResponse({"Error": "Some of arguments are missing"})
                obj.images = data['images']
        obj.save()
        return JsonResponse({"ok": "ok"})

    def delete(self, request, logo_id):
        try:
            data = LogoModel.objects.get(id=logo_id).delete()
            return JsonResponse({"ok": "ok"})
        except Exception:
            return JsonResponse({"Error": "Object doesn't exist"})


class AddOrView(View):
    def get(self, request):
        obj = LogoModel.objects.all()
        return JsonResponse(LogoModelSerializer(obj), safe=False)

    def post(self, request):
        try:
            data = json.loads(request.body.decode("utf-8"))
        except Exception:
            return JsonResponse({"Error": "Data should be in JSON Format"})
        try:
            value = data['title']
            value = data['images']
            value = data['category']
            value = data['tags']
        except KeyError:
            return JsonResponse({"Error": "Some of arguments are missing"})
        if len(data['images']) < 3:
            return JsonResponse({"Error": "Images should be more than 3 types"})
        else:
            try:
                for x in data['images']:
                    value = x['format']
                    value = x['height']
                    value = x['width']
                    value = x['size']
                    value = x['url']
            except KeyError:
                return JsonResponse({"Error": "Some arguments of images are missing"})
            try:
                category = CategoryModel.objects.get(title=data['category'])
            except Exception:
                return JsonResponse({"Error": "There is no such category in database"})
            try:
                tags = []
                for x in data['tags']:
                    tags.append(TagsModel.objects.get(title=x))
            except Exception:
                return JsonResponse({"Error": "There is no such tags in database"})

            obj = LogoModel(images=data['images'], title=data['title'], category=category)
            obj.save()
            for x in tags:
                obj.tags.add(x)
            obj.save()
            return JsonResponse({"ok": "ok"})


class TagsAddOrView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


class TagsDeleteOrUpdateOrView(View):
    def get(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass