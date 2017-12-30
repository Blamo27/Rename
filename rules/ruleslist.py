from ast import literal_eval;

class RulesList:
    def __init__(self, rule):
        self.rule = rule;

    def getRule(self):
        return self.rule;

    def setRule(self, newrule):
        self.rule = newrule;

    def empty(self):
        with open("saves/renamer.ini", "w") as e:
            e.write("{}");

    def load(self):
        with open("saves/renamer.ini", "r") as load:
            try:
                read = literal_eval(load.read());
                return read;
            except SyntaxError:
                return {};

    def save(self):
        rules = self.load();
        name = self.getRule().getObject('rulename');
        rules[name] = self.getRule().getAll();
        print(rules);
        with open("saves/renamer.ini", "w") as s:
            s.write(str(rules));

    def __str__(self):
        return "Règle actuelle {}".format(self.getRule());
