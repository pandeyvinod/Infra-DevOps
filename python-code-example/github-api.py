# using api to github to get project information
import json

import requests
import pprint

response = requests.get("https://api.github.com/users/pandeyvinod/repos",
                        headers={"Accept": "application/vnd.github.v3+json"})
my_repo = response.json()
print(json.dumps(response.json(), indent=2))  # pretty json work.
'''for repo in my_repo:
    print(f"your repo url: {repo['html_url']}")'''