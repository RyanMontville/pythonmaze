class Words():
    def __init__(self):
        self.input_string = ""
        self.line_one = ""
        self.line_two = ""

    def prompt_for_words(self):
        word_start = input("\nType a word or phrase 12 letter long or less (not including spaces): ")
        is_word_good = False
        while not is_word_good:
            word_no_spaces = word_start.replace(" ","")
            if len(word_no_spaces) == 0:
                print("Error. Please enter at least 1 letter.")
                word_start = input("\nType a word or phrase 12 letter long or less (not including spaces): ")
            elif len(word_no_spaces) > 12:
                print(f"Error! Word or Phase can't be longer than 12 letters (not including spaces). You entered {len(word_start)} letters.")
                word_start = input("\nType a word or phrase 12 letter long or less (not including spaces): ")
            elif len(word_no_spaces) == 12:
                self.input_string =  word_no_spaces
                is_word_good = True
            else:
                self.input_string =  word_start.lower()
                is_word_good = True

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
        self.line_one = line_one_final
        self.line_two = line_two_final