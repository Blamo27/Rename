class Rule:
    def __init__(self, init, beginwith, prefix, rulename, suffix, extension, original):
        self.object = {
            'init': init,
            'beginwith': beginwith,
            'prefix': prefix,
            'rulename': rulename,
            'suffix': suffix,
            'extension': extension, # (*.ext, *.jgp)
            'original': original
        };

    def getObject(self, option):
        return self.object[option];

    def setObject(self, option, value):
        self.object[option] = value;

    def getAll(self):
        return self.object;

    def __str__(self):
        return "Amorce: {}\r\nApartir de: {}\r\nPrefix: {}\r\nNom de la règle: {}\r\nSuffix: {}\r\nExtension: {}\r\nOriginal: {}".format(
                self.object['init'], self.object['beginwith'], self.object['prefix'],
                self.object['rulename'], self.object['suffix'], self.object['extension'],
                self.object['original']
        );
