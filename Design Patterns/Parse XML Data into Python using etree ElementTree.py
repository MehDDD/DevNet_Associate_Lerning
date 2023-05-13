import xml.etree.ElementTree as ET

#Get the XML file data
stream = open('XML Example 2.xml' , 'r')

#Parse the data into an ElementTree object
xml = ET.parse(stream)

#Get the 'root' Element object from the ElementTree
root = xml.getroot()

#Iterate through each child of the root Element
for e in root:
    #Print the stringified version of the element
    print(ET.tostring(e))
    print("")

    #Print the 'ID' attribute of the Element object
    print(e.get("Id"))