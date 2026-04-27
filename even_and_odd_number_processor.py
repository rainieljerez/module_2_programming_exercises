#Jerez, Joaqui Rainiel A.
#BSCpE 1-4
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
        file.close()
#classify to even and odd numbers
    def classify_numbers(self):
        for num in self.numbers:
            if num % 2 == 0:
                self.even_numbers.append(num)
            else:
                self.odd_numbers.append(num)
#method for even
    def write_even_numbers(self):
        file = open("even.txt", "w")
        for num in self.even_numbers:
            file.write(str(num) + "\n")
        file.close()
#method for odd
    def write_odd_numbers(self):
        file = open("odd.txt", "w")
        for num in self.odd_numbers:
            file.write(str(num) + "\n")
        file.close()

processor = EvenAndOddNumberProcesser()
processor.read_numbers()
processor.classify_numbers()
processor.write_even_numbers()
processor.write_odd_numbers()

print("Done! Check even.txt and odd.txt for the results.")