import math

##################################################
# Info # Info # Info # Info # Info # Info # Info #
##################################################

# Generates the `input` file for Bertini

#################################################
# Functions # Functions # Functions # Functions #
#################################################

# Gets the functinos needed for the bertini input
class FunctionGenerator(object):
    family_1_file_name = "family1.txt" # Path to the file containing family 1
                                       # functions in order starting with n=1
                                       # on line 0
    _function_number = 1 # Functions are defined for natural numbers {1,2,3,...}
    _function_file = None

    # Opens the file with the functions
    def __init__(self):
        self._function_file = open(self.family_1_file_name, "r")
        if self._function_file == None:
            raise Exception("File {0:s} not found".format(self.family_1_file_name))
        
    def __del__(self):
        if self._function_file != None:
            self._function_file.close()

    # Creates the nth funtion from Sam's functions
    def get_function(self, n: int) -> str:
        # Error checking
        if n < 1:
            raise Exception("n must be a non-zero integer, it is " + str(n))

        # Hard code first two functions
        if n == 1:
             return "(x1^2-1)/(3*y1)+y1"

        if n == 2:
            return "(x2^2-1)/(3*y2)+y1"

        # For functions 3+, read the next line from self.family_1_file_name generated
        #   from the Mathematica file `equations.nb`
        line = self._function_file.readline().strip().replace("**","^")
        if line == "":
            raise Exception("File family.txt contains no more functions, n is {}".format(n))
        return line

    def get_next_function(self) -> str:
        ret_str = self.get_function(self._function_number)
        self._function_number = self._function_number + 1
        return ret_str

# Adds a newline to every line in the list lines
def add_new_lines(lines):
    return list(map(lambda l: l + "\n", lines))

# Adds subfunctions as parameters to the lines as well as Bertini `function`
def add_subfunctions(lines, f_gen, n):
    # Add function_line
    function_line = "function "
    for i in range(1, n):
        function_line = function_line + " f" + str(i)
        if i < n-1:
            function_line = function_line + ","
    function_line = function_line + ";"
    lines.append(function_line)

    # Add subfunctions themselves
    for i in range(1, n + 1):
        lines.append("r" + str(i) + " = " + f_gen.get_next_function() + ";")
    return lines

# Adds functions we're solving
def add_functions(lines, mode, n):
    if mode == 1:
        for i in range(1,n):
            lines.append("f" + str(i) + " = r" + str(i) + " - r" + str(i+1) + ";")
        return lines
    else:
        raise Exception("Mode {0:d} unrecognized".format(mode))

#####################################################
# Parameters # Parameters # Parameters # Parameters #
#####################################################

f_num = 5;
mode = 1;   # Modes:
            # 1: fn = rn - r(n+1) = 0

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

lines = add_subfunctions(lines, f_gen, f_num)
lines.append("")
lines = add_functions(lines, mode, f_num)
lines.append("")
lines.append("END;")
lines = add_new_lines(lines)

f = open("input", "w")
f.writelines(lines)
f.close()
