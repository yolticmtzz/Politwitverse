import re
from learning import makeitastring
import ast


annotations = "{'start': 119, 'end': 125, 'probability': 0.8328, 'type': 'Person', 'normalized_text': 'Gorsuch'}"

print(annotations)
annotations15 = makeitastring(annotations)
annotations16 = annotations15.replace("'", '"')
print(annotations16)
anndict = ast.literal_eval(annotations16)
#anndict = dict(item.split(":") for item in annotations15.split(", "))
#print(annotations)
#annotations3 = re.split(': |, |\*|\n',annotations25)
#print(anndict)

print(anndict)
print(anndict.keys())

dict = {'Name': 'Zara', 'Age': 7}
print(dict)
print(dict.keys())
print(dict.get('Age'))
print(anndict.get('type'))





