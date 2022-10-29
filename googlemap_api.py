import requests

place = input("검색할 장소 : ")
api = "AIzaSyBMY5NVUSAF1fhgBIqvrBayqLiVjiJeYrQ"

#url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input="+str(place)+"&inputtype=textquery&fields=formatted_address%2Cname%2Crating%2Copening_hours%2Cgeometry&key="+str(api)
url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input="+ str(place) + "&inputtype=textquery&fields=name,formatted_address,rating,opening_hours,geometry,business_status,photos,place_id,price_level,user_ratings_total" + "&key=" +str(api) 

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)