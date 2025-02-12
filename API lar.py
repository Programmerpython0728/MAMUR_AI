import requests

url = "https://open-ai21.p.rapidapi.com/conversationllama"

payload = {
	"messages": [
		{
			"role": "user",
			"content": "hello"
		}
	],
	"web_access": False
}
headers = {
	"x-rapidapi-key": "4893157a12mshe49c07deb8f4483p1757dejsnea57e7ec3428",
	"x-rapidapi-host": "open-ai21.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())