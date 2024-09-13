from config import GitHubToken, RepositoryName
from github_api import check_repository, create_repository, delete_repository

API_URL = 'https://api.github.com/user/repos'

headers = {
    'Authorization': f'token {GitHubToken}',
    'Accept': 'application/vnd.github.v3+json'
}

def main():
    create_repository(RepositoryName)

    if check_repository(RepositoryName):
        delete_repository(RepositoryName)

    if check_repository(RepositoryName):
        assert False, f"Repository {RepositoryName} should be removed"

if __name__ == '__main__':
    main()

