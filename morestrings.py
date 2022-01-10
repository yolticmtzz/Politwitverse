import ast
import re
from learning import makeitastring
import tweepy
from collections import defaultdict
import time
import json
import re
import pickle
import ast


def makeitastring(wannabestring):
  convertedstring = ''.join(map(str, wannabestring))
  return(convertedstring)

def convert_list_to_dict(test_list):
    list_soup_dict = {}
    x = 0 #list index
    i = 1 #list length
    list_soup_length = (len(list_soup))
    while i <= list_soup_length:
        list_soupt[0] = makeitastring(list_soup)
        list_soup[0] = list_soup[x].replace("'", '"')
        list_soup[0] = anndict = ast.literal_eval(list_soup[0])
        i = i + 1
        x = x + 1
        while i <= list_soup_length:
           list_soup[x] = makeitastring(list_soup)
           list_soup[x] = list_soup[x].replace("'", '"')
           list_soup[x] = anndict = ast.literal_eval(list_soup[x])
           list_soup[0] = list_soup[0] | list_soup[x]
    list_soup_final = list_soup[0]
    return list_soup_final
       


test_list = [{'start': 208, 'end': 220, 'username': 'NitishKumar', 'id': '143409075'}, {'start': 221, 'end': 232, 'username': 'BsebResult', 'id': '1225054380421812224'}, {'start': 233, 'end': 249, 'username': 'BiharHealthDept', 'id': '1135503797025828864'}, {'start': 251, 'end': 260, 'username': 'abpbihar', 'id': '1267754185837015042'}]

hh = convert_list_to_dict(test_list)
print(hh)