class Rule:
    def __init__(self, init, beginwith, prefix, filename, suffix, extension):
        self.object = {
            init: self.init,
            beginwith: self.beginwith,
            prefix: self.prefix,
            filename: self.filename,
            suffix: self.suffix,
            extension: self.extension
        };

    def getObject(self, option):
        return self.object[option];

    def setObject(self, option, value):
        self.object[option] = value;

    def __str__(self):
        return "Amorce: {}\r\nApartirde: {}\r\nPrefix: {}\r\nFilename: {}\r\nSuffix: {}\r\nExtension: {}".format(
                self.init, self.beginwith, self.prefix, self.filename, self.suffix, self.extension
        );
