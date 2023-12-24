import requests


USERNAME = 'Bammez'
ACCESS_TOKEN = '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'


BASE_URL = 'https://api.github.com'


def get_repositories(username):
    url = f'{BASE_URL}/users/{username}/repos'
    response = requests.get(url, headers={'Authorization': f'token {ACCESS_TOKEN}'})

    if response.status_code == 200:
        repositories = response.json()
        return repositories
    else:
        print(f'Error fetching repositories for {username}. Status code: {response.status_code}')
        return None


def get_members(repo_name, owner):
    url = f'{BASE_URL}/repos/{owner}/{repo_name}/collaborators'
    response = requests.get(url, headers={'Authorization': f'token {ACCESS_TOKEN}'})

    if response.status_code == 200:
        members = response.json()
        return members
    else:
        print(f'Error fetching members for {repo_name}. Status code: {response.status_code}')
        return None


def main():
    
    repository_name = '23W-GBAC'

    
    members = get_members(repository_name, USERNAME)

    if members:
        print(f'Members in the {repository_name} repository:')
        for member in members:
            print(f'- {member["login"]}')

        
        for member in members:
            member_repositories = get_repositories(member['login'])
            if member_repositories:
                print(f'\nRepositories for {member["login"]}:')
                for repo in member_repositories:
                    print(f'-  {repo["name"]}')
            print('\n' + '-' * 30)


if __name__ == '__main__':
    main()
