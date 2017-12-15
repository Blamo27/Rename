from glob import glob;
from os import path;
from os.path import basename;

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
        self.files = []; # empty the array
        for files in self.getRule('extension'):
            self.files.append(glob.glob(os.path.join(self.path, files)));

    def arrayToString(self, array):
        """
        Convert array to string
        """
        return ''.join(map(str, array));

    def getRule(self, option):
        """
        Get current rule (for a given option)
        """
        return self.getRule(option);

    def init(self):
        """
        Get the init depending on the current rule
        """
        if (self.getRule('init')) == None): return "";
        return (self.initNumber(), self.initLetter())[self.getRule('init') == 'letter'];

    def initLetter(self):
        """
        Return init letter (only letters, no path)
        """
        # Alphabet A-Z
        alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)];
        array = []; # result

        # Exception, need alphabet
        if (type(current).__name__ != "str" or current.isalpha() == False):
            return None;

        # Convert String to array & upper letters
        current = list(self.getRule('beginwith').upper());

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
        return self.getRule('prefix');

    def suffix(self):
        """
        Return suffix for each file
        """
        return self.getRule('sufix');

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
            filename = basename(self.files)[0]);
            extension = "." + basename(self.files).split(".")[1]);
            final.append(init[i] + prefix + filename + suffix + extension);
