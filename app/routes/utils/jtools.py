import requests

def preload_anime_details(anime_id):
    url = f'https://api.jikan.moe/v4/anime/{anime_id}/full'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        title_english = data.get('data', {}).get('title_english', 'N/A')
        large_image_url = data.get('data', {}).get('images', {}).get('jpg', {}).get('large_image_url', 'N/A')
        return [title_english, large_image_url]
    else:
        return [None, None]
