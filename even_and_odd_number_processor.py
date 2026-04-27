class EvenAndOddNumberProcesser:
    def __init__(self):
        self.numbers = []
        self.even_numbers = []
        self.odd_numbers = []

#open the file
    def read_numbers(self):
        file = open('numbers.txt', 'r')
        for line in file:
            self.numbers.append(int(line.strip()))
        file.close
#classify to even and odd numbers
#method for even
#method for odd