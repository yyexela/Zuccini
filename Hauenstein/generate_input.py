import math

##################################################
# Info # Info # Info # Info # Info # Info # Info #
##################################################

# Generates the `input` file for Bertini

#################################################
# Functions # Functions # Functions # Functions #
#################################################

class FunctionGenerator(object):
    _function_number = 1 # Functions are defined for natural numbers {1,2,3,...}

    @classmethod
    # Creates the nth funtion from Sam's functions
    def get_function(cls, n: int) -> str:
        # Error checking
        if n < 1:
            raise Exception("n must be a non-zero integer, it is " + str(n))

        # Hard code first two functions
        if n == 1:
             return "(x1^2-1)/(3*y1)+y1"

        if n == 2:
            return "(x2^2-1)/(3*y2)+y1"

        # For functions 3+, subtract 2 to use the expansion (ex. 3 -> 1)
        n = n - 2
        func = ""
        # Numerator
        func = func + "("
        for i in range(1,n+1):
            func = func + str(cls.get_di(i, n)) + "*(x1^" + str(2*i+1) + "*y1^"+\
                str(2*(n-1)+1) + " + x2^" + str(2*i+1) + "*y2^" +\
                str(2*(n-i)+1) + ")"
        
        func = func + ")/(-" + str(cls.get_ci(i,n))

        # Denominator
        for i in range(1,n+1):
            func = func + str(cls.get_ci(i, n)) + " + " +\
                str(cls.get_ci(i, n)) + "*(x1^" + str(2*i+1) + "*y1^"+\
                str(2*(n-i))+" + x2^" + str(2*i+1) + "*y2^" + str(2*(n-i)) + ")"

        func = func + ")"

        return func 

    @classmethod
    def get_next_function(cls) -> str:
        ret_str = cls.get_function(cls._function_number)
        cls._function_number = cls._function_number + 1
        return ret_str

    # TODO: optimize this so we don't re-calculate values every time
    @classmethod
    def get_ci(cls, i: int, n: int):
        # Error checking
        if i < 0:
            raise Exception("i must be greater than 0, it is " + str(i))

        # Logic
        if i == n:
            return 3/((2*n+1)*(2*n-1))
        else:
            return (3*i/(n-i)*(2*n)*(2*n-1))*(math.comb(2*n,2*i+1))
    
    # TODO: optimize this so we don't re-calculate values every time
    @classmethod
    def get_di(cls, i: int, n: int):
        # Error checking
        if i < 0:
            raise Exception("i must be greater than 0, it is " + str(i))

        # Logic
        return (2-(4*(i-1)/(3*(2*i-2*n-1))))*cls.get_ci(i, n)


# Adds a newline to every line in the list lines
def add_new_lines(lines):
    return list(map(lambda l: l + "\n", lines))

# Adds functions as parameters to the lines as well as Bertini `function`
def add_functions(lines, f_gen, n):
    # Add function_line
    function_line = "function "
    for i in range(0, n):
        function_line = function_line + " f" + str(i)
    function_line = function_line + ";"
    lines.append(function_line)

    # Add functions themselves
    for i in range(1, n + 1):
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
