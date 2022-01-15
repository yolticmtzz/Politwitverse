import tweepy
import time
import json
import re
from re import search

def hydrate_context(jj): #accepts tweet.annotations and returns a list of annotations, domain ids and entitity ids

    z = 0
    a = 1

    # print(c[0])
    # print(c[1])
    # print(len(c))
    c={}
    c = jj

    c = makeitastring(jj)

    context15 = c.replace('"', '')
    context16 = context15.replace("'", "")
    context17 = context16.replace("{", "")
    context18 = context17.replace("}", "")
    context19 = context18.replace("(", "")
    context20 = context19.replace("'", "")
    context21 = context20.replace("id':", "")
    context215 = context21.replace("domain:", "")
    context22 = context215.replace("}}", ',')

    context2 = context21.split(",")
    [print(x) for x in context2]
    context_list = []
    domain_list = []
    entity_list = []
    final_list = []
    i=0
    while i < len(context2):
        temp_context = context2[i]
        if search("Entit", temp_context):
            temp_context = ""
        if search("Entit", temp_context):
            temp_context = ""
        if search("Nelson", temp_context):
            temp_context = ""
        if search(("name: "), temp_context):
            temp_context2 = temp_context.replace("name: ", "")
            context_list.append(temp_context2.strip())
        if search("description: ", temp_context):
            temp_context2 = temp_context.replace("description: ", "")
            context_list.append(temp_context2.strip())
        if search("like ", temp_context):
            temp_context2 = temp_context.replace("like ", "")
            context_list.append(temp_context2.strip())
        if search("domain: id", temp_context):
            temp_context2 = temp_context.replace("domain: id:", ",") #see if by changing variables from context2 to something different in each
            #print(temp_context2 + '- domain')
            domain_list.append(temp_context2.strip())
        if search("entity: id", temp_context):
            temp_context2 = temp_context.replace("entity: id:", ",")
            entity_list.append(temp_context2.strip())
        i=i+1
    z=z+1
    a=a+1
    
    context_list = list(set(context_list))  
  # print(context_list)
    domain_list = list(set(domain_list)) 
  # print(domain_list)
    entity_list = list(set(entity_list)) 
  # print(entity_list)
    final_list.append(context_list)
    final_list.append(domain_list)
    final_list.append(entity_list)
  
    return(final_list)


def mention_hydrate(entity_list):  
  x = 0 #list index
  i = 1 #list length
  container = []
  entity_length = len(entity_list)
  while i <= entity_length:
      temp_list = entity_list[x]
      j = temp_list.get("username")
      container.append(j)
      i = i + 1
      x = x + 1   
  return container


def makeitastring(wannabestring):
  convertedstring = ''.join(map(str, wannabestring))
  return(convertedstring)

       


#entity_list = [{'start': 208, 'end': 220, 'username': 'NitishKumar', 'id': '143409075'}, {'start': 221, 'end': 232, 'username': 'BsebResult', 'id': '1225054380421812224'}, {'start': 233, 'end': 249, 'username': 'BiharHealthDept', 'id': '1135503797025828864'}, {'start': 251, 'end': 260, 'username': 'abpbihar', 'id': '1267754185837015042'}]

entity_list =[{'domain': {'id': '10', 'name': 'Person', 'description': 'Named people in the world like Nelson Mandela'}, 'entity': {'id': '981251388607885312', 'name': 'Jason Smith', 'description': 'US Representative Jason Smith (MO-08)'}}, {'domain': {'id': '35', 'name': 'Politician', 'description': 'Politicians in the world, like Joe Biden'}, 'entity': {'id': '981251388607885312', 'name': 'Jason Smith', 'description': 'US Representative Jason Smith (MO-08)'}}]


hh = hydrate_context(entity_list)
print(hh)
