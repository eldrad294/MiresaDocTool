# Import modules
import os
import string_unwrapper as su
from xml.etree.ElementTree import SubElement
#
def project_crawler(project_path, tree, comment_notation_start, comment_notation_end, inner_notation_start, inner_notation_end, parameter_separator):
    " Recursively probes a folder directory until all files have been returned "
    #
    try:
        # Iterate through every folder/file in directory
        for filename in os.listdir(project_path):
            if os.path.isdir(project_path + '\\' + filename):
                #
                # Create sub element for folder
                child = SubElement(tree, 'folder', {'foldername': filename})
                #
                # Makes recursive call down directory
                project_crawler(
                    project_path=project_path + "\\" + filename,
                    tree=child,
                    comment_notation_start=comment_notation_start,
                    comment_notation_end=comment_notation_end,
                    inner_notation_start=inner_notation_start,
                    inner_notation_end=inner_notation_end,
                    parameter_separator=parameter_separator
                )
            else:
                #
                # Iterate through current file, and return a list of notation objects
                if filename != 'Documentation_Notations.xml':
                    notation_list = file_crawler(
                        project_path=project_path + "\\" + filename,
                        comment_notation_start=comment_notation_start,
                        comment_notation_end=comment_notation_end,
                        inner_notation_start=inner_notation_start,
                        inner_notation_end=inner_notation_end,
                        parameter_separator=parameter_separator
                    )
                    #
                    if notation_list is not None:
                        #
                        # Create sub element for file
                        file = SubElement(tree, 'File', {'Filename': filename})
                        #
                        # Creating sub tags within file element
                        for notation in notation_list:
                            #
                            # Create file sub element
                            notation_element = SubElement(file, 'Notation')
                            #
                            # Create method name notation
                            method_name = SubElement(notation_element, 'Method_Name')
                            method_name.text = notation.method_name
                            #
                            # Create method description notation
                            method_description = SubElement(notation_element, 'Method_Description')
                            method_description.text = notation.method_description
                            #
                            # Create method parameter notation
                            method_params = SubElement(notation_element, 'Method_Parameters')
                            for parameter in notation.method_params:
                                method_param = SubElement(method_params, 'Parameter')
                                method_param.text = parameter
                            #
                        #
                    #
                #
    except ValueError as ve:
        print type(ve)
        print ve.args
    except IOError as ioe:
        print type(ioe)
        print ioe.args
    except Exception as exc:
        print type(exc)
        print exc.args
    return tree
#
def file_crawler(project_path, comment_notation_start, comment_notation_end, inner_notation_start, inner_notation_end, parameter_separator):
    " Read the file contents as a single string "
    #
    # Open file into a single variable
    with open(project_path, 'r') as file:
        data = file.read()
        data = data.replace('\n', '')
    #
    # Convert file content string into a list of string notations
    myList = su.string_unwrapper(
        comment_notation_start=comment_notation_start,
        comment_notation_end=comment_notation_end,
        line=data,
        string_list=None
    )
    #
    # Removing comment notations from list content
    if myList is not None:
        myList = su.comment_unwrapper(
            comment_notation_start=comment_notation_start,
            comment_notation_end=comment_notation_end,
            list=myList
        )
        #
        # Converting list strings into 'notation_object' object
        myList = su.string_object_converter(
            inner_notation_start=inner_notation_start,
            inner_notation_end=inner_notation_end,
            parameter_separator=parameter_separator,
            list=myList
        )
        return myList
    else:
        return None
