import requests
from bs4 import BeautifulSoup
import time
import os

# Specify the path to your text file
file_path = 'page.txt'

# API details
api_url = "https://instagram-scraper-api2.p.rapidapi.com/v1/post_info"
api_key = "0e6b7eff56mshb50e42308ba3309p1a4e23jsnd6045b91d1f3"  # Replace with your actual API key

def get_links(file_path):
    with open(file_path, 'r') as file:
        file_contents = file.read()

    soup = BeautifulSoup(file_contents, features="html.parser")
    urls = []
    for a in soup.find_all('a', href=True):
        href_value = a['href']
        if href_value.startswith('/p/'):
            urls.append('https://www.instagram.com' + href_value)

    return urls

def download_video(url, num):
    querystring = {"code_or_id_or_url": url, "include_insights": "true"}
    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "instagram-scraper-api2.p.rapidapi.com"
    }

    try:
        response = requests.get(api_url, headers=headers, params=querystring)
        response.raise_for_status()
        data = response.json()

        # Extract video URL from the JSON response
        video_url = data['data']['video_url']

        # Download the video
        video_response = requests.get(video_url, stream=True)
        video_response.raise_for_status()

        os.makedirs('media', exist_ok=True)
        with open(f'media/{num}.mp4', 'wb') as f_out:
            for chunk in video_response.iter_content(chunk_size=8192):
                if chunk:
                    f_out.write(chunk)

        print(f"Downloaded {num + 1}: {url}")

    except requests.exceptions.RequestException as e:
        print(f"Error while processing {url}: {str(e)}")
    except KeyError as e:
        print(f"Error extracting video URL for {url}: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred for {url}: {str(e)}")

def main():
    urls = get_links(file_path)
    print(f"Total URLs to process: {len(urls)}")

    for num, url in enumerate(urls):
        download_video(url, num)
        time.sleep(1)  # Add a delay to avoid overwhelming the API

if __name__ == "__main__":
    main()