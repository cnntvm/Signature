import os
import sys
import urllib.request
client_id = "TyUJq4JYV_MSWlC1lTno"
client_secret = "gRpMFS1SnB"
search_text = input("검색할 단어는? :")
encText = urllib.parse.quote(search_text)
url =  "https://openapi.naver.com/v1/search/local?query=" + encText +"&display=5&sort=comment"# JSON 결과
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)