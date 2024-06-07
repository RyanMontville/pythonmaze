class Words():
    def __init__(self):
        self.input_string = ""
        self.line_one = ""
        self.line_two = ""

    def check_phrase(self,phrase_to_check):
        print(phrase_to_check)
        phrase_no_spaces = phrase_to_check.replace(" ","")
        if len(phrase_no_spaces) == 0:
            return (False, "Error! Please enter at least 1 letter.\nType a word or phrase 12 letter long or less (not including spaces):")
        elif len(phrase_no_spaces) > 12:
            return (False, "Error! Word or Phrase is too long.\nType a word or phrase 12 letter long or less (not including spaces):")
        elif len(phrase_no_spaces) == 12:
            self.input_string =  phrase_no_spaces
            return (True,"")
        else:
            self.input_string =  phrase_to_check.lower()
            return (True,"")

    def set_word(self, word_input):
        self.input_string = word_input

    def format_string(self):
        words = self.input_string.split()
        line_one = ""
        if len(words) == 1:
            line_one = self.input_string[:6]
            line_two = self.input_string[6:]
        elif len(words[0]) == 6:
            line_one = words[0]
            line_two = self.input_string[6:]
        elif len(words[0]) + len(words[1]) == 6:
            line_one = words[0] + words[1]
            line_two = self.input_string[len(line_one) + 1:]
        elif len(words[0]) + len(words[1]) < 6:
            line_one = words[0] + " " + words[1]
            line_two = self.input_string[len(line_one):]
        else:
            line_one = words[0]
            line_two = self.input_string[len(line_one):]
        line_one_final = line_one.strip()
        line_two_final = line_two.strip()
        while len(line_one_final) < 6:
            line_one_final += "-"
        while len(line_two_final) < 6:
            line_two_final += "-"
        if len(line_two_final) > 6:
            no_spaces = self.input_string.replace(" ","")
            self.line_one = no_spaces[0:6]
            second_line = no_spaces[6:]
            while len(second_line) < 6:
                second_line += "-"
            self.line_two = second_line
        else:
            self.line_one = line_one_final
            self.line_two = line_two_final