import requests
from bs4 import BeautifulSoup
import time

# Specify the path to your text file
file_path = 'page.txt'

# Initialize an empty variable to store the file contents
file_contents = ""

def get_links(file_path):
    # Open the file and read its contents
    with open(file_path, 'r') as file:
        file_contents = file.read()

    soup = BeautifulSoup(file_contents, features="html.parser")
    urls = []
    for a in soup.find_all('a', href=True):
        href_value = a['href']
        if href_value.startswith('/p/'):
            urls.append('www.instagram.com' + href_value)

    return urls

def download_links(urls):
    print(f"Total URLs to download: {len(urls)}")
    for num, post_link in enumerate(urls):
        url = f"http://localhost:3000/api/video?url=https://{post_link}"

        # Try to download the video and handle exceptions
        try:
            response = requests.get(url)
            response.raise_for_status()  # Check for HTTP request errors

            video_url = response.json()['data']['videoUrl']

            headers = {
                'User-Agent': 'Your User-Agent String',
            }

            with open(f'media/{num+115}.mp4', 'wb') as f_out:
                r = requests.get(video_url, headers=headers, stream=True)
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f_out.write(chunk)

            print(f"Downloaded {num + 1}/{len(urls)}: {post_link}")

        except requests.exceptions.RequestException as e:
            print(f"Error while downloading {post_link}: {str(e)}")
        except Exception as e:
            print(f"An unexpected error occurred for {post_link}: {str(e)}")

        # Implement a delay to avoid overwhelming the server
        #time.sleep(0.1)

def main():
    download_links(get_links(file_path))

if __name__ == "__main__":
    main()
