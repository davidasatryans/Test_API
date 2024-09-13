import os
from dotenv import load_dotenv
load_dotenv()

UserName = os.getenv('UserName')
GitHubToken = os.getenv('GitHubToken')
RepositoryName = os.getenv('RepositoryName')