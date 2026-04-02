import os
import requests

def fetch_trending_topics():
    api_key = os.getenv('NEWS_API_KEY')
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    response = requests.get(url).json()
    # Get the top 3 headlines
    return response.get('articles', [])[:3]

def generate_scripts(articles):
    with open('shorts_scripts.md', 'w') as f:
        f.write("# Today's Top 3 YouTube Shorts\n\n")
        for i, art in enumerate(articles, 1):
            title = art.get('title', 'No Title')
            desc = art.get('description', 'No details available.')
            
            f.write(f"### Short {i}: {title}\n")
            f.write(f"**Hook:** Did you hear about this? {title[:50]}...\n")
            f.write(f"**Body:** {desc}\n")
            f.write(f"**CTA:** Like if you're surprised by this! #shorts\n\n")
            f.write("---\n\n")

if __name__ == "__main__":
    news = fetch_trending_topics()
    generate_scripts(news)
