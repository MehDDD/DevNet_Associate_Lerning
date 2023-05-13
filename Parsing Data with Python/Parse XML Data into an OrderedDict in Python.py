import xmltodict

#Get the XML data
stream = stream = open(r'C:\Users\Mahdi\Desktop\DevNet Associate\DevNet_Associate_Lerning\XML_JSON_YAML_Data Formats\XML Example 2.xml')

#Parse the XML file into an 'OrderedDict'
xml = xmltodict.parse(stream.read())

for e in xml ["People"]["Person"]:
    print(e)
