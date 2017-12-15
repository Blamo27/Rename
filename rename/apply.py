import os;
from rename.action import Action;

class Apply(Action):
    def __init__(self, path, rule):
        Action.__init__(self, path, rule);

    def applyRename(self):
        """
        Apply rename for each file
        """
        edit = self.arrayEdit();
        for f in edit: os.rename(self.path + '/' + f[0], self.path + '/' + f[1]);
