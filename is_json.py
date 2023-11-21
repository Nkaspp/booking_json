import json
def is_json (string):
    try:
        d = json.loads(json_string)
        return True
    except:
        return False

json_string = '{"a": 1, "rgrb": 2}'
print(is_json(json_string))