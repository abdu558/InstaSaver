import urllib.request
from bs4 import BeautifulSoup

# urllib.request.urlretrieve('https://scontent.cdninstagram.com/v/t66.30100-16/163617479_262427090189979_4123765007146491502_n.mp4?_nc_ht=scontent.cdninstagram.com&_nc_cat=103&_nc_ohc=7MfIToM6A28AX8Rp9Zi&edm=APs17CUBAAAA&ccb=7-5&oh=00_AfAQ8dWi6fJqhNvePmVx5lID0FJDn5SORg5RFTM_EfCVtA&oe=65982D0A&_nc_sid=10d13b', 'video_name.mp4') 
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
        name = str(num+115)+'.mp4'
        urllib.request.urlretrieve(post_link, name) 

def main():
    download_links(get_links(file_path))

if __name__ == "__main__":
    main()


        # urllib.request.urlretrieve(post_link, name) 
#use this on the websites cdn.