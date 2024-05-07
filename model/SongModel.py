import json

import requests


class SongsModel:
    def __init__(self, base_url="https://localhost:44346/api/Songs"):
        self.base_url = base_url

    def get_songs(self, search=None):
        """Retrieve songs with optional search query."""
        url = f"{self.base_url}"
        if search is not None:
            url = f"{url}?search={search}"
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            return response.text

    def add_song(self, song_data):
        """Add a new song."""
        response = requests.post(f"{self.base_url}/AddTrack", json=song_data, verify=False)
        if response.status_code in [200, 201]:
            j = json.loads(response.content.decode('utf-8'))
            return f"Added, Maybe you will like {j['recomendedSong'].split(',')[0]} by {j['recomendedSong'].split(',')[1]}"
        else:
            return "Failed to add song"

    def update_song(self, song_id, song_data):
        """Update an existing song."""
        response = requests.put(f"{self.base_url}/{song_id}", json=song_data, verify=False)
        if response.status_code == 204:
            return "Song updated successfully"
        else:
            return response.text

    def delete_song(self, song_id):
        """Delete a song."""
        print(f"{self.base_url}/api/Songs/{song_id}")
        response = requests.delete(f"{self.base_url}/{song_id}", verify=False)
        if response.status_code == 204:
            return "Song deleted successfully"
        else:
            return response.text

