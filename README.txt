This tool is a free to use software for documentation purposes. Its purpose is to translate user added
comments into an xml structure for easy documentation of classes and their structures.

The tool extracts user placed comments between appointed tags, into an XML tree structure, useful in conjunction with
the Miresa web documentation tree display.

---------------------------------------------------- Example -----------------------------------------------------------

 The following is an example as to how the developer should use the tool during development, eg:

 <<<
 <<Method Name>>
 <<Method Description>>
 <<
 param1 -> param1_description,
 param2 -> param2_description,
 param3 -> param3_description
 >>
 >>>
 public static void getClientTotal(int param1, int param2, int param3){

 }

------------------------------------------------------ Key -------------------------------------------------------------
Annotations can be user defined, or left null to use defaults:

 <<< = outer_notation_start
 >>> = outer_notation_end
 <!  = inner_notation_start
 !>  = inner_notation_end
 ,   = parameter_separator