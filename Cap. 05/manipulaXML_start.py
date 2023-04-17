#
# Arquivo com exemplo de tratamento de XML
#

import xml.dom.minidom
def manipula():
    doc = xml.dom.minidom.parse("D:\\git\\arquivos_de_exercicios_descubra_o_python\\Cap. 05\\exemploXML.xml")
    print("Primeira tag: ", str(doc.firstChild.tagName))

    fNome = doc.getElementsByTagName("firstname")

    print("O primeiro nome: ", fNome[0].firstChild.nodeValue)

    for skill in doc.getElementsByTagName("skill"):
        print("Skill encontrada: ", skill.getAttribute("name"))


manipula()
