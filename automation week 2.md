# Week two automation 

I wanted to automate away of accessing the names and emails of all my group members in 23W-GBAC .

# First 

In my pycharm  installed requests using pip . By clicking pip install requests . Then boom and i generated the code as it flows . I also used the github api as the url to make the code to happen

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
        
# Second 

I inseted the organisation and i gave the code my access token for my git hub account


organization_name = '23W-GBAC'

github_access_token = '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'

members = get_github_members(organization_name, github_access_token)
# Third 


This is where problems came in because at the start of the automation i wanted acode to help generate the user names and email addresses of all the members in the same group but little did i know that is against the privacy terms of Github
so my code had to change from displaying that data to only displaying the user names .At first the code had to display the names and email addresses but due to privacy terms i change the code to display email not available
and now its only displays the user names but with no email address to these email addresses.


if members:

    for member in members:
    
        username = member['login']
        
        email = member.get('email', 'Email not available')
        
        print(f"Username: {username}, Email: {email}")
