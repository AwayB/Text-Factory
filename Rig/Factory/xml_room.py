from lxml import etree as ET
from os import path
import tell
from FSGate import are_files_in, dump_in_file

#Some XML values rely on an attribute rather than a tag. They are in this dictionary of lists.
#Key=Attribute, Value=List of tags that require this attribute. Modify it at will.
attribute_dependent={'name':('Id','Role'),'type':('Orga', 'Address')}

def concatenate_standard_xml(template_root, values_root):
    """Will concatenate an XML from a template and values.
    """
    #Place the values in a List of Dictionaries.
    values_elems = [ET.Element(i.tag, i.attrib) for i in values_root.iter(tag=ET.Element)]
    
    #Split the elements that depend on attributes from those depending on tags.
    tags_elems = [elem for elem in values_elems if not any(val.__contains__(elem.tag) for val in attribute_dependent.values())]
    attrib_elems = [elem for elem in values_elems if any(val.__contains__(elem.tag) for val in attribute_dependent.values())]

    #Iterate through the fused XML lines.
    for line in template_root.iter():
        
        #If it is tag dependent, get the element and populate the xml with its attributes.
        if len([i for i in tags_elems if i.tag == line.tag]):
            sole_element, = [i for i in tags_elems if i.tag == line.tag]
            for target_attrib in sole_element.attrib:
                line.set(target_attrib, sole_element.get(target_attrib))
            sole_element = None

        #If it is attribute dependent, check the defining attribute content and use it to know what to populate with.
        elif len([i for i in attrib_elems if i.tag == line.tag]):
            possible_elements = [i for i in attrib_elems if i.tag == line.tag]
            for element in possible_elements:
                #get_key_from_dict_value(attribute_dependent, element.attrib)
                target = str()
                for key, value_container in attribute_dependent.items():
                    for value in value_container:
                        if value == element.tag:
                            target = key
                
                if element.get(target) == line.get(target):
                    for target_attrib in element.attrib:
                        line.set(target_attrib, element.get(target_attrib))
    return template_root

def get_key_from_dict_value(dictionary, target):
    "In a dictionary, returns all keys containing the target value."
    possible_keys = list()
    for key, values in dictionary.items():
        if (type(values) == tuple or type(values) == list):
            [possible_keys.append(key) for val in values if val == target]
        else:
            if (values == target):
                possible_keys.append(key)
    return(possible_keys)

def check_against_xsd(fused_xml, xsd_file):
    "Checks your completed XML against an XML Schema file"
    xsd_contents = ET.parse(xsd_file)
    xsd = ET.XMLSchema(xsd_contents)
    xsd.assertValid(ET.parse(fused_xml))
    log = xsd.error_log
    error = log.last_error
    if (error):
        print(error.type_name)

def get_xml_file_root(xml):
    "Returns the root of the XML."
    tree = ET.parse(xml)
    root = tree.getroot()
    return (root)

def get_mandatory_xmls(folder, settings):
    "Gets the necessary XML names from the settings file."
    settings_root = get_xml_file_root(settings)
    return(settings_root.find("TemplateLoc").get("name"),
    settings_root.find("ValuesLoc").get("name"),
    settings_root.find("CheckLoc").get("name"))

def clean_empty(final_xml):
    "Cleans the xml of all attributes that had no values set."
    #Iterate through the fused XML lines.
    for line in final_xml.iter():
        for attrib in line.attrib:
            if line.attrib[attrib] == "":
                del line.attrib
    return final_xml

def fuse_xml_key_values(folder, settings, order):
    "Gets and checks the necessary XMLs, then passes them to concatenation."
    #Check and get base files.
    keys_file, values_file, check_file = get_mandatory_xmls(folder, settings)
    are_files_in(folder, (keys_file, values_file, check_file), True)
    tell.fusion_files(keys_file, values_file)

    #Get the root of both XMLs.
    keys_root = get_xml_file_root(keys_file)
    values_root = get_xml_file_root(values_file)

    #Fuse, then output.
    fused_xml = concatenate_standard_xml(keys_root, values_root)
    final_xml = clean_empty(fused_xml)
    dump_in_file('test.xml',ET.tostring(final_xml , encoding='UTF-8', xml_declaration = True), byte_text=True)