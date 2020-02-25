#!/usr/bin/env python3
import xml.etree.ElementTree as ET
file = "members.rdf"
tree = ET.parse(file)
root = tree.getroot()
NS = {'rdf' : 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
      'rdfs' : 'http://www.w3.org/2000/01/rdf-schema#',
      'dc' : 'http://purl.org/dc/elements/1.1/',
      'dcterms' : 'http://purl.org/dc/terms/',
      'foaf' : 'http://xmlns.com/foaf/0.1/',
      'v' : 'http://www.w3.org/2006/vcard/ns#',
      'cinii' : 'http://ci.nii.ac.jp/ns/1.0/'}

records = root.findall("./foaf:Organization", NS)
for record in records:
 
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

    # alternative
    alternative = record.find("./dcterms:alternative", NS)
    print(alternative.text, end="")
    print("\t", end="")

    # alternative
    alternatives = record.findall("./dcterms:alternative", NS)
    allalternatives = []
    if len(alternatives) > 1:
        for  lternative in alternatives[1:]:
            allalternatives.append(alternative.text)
        print("|".join(allalternatives), end="")
    print("\t", end="")

    # memberid
    memberid = record.find("./cinii:memberid", NS)
    print(memberid.text, end="")
    print("\t", end="")

    # organizationid
    organizationid = record.find("./cinii:organizationid", NS)
    print(organizationid.text, end="")
    print("\t", end="")

    # prefcode
    prefcode = record.find("./cinii:prefcode", NS)
    print(prefcode.text, end="")
    print("\t", end="")

    # catflag
    #catflag = record.find("./cinii:catflag", NS)
    #if	ET.iselement(catflag):
    #    print(catflag.text, end="")
    #print("\t", end="")

    # illflag
    #illflag = record.find("./cinii:illflag", NS)
    #if	ET.iselement(illflag):
    #    print(illflag.text, end="")
    #print("\t", end="")

    # copyservice
    #copyservice = record.find("./cinii:copyservice", NS)
    #if	ET.iselement(copyservice):
    #    print(copyservice.text, end="")
    #print("\t", end="")

    # next record
    print()
