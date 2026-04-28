#Jerez, Joaqui Rainiel A.
#BSCpE 1-4
#class
class WriteToFile:
    def __init__(self, filename):
        self.filename = filename

    def write_text(self):
        with open(self.filename, "w") as f:
            while True:
                text = input("Enter a text: ")
                f.write(text + "\n")

                more_text = input("Are there more lines? (y/n) ").strip().lower()
                if more_text != "y":
                    break

        print(f"\nText saved to {self.filename}")

writer = WriteToFile("mylife.txt")
writer.write_text()



