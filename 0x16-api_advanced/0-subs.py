#!/usr/bin/python3
"""A function that queries the Reddit API and
returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "python:0x16_api_advanced:v1.0.0 (by /u/Accomplished-Rich709)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    limit = "Rate limit exceeded. Waiting..."
    forbidden = 1
    if response.status_code == 429:  # Rate limit exceeded
            return limit  
    elif response.status_code == 403:  # Forbidden
            return forbidden    
    #elif response.status_code != 200:
     #   return response.status_code

    data = response.json().get("data")
    num_subs = data.get("subscribers")

    return num_subs
