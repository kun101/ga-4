import requests

# Optional: Add your GitHub Personal Access Token here to increase rate limit
GITHUB_TOKEN = None  # Replace or leave as None
HEADERS = {'Authorization': f'token {GITHUB_TOKEN}'} if GITHUB_TOKEN else {}

def get_newest_github_user(location, min_followers):
    base_url = 'https://api.github.com/search/users'
    query = f'location:{location} followers:>{min_followers}'
    params = {
        'q': query,
        'sort': 'joined',
        'order': 'desc',
        'per_page': 1  # only need the newest
    }

    print("🔍 Searching GitHub users...")
    response = requests.get(base_url, headers=HEADERS, params=params)
    response.raise_for_status()

    users = response.json().get('items', [])
    if not users:
        print(f"No users found in {location} with >{min_followers} followers.")
        return

    newest_user = users[0]['login']
    print(f"👤 Newest user found: {newest_user}")

    # Fetch full profile to get the account creation date
    user_url = f"https://api.github.com/users/{newest_user}"
    user_response = requests.get(user_url, headers=HEADERS)
    user_response.raise_for_status()

    created_at = user_response.json()['created_at']
    print(f"🗓️ Account created at: {created_at} (ISO 8601)")
    return created_at

# Run for Dublin with >140 followers
if __name__ == "__main__":
    creation_date = get_newest_github_user('Dublin', 140)
