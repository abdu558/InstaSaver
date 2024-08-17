import requests

url = "https://instagram-scraper-api2.p.rapidapi.com/v1/post_info"

querystring = {"code_or_id_or_url":"https://www.instagram.com/p/C75N_NLupk_/","include_insights":"true"}

headers = {
	"x-rapidapi-key": "0e6b7eff56mshb50e42308ba3309p1a4e23jsnd6045b91d1f3",
	"x-rapidapi-host": "instagram-scraper-api2.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json()['data']['video_url'])