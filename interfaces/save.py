from tkinter import *;
from rules.ruleslist import RulesList;

class SaveInterface:

    def __init__(self, rule):
        self.name = None;
        self.rule = rule;

    def tkSave(self):
        root = Tk();
        root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()));
        root.geometry("260x60");
        root.title('Sauvegarder');

        self.name = StringVar(root, value = "");

        label = Label(root, text = "Nom de la règle");
        label.grid(row = 1, column = 1);

        entry = Entry(root, textvariable = self.name);
        entry.grid(row = 1, column = 2, stick = W);

        button = Button(root, text = "Sauvegarder", command = lambda: self.save());
        button.grid(row = 2, column = 2, stick = W);

        root.mainloop();

    def save(self):
        # define rulename
        self.rule.setObject('rulename', self.name.get());
        rules = RulesList(self.rule);

        # save the rule
        rules.save();
