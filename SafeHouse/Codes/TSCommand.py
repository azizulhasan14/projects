import urllib.request
import requests



# Define a function that will post on server every 15 Seconds

def thingspeak_write_c(arm,lock,cam,buzz,move,flame, key):
    isArmed = arm
    isLocked = lock
    isCamera = cam
    isBuzzer = buzz
    isMotion = move
    isFlame = flame
    URl='https://api.thingspeak.com/update?api_key='
    KEY= key
    HEADER='&field1={}&field2={}&field3={}&field4={}&field5={}&field6={}'.format(isArmed,isLocked,isCamera,isBuzzer,isMotion, isFlame)
    NEW_URL=URl+KEY+HEADER
    data=urllib.request.urlopen(NEW_URL)
    return 1
    

def thingspeak_read_c(key:str, id_num:str):
    URL='https://api.thingspeak.com/channels/'+id_num+'/feeds.json?api_key='
    KEY= key
    HEADER='&results=1'
    NEW_URL=URL+KEY+HEADER

    get_data=requests.get(NEW_URL).json()

    data=get_data['feeds']

    t=[]
    for x in data:
        t.append(x['field1'])
        t.append(x['field2'])
        t.append(x['field3'])
        t.append(x['field4'])
        t.append(x['field5'])               
        t.append(x['field6'])                       
    return t
