
import requests

#initialze params
token="" #configure token to be obtained in telegram
chatid="" #configure chatID to be obtained in telegram

http_proxy  = "http://ip:port"   #configure IP and ports
https_proxy = "http://ip:port"   #configure IP and ports
proxyDict = { 
              "http"  : http_proxy, 
              "https" : https_proxy              
            }

def telegram_bot_sendmessage(bot_message):  
  url = "https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+chatid+"&text="+bot_message
  response = requests.get(url, proxies=proxyDict)    #take out second parameter if no proxy is required
  return response.json
    

testmesssage = telegram_bot_sendmessage("Send this message from Python")
print(testmesssage)

