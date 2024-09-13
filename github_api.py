import requests
from config import GitHubToken, UserName

API_URL = 'https://api.github.com/user/repos'

headers = {
    'Authorization': f'token {GitHubToken}',
    'Accept': 'application/vnd.github.v3+json'
}

def create_repository(RepositoryName):
    data = {
        "name": RepositoryName,
        "private": False
    }
    response = requests.post(API_URL, json=data, headers=headers)
    if response.status_code == 201:
        print(f'Repository "{RepositoryName}" created successfully.')
    else:
        print(f'Failed to create repository. Status code: {response.status_code}, Response: {response.json()}')

def check_repository(RepositoryName):
    response = requests.get(API_URL, headers=headers)
    if response.status_code == 200:
        repos = response.json()
        RepositoryNames = [repo['name'] for repo in repos]
        if RepositoryName in RepositoryNames:
            print(f'Repository "{RepositoryName}" exists.')
            return True
        else:
            print(f'Repository "{RepositoryName}" does not exist.')
            return False
    else:
        print(f'Failed to list repositories. Status code: {response.status_code}, Response: {response.json()}')
        return False

def delete_repository(RepositoryName):
    delete_url = f'https://api.github.com/repos/{UserName}/{RepositoryName}'
    response = requests.delete(delete_url, headers=headers)
    if response.status_code == 204:
        print(f'Repository "{RepositoryName}" deleted successfully.')
    else:
        print(f'Failed to delete repository. Status code: {response.status_code}, Response: {response.json()}')
