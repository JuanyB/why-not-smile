import grin

class GrinVar:
    def __init__(self, self_value):
        self.self_value = self_value
        pass

    def __add__(self, other):
        return self.self_value + other
    def __iadd__(self, other):
        return self.self_value + other
    def __sub__(self, other):
        return self.self_value - other
    def __isub__(self, other):
        return self.self_value - other
    def __mul__(self, other):
        return self.self_value * other
    def __imul__(self, other):
        return self.self_value * other
    def __truediv__(self, other):
        return self.self_value / other
    def __floordiv__(self, other):
        return self.self_value // other
    def __lt__(self, other):
        return self.self_value < other
    def __eq__(self, other):
        return self.self_value == other
    def __le__(self, other):
        return self.self_value <= other


def variable_assignment(variable_line):
    variable_dict = dict()
    line_list = list()
    for i in variable_line:
        line_list.append(i)
    if line_list[0].kind() is grin.GrinTokenKind.INSTR:
        return inputted_variable(variable_line, line_list)
    elif line_list[0].kind() is grin.GrinTokenKind.INNUM:
        return inputted_variable(variable_line, line_list)
        pass
    elif line_list[0].kind() is grin.GrinTokenKind.LET:
        variable_name = line_list[1]
        assignedGrin_object = line_list[2]
        def isfloat(num):
            try:
                float(num)
                return True
            except ValueError:
                return False

        if assignedGrin_object.kind() is grin.GrinTokenKind.LITERAL_STRING:
            variable_dict[variable_name.text()] = assignedGrin_object.text()[1:-1]
            return variable_dict
        elif assignedGrin_object.kind() is grin.GrinTokenKind.LITERAL_INTEGER:
            if assignedGrin_object.text()[0] == '-':
                    variable_dict[variable_name.text()] = int(assignedGrin_object.text())
                    return variable_dict
            variable_dict[variable_name.text()] = int(assignedGrin_object.text())
            return variable_dict
        elif assignedGrin_object.kind() is grin.GrinTokenKind.LITERAL_FLOAT:
            if assignedGrin_object.text()[0] == '-':
                    variable_dict[variable_name.text()] = float(assignedGrin_object.text())
                    return variable_dict
            variable_dict[variable_name.text()] = float(assignedGrin_object.text())
            return variable_dict

def inputted_variable(variable_line, line_list):
    variable_dict = dict()
    # print('inn putt')
    def isfloat(num):
        num = num.strip()
        if num.isnumeric():
            return False
        float(num)
        return True

    variable_name = variable_line[1].text()
    if line_list[0].kind() is grin.GrinTokenKind.INSTR:
        assignedGrin_object = input('Please enter your phrase or word:')
        variable_dict[variable_name] = assignedGrin_object

    if line_list[0].kind() is grin.GrinTokenKind.INNUM:
        assignedGrin_object = input('Please enter your whole or decimal number:')
        if isfloat(assignedGrin_object): assignedGrin_object = float(assignedGrin_object)
        elif assignedGrin_object.isnumeric(): assignedGrin_object = int(assignedGrin_object)

        variable_dict[variable_name] = assignedGrin_object
    return variable_dict



