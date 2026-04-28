#Jerez, Joaqui Rainiel A.
#BSCpE 1-4
class CubeAndSquareInteger:
    def __init__(self, source_file):
        self.source_file = source_file
        self.integers = []
#read file
    def read_integers(self):
        with open (self.source_file, "r") as f:
            self.integers = [int(line.strip()) for line in f if line.strip()]
        print(f"Read {len(self.integers)} integers: {self.integers}")
#method for square
    def write_squares(self, output_file = "double.txt"):
        even = [n ** 2 for n in self.integers if n % 2 == 0]
        with open(output_file, "w") as f:
            for value in even:
                f.write(f"{value}\n")
        print(f"double.txt contains squares of even numbers: {even}")
#method for cube
    def write_cubes(self, output_file = "triple.txt"):
        odd = [n ** 3 for n in self.integers if n % 2 != 0]
        with open (output_file, "w") as f:
            for value in odd:
                f.write(f"{value}\n")
        print(f"triple.txt contains cubes of odd numbers: {odd}")
#process for the methods
    def process(self):
        self.read_integers()
        self.write_squares()
        self.write_cubes()
#process the file
if __name__ == "__main__":
    processor = CubeAndSquareInteger("integers.txt")
    processor.process()
