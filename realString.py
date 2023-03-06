from functools import total_ordering


@total_ordering
class RealString:
    def __init__(self, string):
        self.some_string = str(string)
    def __eq__(self, other):
        if not isinstance(other, RealString):
            other = RealString(other)
        return len(self.some_string) == len(other.some_string)
    def __lt__(self, other):
        if not isinstance(other, RealString):
            other = RealString(other)
        return len(self.some_string) < len(other.some_string)

    