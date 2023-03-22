import requests

# Replace the placeholders with your own Instagram access token and the username of the target account
access_token = 'IGQVJXUXRVdnZALZAjJ3aHFZAZAFUzR290WjkwOV8xSEFCR2JfNjloOHJidExnakZAiM2d1cUs4cnlHYkdaX091UWlGQm1wWkZAxS0dqUThnc0pMOWxWaUQ5NHNQWTFYY3duUkYteUFZAdUthT194eU9qWUlMVgZDZD'
target_username = ''
# Make a GET request to the /username/follows endpoint
response = requests.get(f'https://graph.instagram.com/{target_username}/following?access_token={access_token}')

# Extract the list of users from the response JSON
users = response.json().get('data', [])
u = 'aristotle_aletheia'
print(f"{target_username} is following {len(users)} users:")
for user in users:
    print(user['username'])