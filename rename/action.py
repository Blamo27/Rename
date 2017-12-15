from glob import glob;
import os;
from os.path import basename;

class Action:
    def __init__(self, path, rule):
        self.path = path;
        self.rule = rule;
        self.files = []; # by default all files

    def setPath(self, newpath):
        self.path = newpath;

    def selectedExt(self):
        """
        Insert concerned files into [] => self.files
        """
        self.files = []; # empty the array

        for filename in os.listdir(self.path):

            if (self.getRule('extension') == None):
                self.files.append(filename);
                continue;

            for extension in self.getRule('extension'):
                if filename.endswith(extension):
                    self.files.append(filename);

    def arrayToString(self, array):
        """
        Convert array to string
        """
        return ''.join(map(str, array));

    def getRule(self, option):
        """
        Get current rule (for a given option)
        """
        return self.rule.getObject(option);

    def init(self):
        """
        Get the init depending on the current rule
        """
        if (self.getRule('init') == None): return None;
        if (self.getRule('init') == 'letter'): return self.initLetter();
        if (self.getRule('init') == 'chiffre'): return self.initNumber();

    def initLetter(self):
        """
        Return init letter (only letters, no path)
        """
        # Alphabet A-Z
        alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)];
        array = []; # result

        current = self.getRule('beginwith').upper();

        print(current)

        # Exception, need alphabet
        if (type(current).__name__ != "str" or current.isalpha() == False):
            current = "A";

        # Convert String to array & upper letters
        current = list(current);

        for i in range(len(self.files)):
            # Check the last letter (int) 25 => "Z"
            lastIndex = alphabet.index(current[len(current) - 1]);

            # Exception first letter
            o = (1, 0)[i == 0];

            # ["A", "Z"] => ["A", "A", "A"]
            # ["A", "B"] => ["A", "C"]
            if (lastIndex < 25):
                current[len(current) - 1] = alphabet[lastIndex + o];
            else:
                current[len(current) - 1] = "A";
                current += ["A"];

            # Add the result to the array
            array.append(self.arrayToString(current));

        return array;

    def initNumber(self):
        """
        Return init numbers
        """
        index = int(self.getRule('beginwith'));
        length = index + len(self.files);

        if (length > 999): return None;

        return ["{0:03}".format(i) for i in range(index, length)];

    def prefix(self):
        """
        Return prefix for each file
        """
        return ("", self.getRule('prefix'))[self.getRule('prefix') != None];

    def suffix(self):
        """
        Return suffix for each file
        """
        return ("", self.getRule('suffix'))[self.getRule('suffix') != None];

    def arrayEdit(self):
        """
        Return an array containing selected rules
        """
        # append concerned files into the "self.files" array
        self.selectedExt();

        # result
        final = [];

        init   = self.init();       # init (number | letters)
        prefix = self.prefix();     # prefix
        suffix = self.suffix();     # suffix

        for i in range(len(self.files)):
            fileInfo = os.path.splitext(self.files[i]);
            filename = fileInfo[0];
            extension = fileInfo[1];

            ini = "" if (init == None) else init[i];

            final.append([self.files[i], ini + prefix + filename + suffix + extension]);

        return final;
