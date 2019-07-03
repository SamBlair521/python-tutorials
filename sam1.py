# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import datetime
import requests

r = requests.get('https://raw.githubusercontent.com/becloudready/snowflake-tutorials/master/dataset/employees01.csv')

listdata3 = r.text.split('\n')

listdata3[1]

f=open('C:/Users/Sam/sam_python.txt', 'w')

f.write(listdata3[1])
f.close()



url = "https://s3.console.aws.amazon.com/s3/object/deckerblair/sam_python.csv"

payload = "Hello World"
headers = {
    'X-Amz-Content-Sha256': "a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e",
    'Host': "s3.console.aws.amazon.com",
    'X-Amz-Date': "20190703T193739Z",
    'Authorization': "AWS4-HMAC-SHA256 Credential=AKIAYQR72GMA3HNHLTNS/20190703/us-east-2/s3/aws4_request, SignedHeaders=host;x-amz-content-sha256;x-amz-date, Signature=0f0e3fbad45aeccda0b3b7486d9c46dc0ce09b49b3d24ad16cbadce0bd4442a8",
    'Content-Type': "text/plain",
    'User-Agent': "PostmanRuntime/7.15.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "d78e6e6e-d78a-43d4-a591-d97fc87b6936,b493f90e-999b-4e43-a7f4-c802734bce3c",
    'cookie': "awsc-authTimer=%7B%22start%22%3A%221562182411296%22%7D; JSESSIONID=F2D8810E94425964BAF5D18658BAADC9",
    'accept-encoding': "gzip, deflate",
    'content-length': "11",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)


now = datetime.date.today()

now.strftime('%d/%m/%Y')



 
