# #
# # Module imports
# import os
# #
# def project_validator(project_path, comment_notation_start, comment_notation_end, inner_notation_start, inner_notation_end, parameter_separator):
#     'Validates project directory; Checks for correct notation start and endings'
#     try:
#         # Iterate through every folder/file in directory
#         for filename in os.listdir(project_path):
#             if os.path.isdir(project_path + '\\' + filename):
#                 #
#                 # Makes recursive call down directory
#                 project_validator(
#                     project_path=project_path + "\\" + filename,
#                     comment_notation_start=comment_notation_start,
#                     comment_notation_end=comment_notation_end,
#                     inner_notation_start=inner_notation_start,
#                     inner_notation_end=inner_notation_end,
#                     parameter_separator=parameter_separator
#                 )
#             else:
#                 #
#                 # Iterate through current file; Returns a list of filepaths with incorrect notations
#                 if filename != 'Documentation_Notations.xml':
#                     notation_list = file_checker(
#                         project_path=project_path + "\\" + filename,
#                         comment_notation_start=comment_notation_start,
#                         comment_notation_end=comment_notation_end,
#                         inner_notation_start=inner_notation_start,
#                         inner_notation_end=inner_notation_end,
#                         parameter_separator=parameter_separator
#                     )
#                 #
#             #
#         #
#     except ValueError as ve:
#         print 'Error parsing file content'
#         print type(ve)
#         print ve.args
#     except IOError as ioe:
#         print 'An IO error occurred'
#         print type(ioe)
#         print ioe.args
#     except Exception as exc:
#         print 'An error occurred during XML generation'
#         print type(exc)
#         print exc.args
#     return notation_list
#
# def file_checker(project_path, comment_notation_start, comment_notation_end, inner_notation_start, inner_notation_end, parameter_separator):
#     " Read the file contents as a single string "
#     #
#     # Open file into a single variable
#     with open(project_path, 'r') as file:
#         data = file.read()
#         data = data.replace('\n', '')
#     #
#     if comment_notation_start not in data:
#         if