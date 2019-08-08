# -*- encoding: utf-8 -*-
"""
@Author  : QADai
@Email   : daibiao83@126.com
"""
import os
import xml.etree.ElementTree as ET

def modify_text(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    for neighbor in root.iter('name'):
        neighbor.text = neighbor.text.encode("utf-8").decode("unicode_escape")
    tree.write(xml_path, encoding="utf-8", xml_declaration=True)

def get_xml_file(folder_path):
    xml_list = []
    for dirpath, dirname, filenames in os.walk(folder_path):
        for file_name in filenames:
            if file_name.split(".")[-1] == "xml":
                xml_list.append(file_name)
        if len(xml_list) != 1:
            print("文件夹中不止一个xml文件")
        else:
            return os.path.join(folder_path, xml_list[0])


if __name__ == "__main__":
    xml_file = get_xml_file("../../result/")
    print(xml_file)
    # modify_text(xml_file)