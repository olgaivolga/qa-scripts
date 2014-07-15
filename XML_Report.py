#!/usr/bin/env python

import xml.etree.ElementTree as ET

"""
The script can be used to output test results in JUnit-compatible format.
Data in main() is for test purposes.
"""

class XML_Report:

    def __init__(self, suite, cases, filename="./result.xml"):
        self.suite = suite
        self.cases = cases
        self.filename = filename 
        self.build_xml()

    def build_xml(self):

        root = ET.Element("testsuites")
        testsuite = ET.SubElement(root, "testsuite")
        testsuite.set("name", self.suite['name'])
        testsuite.set("tests", str(len(self.cases)))
        for case in self.cases: 
            testcase = ET.SubElement(testsuite, "testcase")
            testcase.set("name", case['name'])
            if case['failure']:
                failure = ET.SubElement(testcase, "failure")
                failure.text = case['failure']
            if case['time']:
                testcase.set("time", case['time'])
        tree = ET.ElementTree(root)
        tree.write(self.filename)

def main():
    suite = {'name': 'Test suite name'}
    cases = [{'name': 'test1', 'failure': '', 'time': '0'}, {'name': 'test2', 'failure': 'something happened!', 'time': ''}]

    myxml = XML_Report(suite, cases, "./result.xml")

if __name__ == '__main__':
    main()

