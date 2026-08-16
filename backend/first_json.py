import json

site_name = "zero-to-tech"

def make_date():
    data = {"message": "Hello, World!", "site": site_name}
    return json.dumps(data)

print(make_date())