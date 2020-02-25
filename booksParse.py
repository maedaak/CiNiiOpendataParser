#!/usr/bin/env python3
import xml.etree.ElementTree as ET
file = "books.rdf"
tree = ET.parse(file)
root = tree.getroot()
NS = {'rdf' : 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
      'rdfs' : 'http://www.w3.org/2000/01/rdf-schema#',
      'owl' : 'http://www.w3.org/2002/07/owl#',
      'dc' : 'http://purl.org/dc/elements/1.1/',
      'dcterms' : 'http://purl.org/dc/terms/',
      'foaf' : 'http://xmlns.com/foaf/0.1/',
      'prism' : 'http://prismstandard.org/namespaces/basic/2.0/',
      'bibo' : 'http://prismstandard.org/namespaces/basic/2.0/',
      'cinii' : 'http://ci.nii.ac.jp/ns/1.0/'}

records = root.findall("./rdf:Description", NS)
for record in records:
    # title
    title = record.find("./dc:title", NS)
    if ET.iselement(title):
        print(title.text, end="")
        print("\t", end="")

        # alternative
        alternative = record.find("./dcterms:alternative", NS)
        if ET.iselement(alternative):
            print(alternative.text, end="")
        print("\t", end="")

        # creator
        creator = record.find("./dc:creator", NS)
        if ET.iselement(creator):
            print(creator.text, end="")
        print("\t", end="")

        # publisher
        publisher = record.find("./dc:publisher", NS)
        if ET.iselement(publisher):
            print(publisher.text, end="")
        print("\t", end="")

        # language
        language = record.find("./dc:language", NS)
        if ET.iselement(language):
            print(language.text, end="")
        print("\t", end="")

        # topic
        topic = record.find("./foaf:topic", NS)
        if ET.iselement(topic):
            print(topic.text, end="")
        print("\t", end="")

        # ncid
        ncid = record.find("./cinii:ncid", NS)
        if ET.iselement(ncid):
            print(ncid.text, end="")
        print("\t", end="")

        # edition
        edition = record.find("./prism:edition", NS)
        if ET.iselement(edition):
            print(edition.text, end="")
        print("\t", end="")

        # extent
        extent = record.find("./dcterms:extent", NS)
        if ET.iselement(extent):
            print(extent.text, end="")
        print("\t", end="")

        # size
        size = record.find("./cinii:size", NS)
        if ET.iselement(size):
            print(size.text, end="")
        print("\t", end="")

        # ownerCount
        ownerCount = record.find("./cinii:ownerCount", NS)
        if ET.iselement(ownerCount):
            print(ownerCount.text, end="")
        print("\t", end="")

        # publicationDate
        publicationDate = record.find("./prism:publicationDate", NS)
        if ET.iselement(publicationDate):
            print(publicationDate.text, end="")
        print("\t", end="")

        # note
        note = record.find("./cinii:note", NS)
        if ET.iselement(note):
            print(note.text, end="")
        print("\t", end="")

        # subject
        subject = record.find("./dc:subject", NS)
        if ET.iselement(subject):
           print(subject.text, end="")
        print("\t", end="")

        print()

