class Rule:
    def __init__(self, init, beginwith, prefix, filename, suffix, extension):
        self.object = {
            'init': init,
            'beginwith': beginwith,
            'prefix': prefix,
            'filename': filename,
            'suffix': suffix,
            'extension': extension # (*.ext, *.jgp)
        };

    def getObject(self, option):
        return self.object[option];

    def setObject(self, option, value):
        self.object[option] = value;

    def __str__(self):
        return "Amorce: {}\r\nApartirde: {}\r\nPrefix: {}\r\nFilename: {}\r\nSuffix: {}\r\nExtension: {}".format(
                self.object['init'], self.object['beginwith'], self.object['prefix'],
                self.object['filename'], self.object['suffix'], self.object['extension']
        );
