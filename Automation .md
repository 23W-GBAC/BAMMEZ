My automation is about a problem i encountered always when i wanted to see the members in the same group repository and to display there class repositories since i wanted to know how they were doing and to keep up with my class members . so i was inspired to create an automation code to help me display members in my class repository and also display there repositories .
import requests

# First step
I added my git hub user name and added the access token to give access to my code so that it could access my github account and also the access token to act as an access key to my git hub account.then i added the base URL.
USERNAME = 'Bammez'
ACCESS_TOKEN = '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'


BASE_URL = 'https://api.github.com'

# second step
I created the def function to define to get repository user name.

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
# third step 
I replaced the repository name with the real class repository which is 23W-GBAC

    repository_name = '23W-GBAC'

    members = get_members(repository_name, USERNAME)

    if members:
        print(f'Members in the {repository_name} repository:')
        for member in members:
            print(f'- {member["login"]}')
#  fourth step 
        
    I fetched the repositories for each member.
        for member in members:
            member_repositories = get_repositories(member['login'])
            if member_repositories:
                print(f'\nRepositories for {member["login"]}:')
                for repo in member_repositories:
                    print(f'-  {repo["name"]}')
            print('\n' + '-' * 30)


if __name__ == '__main__':
    main()
