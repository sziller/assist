
class TxtToMatrix:
    """=== Classname: TxtToMatrix ======================================================================================
    Object to turn string-line into a binary matrix.
    ============================================================================================== by Sziller ==="""
    def __init__(self, string: str, char: str = chr(9608), charset: dict or None = None):
        self.string: str            = str(string)
        self.charset: dict          = charset
        if self.charset is None:
            self.charset = CHARSET
        if 'sc' not in list(self.charset.keys()):
            self.charset['sc']      = [[1, 1, 1, 1],
                                       [1, 0, 0, 1],
                                       [1, 0, 0, 1],
                                       [1, 0, 0, 1],
                                       [1, 0, 0, 1],
                                       [1, 1, 1, 1]]
        
        self.assigned_digits        = []
        self.matrix_to_be_displayed = []
        self.string_to_be_displayed = ""
        self.subst_dict: dict       = {0: " ", 1: char}
        
        self.digit_assign()
        self.display_list_add()
        self.setup_printable()
        
    def digit_assign(self):
        for digit in self.string:
            if digit in list(self.charset.keys()):
                self.assigned_digits.append(self.charset[digit])
            else:
                self.assigned_digits.append(self.charset['sc'])  # substitution character

    def display_list_add(self):
        act_of_row = 0
        tot_of_rows = len(self.assigned_digits[0])
        while act_of_row < tot_of_rows:
            act_row = []
            for digit in self.assigned_digits:
                act_row = act_row + digit[act_of_row]
            act_of_row += 1
            self.matrix_to_be_displayed.append(act_row)

    def setup_printable(self):
        constructed_str = ""
        for line in self.matrix_to_be_displayed:
            row = ""
            for digit in line:
                row += str(self.subst_dict[digit])
            constructed_str += row + "\n"
        self.string_to_be_displayed = constructed_str[:-1]  # deleting last line-break


    def display_string(self):
        print(self.string_to_be_displayed)


CHARSET = {'0': [[0, 0, 1, 1, 0, 0],
                 [0, 1, 0, 0, 1, 0],
                 [0, 1, 0, 0, 1, 0],
                 [0, 1, 0, 0, 1, 0],
                 [0, 1, 0, 0, 1, 0],
                 [0, 0, 1, 1, 0, 0]],
           '1': [[0, 0, 0, 1, 0, 0],
                 [0, 0, 1, 1, 0, 0],
                 [0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 1, 0, 0],
                 [0, 0, 1, 1, 1, 0]],
           '2': [[0, 0, 1, 1, 0, 0],
                 [0, 1, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0],
                 [0, 0, 1, 0, 0, 0],
                 [0, 1, 1, 1, 1, 0]],
           '3': [[0, 0, 1, 1, 0, 0],
                 [0, 1, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 1, 0],
                 [0, 1, 0, 0, 1, 0],
                 [0, 0, 1, 1, 0, 0]],
           '4': [[0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 1, 0],
                 [0, 0, 1, 0, 1, 0],
                 [0, 1, 1, 1, 1, 0],
                 [0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 0]],
           '5': [[0, 1, 1, 1, 1, 0],
                 [0, 1, 0, 0, 0, 0],
                 [0, 1, 1, 1, 0, 0],
                 [0, 0, 0, 0, 1, 0],
                 [0, 1, 0, 0, 1, 0],
                 [0, 0, 1, 1, 0, 0]],
           '6': [[0, 0, 1, 1, 0, 0],
                 [0, 1, 0, 0, 0, 0],
                 [0, 1, 1, 1, 0, 0],
                 [0, 1, 0, 0, 1, 0],
                 [0, 1, 0, 0, 1, 0],
                 [0, 0, 1, 1, 0, 0]],
           '7': [[0, 1, 1, 1, 1, 0],
                 [0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 1, 0, 0],
                 [0, 0, 1, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0]],
           '8': [[0, 0, 1, 1, 0, 0],
                 [0, 1, 0, 0, 1, 0],
                 [0, 0, 1, 1, 0, 0],
                 [0, 1, 0, 0, 1, 0],
                 [0, 1, 0, 0, 1, 0],
                 [0, 0, 1, 1, 0, 0]],
           '9': [[0, 0, 1, 1, 0, 0],
                 [0, 1, 0, 0, 1, 0],
                 [0, 1, 0, 0, 1, 0],
                 [0, 0, 1, 1, 1, 0],
                 [0, 0, 0, 0, 1, 0],
                 [0, 0, 1, 1, 0, 0]],
           ' ': [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]],
           '.': [[0, 0],
                 [0, 0],
                 [0, 0],
                 [0, 0],
                 [0, 1],
                 [0, 0]],
           ',': [[0, 0],
                 [0, 0],
                 [0, 0],
                 [0, 0],
                 [0, 1],
                 [0, 1]],
           ':': [[0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0]],
           'a': [[0, 0, 0, 0, 0],
                 [0, 0, 1, 1, 0],
                 [0, 1, 0, 1, 0],
                 [0, 1, 0, 1, 0],
                 [0, 0, 1, 1, 1],
                 [0, 0, 0, 0, 0]],
           'b': [[0, 1, 0, 0, 0],
                 [0, 1, 1, 0, 0],
                 [0, 1, 0, 1, 0],
                 [0, 1, 0, 1, 0],
                 [0, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0]],
           'c': [[0, 0, 0, 0, 0],
                 [0, 0, 1, 1, 0],
                 [0, 1, 0, 0, 0],
                 [0, 1, 0, 0, 0],
                 [0, 0, 1, 1, 0],
                 [0, 0, 0, 0, 0]],
           'd': [[0, 0, 0, 1, 0],
                 [0, 0, 1, 1, 0],
                 [0, 1, 0, 1, 0],
                 [0, 1, 0, 1, 0],
                 [0, 0, 1, 1, 0],
                 [0, 0, 0, 0, 0]],
           'e': [[0, 0, 0, 0, 0],
                 [0, 0, 1, 1, 0],
                 [0, 1, 0, 0, 1],
                 [0, 1, 1, 1, 0],
                 [0, 0, 1, 1, 1],
                 [0, 0, 0, 0, 0]],
           'f': [[0, 0, 0, 1],
                 [0, 0, 1, 0],
                 [0, 0, 1, 0],
                 [0, 0, 1, 0],
                 [0, 1, 1, 1],
                 [0, 0, 1, 0]],
           'o': [[0, 0, 0, 0, 0],
                 [0, 0, 1, 1, 0],
                 [0, 1, 0, 0, 1],
                 [0, 1, 0, 0, 1],
                 [0, 0, 1, 1, 0],
                 [0, 0, 0, 0, 0]],
           'p': [[0, 0, 0, 0, 0],
                 [0, 1, 1, 1, 0],
                 [0, 1, 0, 0, 1],
                 [0, 1, 1, 1, 0],
                 [0, 1, 0, 0, 0],
                 [0, 1, 0, 0, 0]],
           'r': [[0, 0, 0, 0],
                 [0, 1, 0, 1],
                 [0, 1, 1, 0],
                 [0, 1, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 0, 0]],
           's': [[0, 0, 0, 0, 0],
                 [0, 0, 1, 1, 1],
                 [0, 1, 1, 0, 0],
                 [0, 0, 0, 1, 1],
                 [0, 1, 1, 1, 0],
                 [0, 0, 0, 0, 0]],
           't': [[0, 0, 1, 0],
                 [0, 1, 1, 1],
                 [0, 0, 1, 0],
                 [0, 0, 1, 0],
                 [0, 0, 1, 1],
                 [0, 0, 0, 0]],
           'g': [[0, 0, 0, 0, 0],
                 [0, 0, 1, 1, 1],
                 [0, 1, 0, 0, 1],
                 [0, 0, 1, 1, 1],
                 [0, 0, 0, 0, 1],
                 [0, 0, 1, 1, 0]],
           'h': [[0, 1, 0, 0, 0],
                 [0, 1, 1, 1, 0],
                 [0, 1, 0, 0, 1],
                 [0, 1, 0, 0, 1],
                 [0, 1, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
           'i': [[0, 0, 1, 0],
                 [0, 0, 0, 0],
                 [0, 1, 1, 0],
                 [0, 0, 1, 0],
                 [0, 1, 1, 1],
                 [0, 0, 0, 0]],
           'j': [[0, 0, 1, 0],
                 [0, 0, 0, 0],
                 [0, 1, 1, 0],
                 [0, 0, 1, 0],
                 [1, 0, 1, 0],
                 [0, 1, 0, 0]],
           'k': [[0, 1, 0, 0, 0],
                 [0, 1, 0, 1, 0],
                 [0, 1, 1, 0, 0],
                 [0, 1, 0, 1, 0],
                 [0, 1, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
           'l': [[0, 1, 0],
                 [0, 1, 0],
                 [0, 1, 0],
                 [0, 1, 0],
                 [0, 1, 1],
                 [0, 0, 0]],
           'u': [[0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 1],
                 [0, 1, 0, 0, 1],
                 [0, 1, 0, 0, 1],
                 [0, 0, 1, 1, 1],
                 [0, 0, 0, 0, 0]],
           'm': [[0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 0, 1, 0],
                 [0, 1, 0, 1, 0, 1],
                 [0, 1, 0, 1, 0, 1],
                 [0, 1, 0, 1, 0, 1],
                 [0, 0, 0, 0, 0, 0]],
           'n': [[0, 0, 0, 0, 0],
                 [0, 1, 1, 1, 0],
                 [0, 1, 0, 0, 1],
                 [0, 1, 0, 0, 1],
                 [0, 1, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
           'z': [[0, 0, 0, 0, 0],
                 [0, 1, 1, 1, 1],
                 [0, 0, 0, 1, 0],
                 [0, 0, 1, 0, 0],
                 [0, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0]]
           }

if __name__ == "__main__":
    dp = TxtToMatrix(string="sziller, fight and rezi.", char=chr(9608), charset=None)
    dp.display_string()

