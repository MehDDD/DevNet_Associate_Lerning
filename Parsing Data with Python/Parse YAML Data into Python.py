import yaml
from yaml import load, load_all

stream = open(r'C:\Users\Mahdi\Desktop\DevNet Associate\DevNet_Associate_Lerning\XML_JSON_YAML_Data Formats\yaml sample.yaml')
doc = load_all(stream, Loader=yaml.FullLoader)

for e in doc:
    print(type(e))
    print(e['people'][1]['FN'])