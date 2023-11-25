import asyncio

import httpx


async def yubanGPTReply(text,id=None):
    if id!=None:
        url="https://ybapi.cn/API/gpt.php?type=1&msg="+text+"&id="+id
    else:
        url="https://ybapi.cn/API/gpt.php?type=1&msg="+text
    async with httpx.AsyncClient(timeout=100) as client: #100s超时
        r = await client.get(url)  #发起请求
        return r.json().get("text"), r.json().get("id")  #返回结果
if __name__ == '__main__':
    id=None
    while True:
        text=input("textHere:")
        print(id)
        text1,id1=asyncio.run(yubanGPTReply(text,id))
        if id==None:
            id=id1
        print(text1)