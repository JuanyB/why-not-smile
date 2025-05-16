# project3.py
#
# ICS 33 Spring 2025
# Project 3: Why Not Smile?
#
# The main module that executes your Grin interpreter.
#
# WHAT YOU NEED TO DO: You'll need to implement the outermost shell of your
# program here, but consider how you can keep this part as simple as possible,
# offloading as much of the complexity as you can into additional modules in
# the 'grin' package, isolated in a way that allows you to unit test them.




def main() -> None:
    import my_files as mf
    input_lines_list = []
    """Make sure the inputted grin code is input from the terminal not a sample file
    use a while loop to stop once a person inputs a period or END"""
    run = True

    while run:

        first_grin_code = input()

        input_lines_list.append(first_grin_code)

        if first_grin_code.strip() == ".":
            break

    mf.off_hand.handle_main_organize(input_lines_list)



if __name__ == '__main__':
    main()


