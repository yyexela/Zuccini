##################################################
# Info # Info # Info # Info # Info # Info # Info #
##################################################

# Generates the `input` file for Bertini

#################################################
# Functions # Functions # Functions # Functions #
#################################################

class FunctionGenerator(object):
    _function_number = 0

    @classmethod
    def get_function(cls, f_num):
        return "x1^2"

    @classmethod
    def get_next_function(cls):
        return cls.get_function(cls._function_number)



# Adds a newline to every line in the list lines
def add_new_lines(lines):
    return list(map(lambda l: l + "\n", lines))

# Adds functions as parameters to the lines as well as Bertini `function`
def add_functions(lines, f_gen, f_num):
    # Add function_line
    function_line = "function "
    for i in range(0, f_num):
        function_line = function_line + " f" + str(i)
    function_line = function_line + ";"
    lines.append(function_line)

    # Add functions themselves
    for i in range(0, f_num):
        lines.append("r" + str(i) + " = " + f_gen.get_next_function() + ";")
    return lines


#####################################################
# Parameters # Parameters # Parameters # Parameters #
#####################################################

f_num = 5;

##################################################
# Main # Main # Main # Main # Main # Main # Main #
##################################################

# Create lines we want to write, add newlines later
# Declare config and other static lines that won't necessarily be changing later
lines = ["CONFIG;", \
         "TRACKTYPE: 1;", \
         "END;", \
         "", \
         "INPUT", \
         "variable_group x1, y1, x2, y2;"]

# Create class which generates function
f_gen = FunctionGenerator()

lines = add_functions(lines, f_gen, f_num)
lines = add_new_lines(lines)

f = open("input", "w")
f.writelines(lines)
f.close()
