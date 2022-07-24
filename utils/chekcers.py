

def check_if_json(response):
    return response.headers.get('content-type') == 'application/json'


def check_sorted_by(json, param_name):
    list_of_elems = [x[param_name] for x in json]
    return list_of_elems == sorted(list_of_elems)

