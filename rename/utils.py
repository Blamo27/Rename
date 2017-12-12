class Util:
    def __init__(self, current, debug = False):
        self.current = current;
        self.debug = debug;

    def setCurrent(self, newcurrent):
        self.current = newcurrent;

    def initLetter(self, beginwith):
        """
        Amorce lettre
        """
        return True;

    def initNumber(self, beginwith):
        """
        Amorce chiffre
        """
        return True;

    def prefix(self, ):
        """
        Préfixe
        """
        return True;

    def suffix(self):
        """
        Postefixe
        """
        return True;

    def selectedExt(self):
        """
        Extension
        """
        return True;
