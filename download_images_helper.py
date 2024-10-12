import os
import time
import requests
from urllib.parse import urlparse

def download_images(image_urls, download_folder, delay=1):
    """
    Downloads images from given URLs and saves them to the specified folder.

    Args:
        image_urls (list): List of image URLs.
        download_folder (str): Folder where images will be saved.
        delay (int): Delay in seconds between each download.
    """
    # Create the download folder if it doesn't exist
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # Loop through all image URLs
    for url in image_urls:
        try:
            # Get the image file name from the URL
            parsed_url = urlparse(url)
            file_name = os.path.basename(parsed_url.path)

            # Full path to save the file
            file_path = os.path.join(download_folder, file_name)

            # Download the image
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open(file_path, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                print(f"Downloaded {file_name}")
            else:
                print(f"Failed to download {file_name}, status code: {response.status_code}")

            # Wait for the specified delay before downloading the next image
            time.sleep(delay)

        except Exception as e:
            print(f"An error occurred while downloading {file_name}: {e}")

final_list=[]
print(final_list, len(final_list))
