from glob import glob;
from os import path;

class Util:
    def __init__(self, path, rule, debug = False):
        self.path = path;
        self.rule = rule;
        self.debug = debug;
        self.files = []; # by default all files

    def setPath(self, newpath):
        self.path = newpath;

    def selectedExt(self):
        """
        Insert concerned files into [] => self.files
        """
        for files in self.rules.getObject('extension'):
            self.files.append(glob.glob(os.path.join(self.path, files)));

    def arrayToString(self, array):
        return ''.join(map(str, array));

    def initLetter(self, current):
        """
        Return init letter (only letters, no path)
        """
        # Alphabet A-Z
        alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)];
        array = []; # result

        # Exception, need alphabet
        if (current.isalpha() == False): return None;

        # Convert String to array & upper letters
        current = list(current.upper());

        for i in range(len(self.files)):
            # Check the last letter (int) 25 => "Z"
            lastIndex = alphabet.index(current[len(current) - 1]);

            # ["A", "Z"] => ["A", "A", "A"]
            # ["A", "B"] => ["A", "C"]
            if (lastIndex < 25):
                current[len(current) - 1] = alphabet[lastIndex + 1];
            else:
                current[len(current) - 1] = "A";
                current += ["A"];

            # Add the result to the array
            array.append(self.arrayToString(current));

        return array;

    def initNumber(self, number):
        """
        Amorce chiffre
        """
        return True;

    def prefix(self, prefix):
        """
        Préfixe
        """
        return True;

    def suffix(self, suffix):
        """
        Postefixe
        """
        return True;
