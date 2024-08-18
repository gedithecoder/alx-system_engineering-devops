#!/usr/bin/python3
"""A function that queries the Reddit API and
returns the number of subscribers"""

import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """

    user_agent = "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"  # Replace with your custom User-Agent
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": user_agent}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for error HTTP statuses

        data = response.json()
        return data['data']['subscribers']
    except (requests.exceptions.RequestException, KeyError, ValueError):
        return 0
