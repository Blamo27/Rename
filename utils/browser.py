# Interface nav' pour fichier
from tkinter.filedialog import *;

class Browser:

    def __init__(self, debug = False):
        self.debug = debug;

        # Ouvre le browser sans afficher de fenêtre Tk
        Tk().withdraw();
        self.file = askdirectory();

    def get(self):
        return self.file;
