from tkinter import *;
from rename.utils import *;

def __init__(self, app):
    self.app = app;
    self.init = None;
    self.beginwith = None;
    self.prefix = None;
    self.suffix = None;
    self.extension = None;

def tkTemp(self):
    root = Tk();
    root.title(self.app);

    List = Button(root, text="Lister").grid(row = 0, column = 0, stick = W);
    CreateButton = Button(root, text="Créer").grid(row = 1, column = 0, stick = W);

    Label(root, text = "Nom du répertoire").grid(row = 2, column = 1);
    Entry(root).grid(row = 2, column = 2, stick = W);

    Label(root, text = "Amorce").grid(row = 4, column = 0, stick = W);
    Button(root, text = "Aucune", command = lambda : self.init = None).grid(row = 5, column = 0, stick = W);
    Button(root, text = "Lettre", command = lambda : self.init = "letter").grid(row = 6, column = 0, stick = W);
    Button(root, text = "Chiffre", command = lambda : self.init = "chiffre").grid(row = 6, column = 0, stick = W);

    Label(root, text = "A partir de").grid(row = 8, column = 0, stick = W);
    start = Entry(root).grid(row = 9, column = 0,stick = W);

    Label(root, text = "Préfixe").grid(row = 4, column = 1);
    prefix = Entry(root).grid(row = 5, column = 1);

    originalname = Checkbutton(root, text="Nom original").grid(row=5, column=2);

    Label(root, text = "Postfixe").grid(row = 4, column = 3);
    post = Entry(root).grid(row = 5, column = 3);

    Label(root, text = "Extension concernée").grid(row = 4; column = 4);
    self.extension = Entry(root).grid(row = 5, column = 4);
    
    root.mainloop()
    # RULE & UTILS 
    
def tkRules(self):
    root = Tk()
    root.title("Ajout de règle")

    List = Button(root, text="Lister").grid(row = 0, column = 0, stick = W)
    CreateButton = Button(root, text="Créer").grid(row = 1, column = 0, stick = W)

    Label(root, text="Créer une règle").grid(row=1, column=2)
    Label(root, text = "Nom de la règle").grid(row = 2, column = 1)
    Entry(root).grid(row = 2, column = 2, stick = W)

    Label(root, text = "Amorce").grid(row = 4, column = 0, stick = W)
    none = Button(root, text="Aucune", command=lambda :self.init).grid(row=5, column=0, stick=W)
    Letter = Button(root, text="Lettre", command=lambda :self.init).grid(row=6, column=0, stick=W)
    Number = Button(root, text="Chiffre", command=lambda :self.init).grid(row=7, column=0, stick=W)

    Label(root, text = "A partir de").grid(row = 8, column = 0, stick = W)
    start = Entry(root).grid(row = 9, column = 0,stick = W)

    Label(root, text = "Préfixe").grid(row = 4, column = 1)
    prefix = Entry(root).grid(row = 5, column = 1)

    originalname = Checkbutton(root, text="Nom original").grid(row=5, column=2)

    Label(root, text = "Postfixe").grid(row = 4, column = 3)
    post = Entry(root).grid(row = 5, column = 3)

    Label(root, text = "Extension concernée").grid(row = 4, column = 4);
    self.extension = Entry(root).grid(row = 5, column = 4);

    root.mainloop()
