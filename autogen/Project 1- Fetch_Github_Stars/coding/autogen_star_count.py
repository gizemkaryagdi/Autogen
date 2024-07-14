import requests

def get_star_count():
    url="https//api.github.com/repos/microsoft/Autogen"
    response=requests.get(url)
    data=response.json()
    return data['stargazers_count']
print(f"Microsoft's Autogen has {get_star_count()} stars on Github.")