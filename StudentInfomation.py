'''
Created on Mar 9, 2021

@author: Marlon Gacrama
'''

from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree

root=Element('Student')
tree=ElementTree(root)

name=Element('name')
root.append(name)
name.text='Marlon Gacrama Jr'

address=Element('address')
root.append(address)
address.text='Cebu City'

contact=Element('contact')
root.append(contact)
contact.text="09396810206"

root.set('id', '100424250')

print (etree.tostring(root))
tree.write('Student.xml')