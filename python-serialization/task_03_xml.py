import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Sérialise un dictionnaire Python en XML et sauvegarde dans un fichier.

    Args:
        dictionary (dict): Le dictionnaire à sérialiser.
        filename (str): Le nom du fichier XML de sortie.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # convertir en string

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Désérialise un fichier XML en dictionnaire Python.

    Args:
        filename (str): Le fichier XML à lire.

    Returns:
        dict: Le dictionnaire reconstruit depuis le XML.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    data = {}
    for child in root:
        data[child.tag] = child.text

    return data
