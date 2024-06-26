# # OVERALL TASKS
# 1. Store input data to txt file
# 2. Read input data from file
# 3. Calculate points


class Scratchcards:
    # initialize
    def __init__(self, file_path):
        self.file_path = file_path

    # fetch data from txt file
    def fetch_data(self):
        # open and close file after use
        with open(self.file_path, 'r') as file:
            # .read() reads file as a single string
            data = file.read().strip().split("\n")
        return data

    # process data/symbols and calculate points
    def process_data(self, line):
        # make an array/list of elements for each line
        numbers_list = line.split()
        # remove the label/first two elements. Start from element 3
        numbers_list = numbers_list[2:]
        # select only the winning numbers, everything before | index
        # convert winning numbers into integers and store them into a list
        winning_numbers = list(map(int, numbers_list[:numbers_list.index('|')]))
        # select my numbers from numbers list, everything after | index
        my_numbers = list(map(int, numbers_list[numbers_list.index('|') + 1:]))
        return winning_numbers, my_numbers

    # calculate points per card
    def calculate_card_points(self, winning_numbers, my_numbers):
        # initialize
        match_count = 0
        card_total = 0

        # iterate through all numbers from my numbers
        # if my number == winning number add point to card total
        for number in my_numbers:
            if number in winning_numbers:
                match_count += 1
                if match_count == 1:
                    card_total = 1
                else:
                    card_total *= 2
        return card_total

    # calculate total points
    def calculate_total_points(self):
        # initialize
        cards = self.fetch_data()
        total = 0

        for card in cards:
            winning_numbers, my_numbers = self.process_data(card)
            total += self.calculate_card_points(winning_numbers, my_numbers)

        return total

# if script run directly, which it is
if __name__ == "__main__":
    file_path = "input_data.txt"
    # enter file_path for class (__init__)
    scratchcards = Scratchcards(file_path)
    total = scratchcards.calculate_total_points()
    print(f"My total is {total} points")
