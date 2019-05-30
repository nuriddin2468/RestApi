import json


def LogoModelSerializer(obj, pos = True):
    if pos:
        data = []
        for x in obj:
            data.append({
                "id": x.id,
                "title": x.title,
                "images": x.images,
                "category": x.category.title,
                "tags": [datas.title for datas in x.tags.all()]
            })
        return data
    else:
        return {
            "id": obj.id,
            "title": obj.title,
            "images": obj.images,
            "category": obj.category.title,
            "tags": [datas.title for datas in obj.tags.all()]
        }