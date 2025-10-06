import requests
import csv

def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder and prints the status code and titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
    else:
        print("Failed to fetch posts.")

def fetch_and_save_posts():
    """
    Fetches posts and saves them to a CSV file (posts.csv) with id, title, and body.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        # Extract only the required fields
        filtered_posts = [
            {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            for post in posts
        ]

        # Write to CSV
        with open("posts.csv", "w", newline='', encoding='utf-8') as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(filtered_posts)

    else:
        print("Failed to fetch posts for saving.")
