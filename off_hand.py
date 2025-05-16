from my_files import myvariables
from my_files import mylabels
from my_files import grin_arithmetic as minimath
from collections import namedtuple
import grin
import sys

"""Program list is actually a dictionary, originally a list, but switched to a dictionary for easier access to 
variable names and their values. """
# the program order list is to make jump statements easier, by finding the index of the desired line, we can
# easily access it and execute the line of grin code with a function

"""handle_main is used to determine which modules and functions are appropriate for the line of grin code we are receiving"""


program_variables = dict()
program_order = namedtuple("program_order", ["program_line_contents", "program_order_number"])

def handle_main_organize(file_lines_list):
    try:
        parsed_grin_line = grin.parse(file_lines_list)

        program_order_list_simplified = list(parsed_grin_line)
        # print('PROGRAM LIST', list(parsed_grin_line))
        handle_grin_line_commands(program_order_list_simplified)
    except grin.GrinParseError as e:
        print(e)
        sys.exit(0)

def handle_grin_line_commands(program_order_index):
    negative_jump = None
    sub_index = 0
    current_index = 0
    sub_index_list = []
    sub_list_index = 0
    while current_index < len(program_order_index):
        line_tokens = program_order_index[current_index]
        line_command = line_tokens[0]

        # if line_command.kind() is grin.GrinTokenKind.GOTO:
        #     current_index += 1
        #     line_jump = line_tokens[1]
        #     if len(line_tokens) > 3:
        #         comparison_operation = comparison_operations(line_tokens[2], line_tokens[3], line_tokens[4], line_tokens[5])
        #         if comparison_operation:
        #             program_order_index += int(line_jump.text())
        #     else:
        #         if line_jump.kind() is grin.GrinTokenKind.IDENTIFIER:
        #             program_order_index += 1
        #         if line_jump.text().isnumeric():
        #             program_order_index = program_order_index + int(line_jump.text())
        #         elif line_jump.text()[1:].isnumeric():
        #             if negative_jump == line_jump.text():
        #                 program_order_index += abs(int(line_jump.text()))
        #                 program_order_index += 1
        #             negative_jump = line_jump.text()
        #             program_order_index -= abs(int(line_jump.text()))
        #         elif line_jump.text().isalpha():
        #             for token_line in program_order_index:
        #                 if token_line[0].text() == line_jump.text():
        #                     program_order_index = int(program_order_index.index(token_line))
        # elif line_command.kind() is grin.GrinTokenKind.GOSUB:
        #     current_index += 1
        #     line_jump = line_tokens[1]
        #     sub_index = program_order_index + 1
        #     sub_index_list.append(sub_index)
        #     if len(line_tokens) > 3:
        #         comparison_operation = comparison_operations(line_tokens[2], line_tokens[3], line_tokens[4],
        #                                                      line_tokens[5])
        #         if comparison_operation:
        #             program_order_index += int(line_jump.text())
        #     else:
        #         if line_jump.kind() is grin.GrinTokenKind.IDENTIFIER:
        #             program_order_index += 1
        #         if line_jump.text().isnumeric():
        #             program_order_index = program_order_index + int(line_jump.text())
        #         elif line_jump.text()[1:].isnumeric():
        #             if negative_jump == line_jump.text():
        #                 program_order_index += abs(int(line_jump.text()))
        #                 program_order_index += 1
        #             negative_jump = line_jump.text()
        #             program_order_index -= abs(int(line_jump.text()))
        #         elif line_jump.text().isalpha():
        #             for token_line in program_order_index:
        #                 if token_line[0].text() == line_jump.text():
        #                     # print('Label made it here')
        #                     program_order_index = int(program_order_index.index(token_line))
        if line_command.kind() is grin.GrinTokenKind.RETURN:
            current_index += 1
            sub_list_index -= 1
            program_order_index = sub_index_list[sub_list_index]
            sub_index += 1

        else:
            current_index += 1
            execute_grin_one_by_one(line_tokens)

def execute_grin_one_by_one(single_line_grin_code):
    grin_command = single_line_grin_code[0]
    if single_line_grin_code[1].kind() is grin.GrinTokenKind.COLON:
        mylabels.take_label(single_line_grin_code)
    if grin_command.kind().category() is grin.GrinTokenCategory.KEYWORD:
        if grin_command.kind() is grin.GrinTokenKind.LET:
            program_variables.update(myvariables.variable_assignment(single_line_grin_code))
        elif grin_command.kind() is grin.GrinTokenKind.PRINT:
            printing(single_line_grin_code)
        elif grin_command.kind() is grin.GrinTokenKind.INNUM:
            input_num = myvariables.variable_assignment(single_line_grin_code)
            if input_num is not None: program_variables.update(input_num)
        elif grin_command.kind() is grin.GrinTokenKind.INSTR:
            input_str = myvariables.variable_assignment(single_line_grin_code)
            if input_str is not None: program_variables.update(input_str)

        else:
            keyword_category(single_line_grin_code)



def keyword_category(keyword_object_line):

    for keyword_object in keyword_object_line:
        """This function should handle all keywords that are arithmetic"""
        if keyword_object.kind() is grin.GrinTokenKind.ADD:
            type_of_operation = keyword_object_line[0]
            operand_1 = keyword_object_line[1]
            operand_2 = keyword_object_line[2]
            math_dict = minimath.dictionary_update(type_of_operation, operand_1, operand_2, program_variables)
            program_variables.update(math_dict)
            arithmetic_operations(type_of_operation, operand_1, operand_2)
        elif keyword_object.kind() is grin.GrinTokenKind.MULT:
            type_of_operation = keyword_object_line[0]
            operand_1 = keyword_object_line[1]
            operand_2 = keyword_object_line[2]
            math_dict = minimath.dictionary_update(type_of_operation, operand_1, operand_2, program_variables)
            program_variables.update(math_dict)
            arithmetic_operations(type_of_operation, operand_1, operand_2)

        elif keyword_object.kind() is grin.GrinTokenKind.DIV:
            type_of_operation = keyword_object_line[0]
            operand_1 = keyword_object_line[1]
            operand_2 = keyword_object_line[2]
            math_dict = minimath.dictionary_update(type_of_operation, operand_1, operand_2, program_variables)
            program_variables.update(math_dict)
            arithmetic_operations(type_of_operation, operand_1, operand_2)

        elif keyword_object.kind() is grin.GrinTokenKind.SUB:
            type_of_operation = keyword_object_line[0]
            operand_1 = keyword_object_line[1]
            operand_2 = keyword_object_line[2]
            math_dict = minimath.dictionary_update(type_of_operation, operand_1, operand_2, program_variables)
            program_variables.update(math_dict)
            arithmetic_operations(type_of_operation, operand_1, operand_2)


def arithmetic_operations(type_of_operation, operand_1, operand_2):
    """Operand 1 and two are the two terms after the type of operation which would be ADD, SUB(subtract) etc. """
    if type_of_operation.kind() is grin.GrinTokenKind.ADD:
        addition = minimath.add(operand_1, operand_2, program_variables)
        # print(addition)
        program_variables.update(addition)
    elif type_of_operation.kind() is grin.GrinTokenKind.MULT:
        multiply = minimath.multiply(operand_1, operand_2, program_variables)
        program_variables.update(multiply)
        pass
        # program_list.update(math_dict)
    elif type_of_operation.kind() is grin.GrinTokenKind.DIV:
        division = minimath.divide(operand_1, operand_2, program_variables)
        program_variables.update(division)
        pass
        # program_list.update(math_dict)
    elif type_of_operation.kind() is grin.GrinTokenKind.SUB:
        subtraction = minimath.subtract(operand_1, operand_2, program_variables)
        program_variables.update(subtraction)
        pass
        # program_list.update(math_dict)
def printing(line_printable_objects):
    """This function handles all lines of grin code with the keyword PRINT"""
    for printable_object in line_printable_objects:
        if printable_object.kind() is grin.GrinTokenKind.PRINT:
            continue
        elif printable_object.kind().category() is grin.GrinTokenCategory.LITERAL_VALUE:
            print(printable_object.text())
        elif printable_object.kind().category() is grin.GrinTokenCategory.IDENTIFIER:
            print(program_variables[printable_object.text()])

def comparison_operations(conditional_statement, first_term, comparison_operator, second_term):
    """still got to do comparison operators with the if statement"""
    first_term_value = None
    second_term_value = None

    if first_term.kind() is grin.GrinTokenKind.IDENTIFIER:
        first_term_value = program_variables[first_term.text()]
    elif first_term.kind() is grin.GrinTokenKind.LITERAL_INTEGER:
        first_term_value = int(first_term.text())
    elif first_term.kind() is grin.GrinTokenKind.LITERAL_STRING:
        first_term_value = first_term.text()
    elif first_term.kind() is grin.GrinTokenKind.LITERAL_FLOAT:
        first_term_value = float(first_term.text())

    if second_term.kind() is grin.GrinTokenKind.IDENTIFIER:
        second_term_value = program_variables[second_term.text()]
    elif second_term.kind() is grin.GrinTokenKind.LITERAL_INTEGER:
        second_term_value = int(second_term.text())
    elif second_term.kind() is grin.GrinTokenKind.LITERAL_STRING:
        second_term_value = second_term.text()
    elif second_term.kind() is grin.GrinTokenKind.LITERAL_FLOAT:
        second_term_value = float(second_term.text())


    if first_term_value is not None and second_term_value is not None:
        if comparison_operator.kind() is grin.GrinTokenKind.LESS_THAN_OR_EQUAL:
            return first_term_value <= second_term_value
        elif comparison_operator.kind() is grin.GrinTokenKind.LESS_THAN:
            return first_term_value <= second_term_value
        elif comparison_operator.kind() is grin.GrinTokenKind.GREATER_THAN_OR_EQUAL:
            return first_term_value >= second_term_value
        elif comparison_operator.kind() is grin.GrinTokenKind.GREATER_THAN:
            return first_term_value > second_term_value
        elif comparison_operator.kind() is grin.GrinTokenKind.EQUAL:
            return first_term_value == second_term_value
        elif comparison_operator.kind() is grin.GrinTokenKind.NOT_EQUAL:
            return first_term_value != second_term_value


    __all__ = [
        handle_main_organize.__name__,
        handle_grin_line_commands.__name__
]