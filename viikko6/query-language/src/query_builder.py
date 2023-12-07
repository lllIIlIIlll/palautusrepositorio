from matchers import All, And, PlaysIn, HasAtLeast, HasFewerThan, Not, Or

class QueryBuilder:
    def __init__(self, matcher = All()):
        self._matcher_olio = matcher

    def playsIn(self, team):
        return QueryBuilder(And(self._matcher_olio, PlaysIn(team)))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._matcher_olio, HasAtLeast(value, attr)))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._matcher_olio, HasFewerThan(value, attr)))
    
    def notPlaysIn(self, team):
        return QueryBuilder(And(self._matcher_olio, Not(PlaysIn(team))))
    
    def notHasAtLeast(self, value, attr):
        return QueryBuilder(And(self._matcher_olio, Not(HasAtLeast(value, attr))))
    
    def notHasFewerThan(self, value, attr):
        return QueryBuilder(And(self._matcher_olio, Not(HasFewerThan(value, attr))))
    
    def oneOf(self, m1, m2):
        return QueryBuilder(Or(m1, m2))
    
    def build(self):
        return self._matcher_olio