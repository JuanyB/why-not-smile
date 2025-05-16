import grin
"""This function updates the entire program dictionary with the updated values of 
grin variables after a mathematical expression such as ADD or SUB"""

def dictionary_update(operation_type, first_term, second_term, program_dict):
    first_operand = None
    second_operand = None
    math_dict = dict()
    if first_term.kind() is grin.GrinTokenKind.IDENTIFIER:
        first_operand = program_dict[first_term.text()]
    elif first_term.kind() is grin.GrinTokenKind.LITERAL_STRING:
        first_operand = first_term.text()
    elif first_term.kind() is grin.GrinTokenKind.LITERAL_INTEGER:
        first_operand = int(first_term.text())
    elif first_term.kind() is grin.GrinTokenKind.LITERAL_FLOAT:
        first_operand = float(first_term.text())

    if second_term.kind() is grin.GrinTokenKind.IDENTIFIER:
        second_operand = program_dict[second_term.text()]
    elif second_term.kind() is grin.GrinTokenKind.LITERAL_STRING:
        second_operand = second_term.text()
    elif second_term.kind() is grin.GrinTokenKind.LITERAL_INTEGER:
        second_operand = int(second_term.text())
    elif second_term.kind() is grin.GrinTokenKind.LITERAL_FLOAT:
        second_operand = float(second_term.text())
    if first_operand is not None and second_operand is not None:
        math_dict[operation_type.text()] = (first_operand, second_operand)
        return math_dict

def add(a, b, program_dict):
    first = None
    second = None
    if a.kind() is grin.GrinTokenKind.IDENTIFIER:
        first = program_dict[a.text()]
    elif a.kind() is grin.GrinTokenKind.LITERAL_STRING:
        first = a.text()
    elif a.kind() is grin.GrinTokenKind.LITERAL_INTEGER:
        first = int(a.text())
    elif a.kind() is grin.GrinTokenKind.LITERAL_FLOAT:
        first = float(a.text())

    if b.kind() is grin.GrinTokenKind.IDENTIFIER:
        second = program_dict[b.text()]
    elif b.kind() is grin.GrinTokenKind.LITERAL_STRING:
        second = b.text()
    elif b.kind() is grin.GrinTokenKind.LITERAL_INTEGER:
        second = int(b.text())
    elif b.kind() is grin.GrinTokenKind.LITERAL_FLOAT:
        second = float(b.text())
    if first is not None and second is not None:
        mini_dict = dict()
        mini_dict[a.text()] = first + second
        return mini_dict

def subtract(a, b, program_dict):
    first = None
    second = None
    if a.kind() is grin.GrinTokenKind.IDENTIFIER:
        first = program_dict[a.text()]
    elif a.kind() is grin.GrinTokenKind.LITERAL_STRING:
        first = a.text()
    elif a.kind() is grin.GrinTokenKind.LITERAL_INTEGER:
        first = int(a.text())
    elif a.kind() is grin.GrinTokenKind.LITERAL_FLOAT:
        first = float(a.text())

    if b.kind() is grin.GrinTokenKind.IDENTIFIER:
        second = program_dict[b.text()]
    elif b.kind() is grin.GrinTokenKind.LITERAL_STRING:
        second = b.text()
    elif b.kind() is grin.GrinTokenKind.LITERAL_INTEGER:
        second = int(b.text())
    elif b.kind() is grin.GrinTokenKind.LITERAL_FLOAT:
        second = float(b.text())
    if first is not None and second is not None:
        mini_dict = dict()
        mini_dict[a.text()] = first - second
        return mini_dict

def multiply(a, b, program_dict):
    first = None
    second = None
    if a.kind() is grin.GrinTokenKind.IDENTIFIER:
        first = program_dict[a.text()]
    elif a.kind() is grin.GrinTokenKind.LITERAL_STRING:
        first = a.text()
    elif a.kind() is grin.GrinTokenKind.LITERAL_INTEGER:
        first = int(a.text())
    elif a.kind() is grin.GrinTokenKind.LITERAL_FLOAT:
        first = float(a.text())

    if b.kind() is grin.GrinTokenKind.IDENTIFIER:
        second = program_dict[b.text()]
    elif b.kind() is grin.GrinTokenKind.LITERAL_STRING:
        second = b.text()
    elif b.kind() is grin.GrinTokenKind.LITERAL_INTEGER:
        second = int(b.text())
    elif b.kind() is grin.GrinTokenKind.LITERAL_FLOAT:
        second = float(b.text())
    if first is not None and second is not None:
        mini_dict = dict()
        mini_dict[a.text()] = first * second
        return mini_dict
def divide(a, b, program_dict):
    first = None
    second = None
    if a.kind() is grin.GrinTokenKind.IDENTIFIER:
        first = program_dict[a.text()]
    elif a.kind() is grin.GrinTokenKind.LITERAL_STRING:
        first = a.text()
    elif a.kind() is grin.GrinTokenKind.LITERAL_INTEGER:
        first = int(a.text())
    elif a.kind() is grin.GrinTokenKind.LITERAL_FLOAT:
        first = float(a.text())

    if b.kind() is grin.GrinTokenKind.IDENTIFIER:
        second = program_dict[b.text()]
    elif b.kind() is grin.GrinTokenKind.LITERAL_STRING:
        second = b.text()
    elif b.kind() is grin.GrinTokenKind.LITERAL_INTEGER:
        second = int(b.text())
    elif b.kind() is grin.GrinTokenKind.LITERAL_FLOAT:
        second = float(b.text())
    if first is not None and second is not None:
        mini_dict = dict()
        mini_dict[a.text()] = first // second
    return mini_dict
