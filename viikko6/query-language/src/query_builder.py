
from matchers import And, All, Not, Or
from matchers import PlaysIn, HasAtLeast, HasFewerThan


class Query:
    def __init__(self, matcher=None):
        if matcher is None:
            self._matcher = All()
        else:
            self._matcher = matcher

    def andMatch(self, matcher):
        if self._matcher is None:
            return Query(matcher)
        else:
            return Query(And(self._matcher, matcher))

    def all(self):
        return Query(All())

    def notMatch(self):
        return Query(Not(self._matcher))
        
    def get(self):
        return self._matcher


class QueryBuilder:
    def __init__(self, query=None):
        if query is None:
            self.query = Query()
        else:
            self.query = query

    def playsIn(self, team):
        return QueryBuilder(self.query.andMatch(PlaysIn(team)))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(self.query.andMatch(HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(self.query.andMatch(HasFewerThan(value, attr)))

    def all(self):
        return QueryBuilder(self.query.all())

    def notMatch(self):
        return QueryBuilder(self.query.notMatch())

    def build(self):
        return self.query.get()