# Import modules
import project_crawler as fc
from xml.etree.ElementTree import Element, Comment
import xml.etree.cElementTree as et
#
print "Welcome to DocTool, a documentation to XML parser."
#
# User Input
project_path = raw_input("Enter project path directory:")
outer_notation_start = raw_input("Enter notation for block start:") or "<<<"
outer_notation_end = raw_input("Enter notation for block end:") or ">>>"
inner_notation_start = raw_input("Enter notation for inner block start") or "<<"
inner_notation_end = raw_input("Enter notation for inner block end") or ">>"
parameter_separator = raw_input("Enter notation for parameter separator") or ","
#
# Cleaning input path
project_path = project_path.replace("//", "\\")
project_path = project_path.replace("/", "\\")
#
# Generate top xml node
tree = Element('root_folder')
comment = Comment('XML Root Node')
tree.append(comment)
#
# Initiate file_crawler process
print 'Initiating File Crawler Process...'
tree = fc.project_crawler(
    project_path=project_path,
    tree=tree,
    comment_notation_start=outer_notation_start,
    comment_notation_end=outer_notation_end,
    inner_notation_start=inner_notation_start,
    inner_notation_end=inner_notation_end,
    parameter_separator=parameter_separator
)
#
# Writing XML tree to file
print 'Creating XML File...'
tree = et.ElementTree(tree)
tree.write(project_path + "\Documentation_Notations.xml")
#
# Print success message if script has come this far
print "XML file successfully created at " + project_path + "\Documentation_Notations.xml"
