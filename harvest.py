#!/usr/bin/env python
import json
import requests


def getArtworkIds(entityRoot):
    httpReq= r'http://wdq.wmflabs.org/api?q=claim[31:%28tree['+str(entityRoot)+r'][][279]%29]'
    print(httpReq)
    req = requests.get(httpReq)
    return req

def getEntityProperties(entityId):
    httpReq=r'http://www.wikidata.org/w/api.php?action=wbgetentities&ids=q'+str(entityId)+r'&format=json'
    print(httpReq)
    req = requests.get(httpReq)
    return req

def getLabelsFromJson(js, prefixChar="Q"):
    return js["entities"][prefixChar+str(i)]['aliases'] 

def getClaimsFromJson(js, prefixChar="Q"):
    return js["entities"][prefixChar+str(i)]['claims'] 

artId = 17514
x = getArtworkIds(artId).json()["items"]
for i in x:
    y = getEntityProperties(i)
    print(y.json().keys())
    for prop in [31,135]:
        propDict = getClaimsFromJson(y.json())
        propStr = 'P'+str(prop)
        if(propStr in propDict):
            print(propDict[propStr][0]['mainsnak']['datavalue']['value']['numeric-id'])
