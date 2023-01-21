from PIL import Image, ImageDraw, ImageFont
import requests
from datetime import datetime
from pandas import DataFrame
import json
from datetime import datetime, timedelta
import time

def api():
    print("api!!!")
    clientID = "ff2d23662d806bc1a677c95b0a47aca2"
    slientSecret = "ff2d23662d806bc1a677c95b0a47aca25f99fe4ab213eca03b84866e2c6080a2dd98baf1"
    redirectURL = "https://ddukbaegi.tistory.com"
    code = "7439d2813534a225180fdfdf4ffd8e6852ddb0d685a4e213d55db7afba671e39ef08ff2f"
    accessToken="79a747a77bc6add4cdb80fe8c6e62e8d_131ff873a0e84eb868944d3bd0ab9051"
    url = "https://www.tistory.com/apis/category/list?access_token="+accessToken+"&output=json&blogName="+redirectURL

    url2 = "https://www.tistory.com/oauth/authorize?client_id=ff2d23662d806bc1a677c95b0a47aca2&redirect_uri=https://ddukbaegi.tistory.com/&response_type=code"
    url3 = "https://ddukbaegi.tistory.com/?code=7439d2813534a225180fdfdf4ffd8e6852ddb0d685a4e213d55db7afba671e39ef08ff2f&state="
    url4 = "GET https://www.tistory.com/oauth/access_token?client_id=ff2d23662d806bc1a677c95b0a47aca2&client_secret=ff2d23662d806bc1a677c95b0a47aca25f99fe4ab213eca03b84866e2c6080a2dd98baf1&redirect_uri=https://ddukbaegi.tistory.com/&code=7439d2813534a225180fdfdf4ffd8e6852ddb0d685a4e213d55db7afba671e39ef08ff2f&grant_type=authorization_code"

    categoryURL = "https://www.tistory.com/apis/category/list?access_token=79a747a77bc6add4cdb80fe8c6e62e8d_131ff873a0e84eb868944d3bd0ab9051&output=json&blogName=https://ddukbaegi.tistory.com"
    blogURL = "https://www.tistory.com/apis/post/list?access_token=79a747a77bc6add4cdb80fe8c6e62e8d_131ff873a0e84eb868944d3bd0ab9051&targetUrl=ddukbaegi&count=3&sort=id&output=json&page=1"

    jsikim1URL = "https://www.tistory.com/apis/post/list?access_token=" + accessToken + "&targetUrl=jsikim1&count=3&sort=id&output=json&page=1"

    res = requests.get(jsikim1URL)
    resDict = json.loads(res.text)
    resArr = resDict.get("tistory").get("item").get("posts")
    print(resArr)
    list = []
    for i in resArr:
        listOne = []

        listOne.append(i.get("title"))
        listOne.append(i.get("postUrl"))

        date = i.get("date")
        strtime = "%Y-%m-%d %H:%M:%S"
        blogtime = datetime.strptime(date, strtime)
        blogDate = datetime.strftime(blogtime, '%Y.%m.%d')
        listOne.append(blogDate)

        now = datetime.now()
        pastDate = (now-blogtime).days
        if(pastDate > 7):
            pastDate = pastDate // 7
            pastStr = str(pastDate) + "주 전"            
        else :
            pastStr = str(pastDate) + "일 전"
        listOne.append(pastStr)        
        
        list.append(listOne)

        print("listOne : " , listOne)
    print("list : " , list)

    return list

    
