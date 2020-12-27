import json
with open('data.json') as f:
  data = json.load(f)
def list(tag,choice):
    # Output: {'name': 'Bjson.dumps(person_dict, indent = 4, sort_keys=True)ob', 'languages': ['English', 'Fench']}
    return data[tag][choice]['url_suffix']

def list_names(tag):
    return data[tag]
