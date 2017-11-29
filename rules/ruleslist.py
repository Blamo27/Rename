from rule import Rule;
from ast import literal_eval;

class RulesList:
    def __init__(self, rule):
        self.rule = rule;

    def getRule(self):
        return self.rule;

    def setRule(self, newrule):
        self.rule = newrule;

    def get(self):
        with open("saves/renamer.ini", "r") as get:
            return literal_eval(get.read());

    def load(self):
        with open("saves/renamer.ini", "r") as load:
            return literal_eval(load.read());

    def save(self):
        obj = self.get();
        obj[self.getRule().getObject('filename')] = self.getRule();
        with open("saves/renamer.ini", "w") as save:
            save.write(obj);

    def __str__(self):
        return "Règle actuelle {}".format(self.getRule());
