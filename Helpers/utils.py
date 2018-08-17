from django.http import JsonResponse

def get_or_none(model,**query):
    try:
        obj = model.objects.get(**query)
    except model.DoesNotExist:
        return None    
    return obj

def assert_found(instance, message):
    response = {}
    if instance is not None:
        response['success'] = False
        response['message'] = message
        return response
    else:
        response['success'] = True
        return response    

def assert_not_found(instance, message):
    response = {}
    if instance is None:
        response['success'] = False
        response['message'] = message
        return response
    else:
        response['success'] = True
        return response    