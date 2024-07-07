import requests

class AnimeMetadata:
    def __init__(self, anime_id):
        self.anime_id = anime_id
        self.title_jp = None
        self.title_en = None
        self.poster = None
        self.large_poster = None
        self.title_type = None
        self.airing = None
        self.score = None
        self.year = None
        self.genres = None
        self.fetch_metadata()

    def fetch_metadata(self):
        url = f'https://api.jikan.moe/v4/anime/{self.anime_id}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            self.title_jp = data.get('data', {}).get('title', 'N/A')
            self.title_en = data.get('data', {}).get('title_english', 'N/A')
            self.poster = data.get('data', {}).get('images', {}).get('jpg', {}).get('image_url', None)
            self.large_poster = data.get('data', {}).get('images', {}).get('jpg', {}).get('large_image_url', None)
            self.title_type = data.get('data', {}).get('type', None)
            self.airing = data.get('data', {}).get('airing', None)
            self.score = data.get('data', {}).get('score', None)
            self.year = data.get('data', {}).get('year', None)
            self.genres = [genre["name"] for genre in data.get('data', {}).get('genres', []) if "name" in genre]
        else:
            print("Failed to fetch data. Status code:", response.status_code)


        