from tkinter import *;
from rules.rule import Rule;

from rename.apply import Apply;
from rename.action import Action;

from utils.animatedgif import *;
from utils.browser import Browser;
from utils.tabulate import tabulate;

class RenameInterface:

    def __init__(self, app):
        self.app = app;
        self.simulation = False;
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
        root.geometry("870x230+300+300");
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
        Button(root, text = "Aucune", command = lambda: self.get('init').set(None)).grid(row = 5, column = 0, stick = W);
        Button(root, text = "Lettre", command = lambda: self.get('init').set('letter')).grid(row = 6, column = 0, stick = W);
        Button(root, text = "Chiffre", command = lambda: self.get('init').set('chiffre')).grid(row = 7, column = 0, stick = W);

        # Begin with
        Label(root, text = "A partir de").grid(row = 8, column = 0, stick = W);
        Entry(root, textvariable = self.get('beginwith')).grid(row = 9, column = 0,stick = W);

        # Prefix
        Label(root, text = "Préfixe").grid(row = 4, column = 1);
        Entry(root, textvariable = self.get('prefix')).grid(row = 5, column = 1);

        # Suffix
        Label(root, text = "Postfixe").grid(row = 4, column = 2);
        Entry(root, textvariable = self.get('suffix')).grid(row = 5, column = 2);

        # Concerned extension(s)
        Label(root, text = "Extension concernée").grid(row = 4, column = 3);
        Entry(root, textvariable = self.get('extension')).grid(row = 5, column = 3);

        # Rename button
        Button(root, text = "Renommer", command = lambda : self.rename()).grid(row = 7, column = 3);

        # Create canvas (1 hour stabilization)
        gif = AnimatedGif(root, 'ezgif.com-optimize.gif', 0.05);
        gif.place(x = 500, y = 0);
        gif.start();

        # Checkbox simulate
        Checkbutton(root, text="Simuler", command = lambda: self.simulate()).grid(row = 9, column = 3);
        root.mainloop();

    def setPath(self):
        """
        Define current path with Browser (utils)
        """
        file = Browser();
        self.get('dirname').set(file.get());

    def simulate(self):
        """
        Enable / disable simulation mode
        """
        self.simulation = not self.simulation;

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
        extension = ([x.strip() for x in self.get('extension').get().split(',')], None)[self.get('extension').get() == ""];
        beginwith = self.get('beginwith').get();
        prefix = self.get('prefix').get();
        suffix = self.get('suffix').get();

        if (beginwith == ""): beginwith = ("001", "A")[init == "letter"];

        # Rule & Util
        rule = Rule(init, beginwith, prefix, 'test', suffix, extension);


        if (self.simulation):
            action = Action(self.get('dirname').get(), rule);

            # Simulation
            header = ["Fichier original", "Renommé"];
            final = action.arrayEdit();

            # Debug (simulate with tabulate)
            print("");
            print(tabulate(final, header, tablefmt="simple"));

            return;

        rename = Apply(self.get('dirname').get(), rule);
        rename.applyRename();
