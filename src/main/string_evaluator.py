# Created by Leon Hunter at 3:57 PM 10/23/2020
class StringManipulator(object):
    def get_hello_world(self):
        return "Hello World"

    def concatenate(self, value_to_be_added_to, value_to_add):
        return (str(value_to_be_added_to) + str(value_to_add))

    def substring_inclusive(self, string_to_fetch_from, starting_index, ending_index):
        return slice(string_to_fetch_from, starting_index, ending_index)

    def substring_exclusive(self, string_to_fetch_from, starting_index, ending_index):
        return slice(string_to_fetch_from, starting_index + 1, ending_index - 1)

    def compare(self, first_value, second_value):
        is_equal = eval(first_value) == eval(second_value)
        return is_equal

    def get_middle_character(self, string_to_fetch_from):
        return string_to_fetch_from[len(string_to_fetch_from) / 2]

    def get_first_word(self, string_to_fetch_from):
        return string_to_fetch_from.split()[0]

    def get_second_word(self, string_to_fetch_from):
        return string_to_fetch_from.split()[1]

    def reverse(self, string_to_be_reversed):
        return string_to_be_reversed[::-1]
