import pkg_resources
import json

class Cypher:

    def __init__(self):
        self.FUNCTIONS = [
            "ABS",
            "ACOS",
            "ALL",
            "ALLSHORTESTPATHS",
            "ANY",
            "ASIN",
            "ATAN",
            "ATAN2",
            "AVG",
            "CEIL",
            "COALESCE",
            "COLLECT",
            "COS",
            "COT",
            "COUNT",
            "DEGREES",
            "E",
            "ENDNODE",
            "EXP",
            "EXTRACT",
            "FILTER",
            "FLOOR",
            "HAS",
            "HAVERSIN",
            "HEAD",
            "ID",
            "KEYS",
            "LABELS",
            "LAST",
            "LEFT",
            "LENGTH",
            "LOG",
            "LOG10",
            "LOWER",
            "LTRIM",
            "MAX",
            "MIN",
            "NODE",
            "NODES",
            "NONE",
            "PERCENTILECONT",
            "PERCENTILEDISC",
            "PI",
            "RADIANS",
            "RAND",
            "RANGE",
            "REDUCE",
            "REL",
            "RELATIONSHIP",
            "RELATIONSHIPS",
            "REPLACE",
            "RIGHT",
            "ROUND",
            "RTRIM",
            "SHORTESTPATH",
            "SIGN",
            "SIN",
            "SINGLE",
            "SPLIT",
            "SQRT",
            "STARTNODE",
            "STDEV",
            "STDEVP",
            "STR",
            "SUBSTRING",
            "SUM",
            "TAIL",
            "TAN",
            "TIMESTAMP",
            "TOFLOAT",
            "TOINT",
            "TRIM",
            "TYPE",
            "UPPER"
        ]

        self.KEYWORDS = [
            "AND",
            "AS",
            "ASC",
            "ASCENDING",
            "ASSERT",
            "BY",
            "CASE",
            "COMMIT",
            "CONSTRAINT",
            "CREATE",
            "CSV",
            "CYPHER",
            "DELETE",
            "DESC",
            "DESCENDING",
            "DISTINCT",
            "DROP",
            "ELSE",
            "END",
            "EXPLAIN",
            "FALSE",
            "FIELDTERMINATOR",
            "FOREACH",
            "FROM",
            "HEADERS",
            "IN",
            "INDEX",
            "IS",
            "LIMIT",
            "LOAD",
            "MATCH",
            "MERGE",
            "NOT",
            "NULL",
            "ON",
            "OPTIONAL",
            "OR",
            "ORDER",
            "PERIODIC",
            "PROFILE",
            "REMOVE",
            "RETURN",
            "SCAN",
            "SET",
            "SKIP",
            "START",
            "THEN",
            "TRUE",
            "UNION",
            "UNIQUE",
            "UNWIND",
            "USING",
            "WHEN",
            "WHERE",
            "WITH",
            "XOR"
        ]

        self.markov = json.loads(open(pkg_resources.resource_filename(__name__, "markov.json")).read())

    def words(self):
        return sorted(self.FUNCTIONS + self.KEYWORDS)

    def most_probable_next_keyword(self, last_word):
        row = self.markov[last_word]
        return sorted(row, key=row.get, reverse=True)