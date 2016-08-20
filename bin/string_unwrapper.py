import sys
import notation_object as nobj
sys.setrecursionlimit(10000)
#
def string_unwrapper(comment_notation_start, comment_notation_end, line, string_list):
    " Takes input file content as a single string; Returns list of notation_objects "
    #
    # Recursive check
    if comment_notation_start not in line and comment_notation_end not in line:
        return string_list
    #
    if string_list is None:
        string_list = []
    #
    # Calculates position of start and end notation
    comment_notation_start_index = line.index(comment_notation_start)
    comment_notation_end_index = line.index(comment_notation_end)
    #
    sub_string = line[comment_notation_start_index: comment_notation_end_index + len(comment_notation_end)]
    #
    # Append substring to the list which will be returned at the end of this function
    string_list.append(sub_string)
    #
    # Delete substring from file string
    line = line.replace(sub_string, '', 1)
    #
    # Recursive Call
    return string_unwrapper(
        comment_notation_start=comment_notation_start,
        comment_notation_end=comment_notation_end,
        line=line,
        string_list=string_list
    )
#
def comment_unwrapper(comment_notation_start, comment_notation_end, list):
    " Unwraps list of string notations, removing comment_notation string elements "
    string_list = []
    for line_block in list:
        if comment_notation_start in line_block and comment_notation_end in line_block:
            #
            # Calculates position of start and end notation
            comment_notation_start_index = line_block.index(comment_notation_start)
            comment_notation_end_index = line_block.index(comment_notation_end)
            #
            sub_string = line_block[comment_notation_start_index + len(comment_notation_start): comment_notation_end_index]
            #
            # Append substring to list
            string_list.append(sub_string)
        #
    #
    return string_list
#
def string_object_converter(inner_notation_start, inner_notation_end, parameter_separator, list):
    " Converts list of string notations into a list of 'notation_object' objects "
    #
    notation_list = []
    #
    # Iterate through list of strings. Every Iteration, each string module will be converted into an object of type
    # 'notation_object'
    for line_block in list:
        # Scope declarations
        sub_string_name = ''
        sub_string_desc = ''
        param_list = []
        #
        # Check for inner_notations inside string
        if inner_notation_start in line_block or inner_notation_end in line_block:
            #
            # Retrieve method name string
            start_index_name = line_block.index(inner_notation_start)
            end_index_name = line_block.index(inner_notation_end)
            sub_string_name = line_block[start_index_name: end_index_name + len(inner_notation_start)]
            #
            # Delete substring from file string
            line_block = line_block.replace(sub_string_name, '', 1)
            #
            # Clean substring from inner_notations
            sub_string_name = inner_notation_unwrapper(
                inner_notation_start=inner_notation_start,
                inner_notation_end=inner_notation_end,
                line=sub_string_name
            )
        #
        # --------------------------------------------------------------------------------------------------------------
        #
        # Check for inner_notations inside string
        if inner_notation_start in line_block or inner_notation_end in line_block:
            #
            # Retrieve method description string
            start_index_desc = line_block.index(inner_notation_start)
            end_index_desc = line_block.index(inner_notation_end)
            sub_string_desc = line_block[start_index_desc: end_index_desc + len(inner_notation_start)]
            #
            # Delete substring from file string
            line_block = line_block.replace(sub_string_desc, '', 1)
            #
            # Clean substring from inner_notations
            sub_string_desc = inner_notation_unwrapper(
                inner_notation_start=inner_notation_start,
                inner_notation_end=inner_notation_end,
                line=sub_string_desc
            )
        #
        # --------------------------------------------------------------------------------------------------------------
        #
        # Check for inner_notations inside string
        if inner_notation_start in line_block or inner_notation_end in line_block:
            #
            # Retrieve method parameters
            start_index_param = line_block.index(inner_notation_start)
            end_index_param = line_block.index(inner_notation_end)
            sub_string_param = line_block[start_index_param: end_index_param + len(inner_notation_start)]
            #
            # Clean substring from inner_notations
            sub_string_param = inner_notation_unwrapper(
                inner_notation_start=inner_notation_start,
                inner_notation_end=inner_notation_end,
                line=sub_string_param
            )
            #
            # Unwrap parameter string into list
            param_list = paramater_unwrapper(
                sub_string_param=sub_string_param,
                parameter_separator=parameter_separator,
                param_list=None
            )
        #
        if sub_string_name is not '' or sub_string_desc is not '' or len(param_list) != 0:
            no = nobj.Notation(
                method_name=sub_string_name,
                method_description=sub_string_desc,
                method_params=param_list
            )
            notation_list.append(no)
    #
    if len(notation_list) == 0:
        return None
    return notation_list
#
def paramater_unwrapper(sub_string_param, parameter_separator, param_list):
    " Unwraps param string, splitting parameters into a list of parameters "
    #
    if param_list is None:
        param_list = []
    #
    # Recursive check
    if parameter_separator not in sub_string_param:
        param = sub_string_param
        param_list.append(param)
        return param_list
    #
    # Calculates position of parameter separator
    parameter_separator_index = sub_string_param.index(parameter_separator)
    param = sub_string_param[0: parameter_separator_index + 1]
    #
    # Delete substring from file string
    sub_string_param = sub_string_param.replace(param, '', 1)
    #
    # Delete parameter separator from parameter
    param = param.replace(parameter_separator, '', 1)
    #
    # Append Parameter to list
    param_list.append(param)
    #
    # Recursive call
    return paramater_unwrapper(
        sub_string_param=sub_string_param,
        parameter_separator=parameter_separator,
        param_list=param_list
    )
#
def inner_notation_unwrapper(inner_notation_start, inner_notation_end, line):
    " Cleans inner comment notations from start & end inner notations "
    #
    # Calculates position of start and end inner_notation
    inner_notation_start_index = line.index(inner_notation_start)
    inner_notation_end_index = line.index(inner_notation_end)
    #
    return line[inner_notation_start_index + len(inner_notation_start): inner_notation_end_index]