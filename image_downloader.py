import os
from urllib.parse import urlparse
from tqdm import tqdm
import requests

def download_image(url, destination_dir):
    """Downloads an image from the specified URL and saves it to the destination directory.

    Args:
        url (str): The URL of the image to download.
        destination_dir (str): The directory where the image will be saved.
    """

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        filename = urlparse(url).path.split('/')[-1]
        file_path = os.path.join(destination_dir, filename)

        with open(file_path, 'wb') as f:
            total_size = int(response.headers.get('content-length', 0))
            with tqdm(total=total_size, unit='B', unit_scale=True, desc=filename) as progress_bar:
                for chunk in response.iter_content(chunk_size=1024):
                    progress_bar.update(len(chunk))
                    f.write(chunk)

        print(f"Image downloaded successfully: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")

def main():
    """Main function for the image downloader."""

    destination_dir = input("Enter the destination directory: ")
    os.makedirs(destination_dir, exist_ok=True)

    while True:
        urls = input("Enter one or more URLs (separated by spaces): ")
        if not urls:
            break

        for url in urls.split():
            download_image(url, destination_dir)

if __name__ == "__main__":
    main()

# Add an empty line here    