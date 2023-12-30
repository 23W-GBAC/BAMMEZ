import requests


def get_github_members(org_name, access_token):
    url = f'https://api.github.com/orgs/{org_name}/members'
    headers = {'Authorization': f'token {access_token}'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        members = response.json()
        return members
    else:
        print(f"Error: {response.status_code}")
        return None


# Replace 'your_organization' and 'your_access_token' with your actual organization name and GitHub access token
organization_name = '23W-GBAC'
github_access_token = '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'

members = get_github_members(organization_name, github_access_token)

if members:
    for member in members:
        username = member['login']
        email = member.get('email', 'Email not available')
        print(f"Username: {username}, Email: {email}")
