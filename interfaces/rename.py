from tkinter import *;
from rules.rule import Rule;
from rename.action import Action;
from utils.browser import Browser;

class RenameInterface:

    def __init__(self, app):
        self.app = app;
        self.params = {
            'init': None,
            'beginwith': None,
            'prefix': None,
            'suffix': None,
            'extension': None,
            'dirname': None
        };

    def tkTemp(self):
        root = Tk();
        root.title(self.app);

        self.set('init', StringVar());
        self.set('dirname', StringVar());
        self.set('prefix', StringVar());
        self.set('suffix', StringVar());
        self.set('beginwith', StringVar());
        self.set('extension', StringVar());

        # List | Create
        Button(root, text="Lister").grid(row = 0, column = 0, stick = W);
        Button(root, text="Créer").grid(row = 1, column = 0, stick = W);

        # Directory name
        Label(root, text = "Nom du répertoire").grid(row = 2, column = 1);
        Entry(root, textvariable = self.get('dirname')).grid(row = 2, column = 2, stick = W);
        Button(root, text = "Choisir un chemin", command = lambda: self.setPath()).grid(row = 2, column = 3, stick = W);

        # Init
        Label(root, text = "Amorce").grid(row = 4, column = 0, stick = W);
        Button(root, text = "Aucune", command = lambda: self.set('init', None)).grid(row = 5, column = 0, stick = W);
        Button(root, text = "Lettre", command = lambda: self.set('init', 'letter')).grid(row = 6, column = 0, stick = W);
        Button(root, text = "Chiffre", command = lambda: self.set('init', 'chiffre')).grid(row = 7, column = 0, stick = W);

        # Begin with
        Label(root, text = "A partir de").grid(row = 8, column = 0, stick = W);
        start = Entry(root).grid(row = 9, column = 0,stick = W);

        # Prefix
        Label(root, text = "Préfixe").grid(row = 4, column = 1);
        prefix = Entry(root, textvariable = self.get('prefix')).grid(row = 5, column = 1);

        # Suffix
        Label(root, text = "Postfixe").grid(row = 4, column = 2);
        suffix = Entry(root, textvariable = self.get('suffix')).grid(row = 5, column = 2);

        # Concerned extension(s)
        Label(root, text = "Extension concernée").grid(row = 4, column = 3);
        self.extension = Entry(root).grid(row = 5, column = 3);

        # Rename button
        Rename = Button(root, text = "Renommer", command = lambda : self.rename()).grid(row = 7, column = 3);
        root.mainloop();

    def setPath(self):
        """
        Define current path with Browser (utils)
        """
        file = Browser();
        self.get('dirname').set(file.get());

    def set(self, option, value):
        """
        Set a value (object)
        """
        self.params[option] = value;

    def get(self, option):
        """
        Get a value (object)
        """
        return self.params[option];

    def rename(self):

        init = (self.get('init').get(), None)[self.get('init').get() == ""];
        extension = (self.get('extension').get(), None)[self.get('extension').get() == ""];

        # Rule & Util
        rule = Rule(init, self.get('beginwith').get(), self.get('prefix').get(),
                    'test', self.get('suffix').get(), extension);

        util = Action(self.get('dirname').get(), rule);

        # Simulation
        util.arrayEdit();
