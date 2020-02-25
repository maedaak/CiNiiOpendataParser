#!/usr/bin/env python3
import xml.etree.ElementTree as ET
file = "names.rdf"
tree = ET.parse(file)
root = tree.getroot()
NS = {'rdf' : 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
      'rdfs' : 'http://www.w3.org/2000/01/rdf-schema#',
      'owl' : 'http://www.w3.org/2002/07/owl#',
      'dc' : 'http://purl.org/dc/elements/1.1/',
      'dcterms' : 'http://purl.org/dc/terms/',
      'foaf' : 'http://xmlns.com/foaf/0.1/',
      'cinii' : 'http://ci.nii.ac.jp/ns/1.0/'}

records = root.findall("./rdf:Description", NS)
for record in records:
    # authorid 
    authorid = record.find("./cinii:authorid", NS)
    print(authorid.text, end="")
    print("\t", end="")

    # rdf:type resource
    type = record.find("./rdf:type", NS)
    rdfresource = '{' + NS['rdf'] + '}' + 'resource'
    print(type.attrib[rdfresource], end="")
    print("\t", end="")
 
    # name
    name = record.find("./foaf:name", NS)
    print(name.text, end="")
    print("\t", end="")

    # name
    names = record.findall("./foaf:name", NS)
    allname = []
    if len(names) > 1:
        for name in names[1:]:
            allname.append(name.text)
        print("|".join(allname), end="")
    print("\t", end="")

    # givenName
    givenName = record.find("./foaf:givenName", NS)
    if ET.iselement(givenName):
        print(givenName.text, end="")
    print("\t", end="")

    # middleName
    middleName = record.find("./foaf:middleName", NS)
    if ET.iselement(middleName):
        print(middelName.text, end="")
    print("\t", end="")

    # familyName
    familyName = record.find("./foaf:familyName", NS)
    if ET.iselement(familyName):
        print(familyName.text, end="")
    print("\t", end="")

    # alternative
    alternative = record.find("./dcterms:alternative", NS)
    if ET.iselement(alternative):
        print(alternative.text, end="")
    print("\t", end="")

    # next record
    print()
