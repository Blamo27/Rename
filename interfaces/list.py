from tkinter import *;
from rules.ruleslist import RulesList;

class LoadInterface:

    def __init__(self, rename):
        self.rename = rename;

    def onselect(self, evt):
        w = evt.widget;
        index = int(w.curselection()[0]);
        value = w.get(index);

        load = self.load()[value];
        for i in load:
            self.rename.get(i).set(load[i]);

        print('Vous avez séléctionné la règle "%s"' % (value));

    def tkList(self):
        root = Tk();
        root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()));
        root.title('Sauvegarder');

        listbox = Listbox(root);
        rules = self.load()
        for i, k in enumerate(rules):
            listbox.insert(i, k);
        listbox.pack();

        listbox.bind('<<ListboxSelect>>', self.onselect);

        root.mainloop();

    def load(self):
        # load rules
        rules = RulesList('');
        return rules.load();
