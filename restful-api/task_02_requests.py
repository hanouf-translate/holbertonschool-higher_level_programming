#!/usr/bin/python3
"""
Module to fetch and process posts from JSONPlaceholder API
using the requests library and csv module.
"""

import csv
import requests


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder, prints the status code,
    and prints the titles of all the posts if successful.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    print("Status Code: {}".format(response.status_code))
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder, filters/structures them
    into a list of dictionaries (id, title, body), and saves them
    into a CSV file named posts.csv.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        
        # Structure data into a list of dictionaries with specific keys
        structured_posts = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]
        
        # Write to posts.csv using csv.DictWriter
        filename = "posts.csv"
        fieldnames = ["id", "title", "body"]
        
        try:
            with open(filename, mode="w", encoding="utf-8", newline="") as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for post in structured_posts:
                    writer.writerow(post)
        except IOError:
            print("I/O error while writing to {}".format(filename))