from my_files.off_hand import *

def take_label(line_with_label):
    elements_in_line = []
    for i in line_with_label[2:]:
        elements_in_line.append(i)
    execute_grin_one_by_one(elements_in_line)
