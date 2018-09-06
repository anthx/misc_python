from tkinter import filedialog, Tk
root = Tk()

class File(object):
    
    def load(self, filename):
        f = open(filename, 'r')
        contents = []
        for line in f:
            contents.append(line)
        f.close()
        return contents

    def get_contents(self):
        return self.contents

    def __init__(self, filename):
        self.filename = str(filename)
        self.contents = self.load(self.filename)

class Differences(object):
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2

        differences = []

        for i, line in enumerate(self.file1):
            if self.file2[i] != self.file1[i]:
                differences.append("line " + str(i) + str(self.file1[i])
                                   + ", " + str(self.file2[i]))

class Missing(object):
    """
    holds lines in file1 that aren't in file2
    """
    def __init__(self, file1cont, file2cont):
        self.file1 = file1cont
        self.file2 = file2cont

        #sort both files internally first
        self.file1.sort()
        self.file2.sort()

        self.missing = []

        for i, line in enumerate(self.file1):
            if line not in self.file2:
                self.missing.append(line)

    def get_missing_lines(self):
        return self.missing

def find_missing():
    print("First File")
    file1path = filedialog.askopenfilename()
    print(file1path)
    file1 = File(file1path)
    
    print("Second File")
    file2path = filedialog.askopenfilename()
    print(file2path)
    file2 = File(file2path)
    
    missing_lines = Missing(file1.get_contents(), file2.get_contents())

    path_to_save = filedialog.asksaveasfilename()    

    f = open(path_to_save, "w")

    for line in missing_lines.get_missing_lines():
        f.write(line)
    f.close()
    print("Writen to", path_to_save)


find_missing()
