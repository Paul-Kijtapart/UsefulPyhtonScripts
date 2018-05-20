from collections import Counter


class Strings:

    @staticmethod
    def find_the_difference(s, t):
        """
        find the one difference between s and t

        Args:
            s(str): consist of only lowercase letters
            t(str): is generated by random shuffling string s and then add one more letter at a random position

        Returns:
            str: the added letter
        """
        s_counter = Counter(s)

        for c in list(t):

            if c in s_counter:
                s_counter[c] -= 1

                if s_counter[c] < 0:
                    return c
            else:
                return c

    @staticmethod
    def find_the_difference_pro(s, t):
        """
        find the one difference between s and t

        Args:
            s(str): consist of only lowercase letters
            t(str): is generated by random shuffling string s and then add one more letter at a random position

        Returns:
            str: the added letter
        """
        res = 0

        for c in list(s):
            res = res ^ ord(c)

        for c in list(t):
            res = res ^ ord(c)

        return chr(res)

    @staticmethod
    def is_unique(str):
        """
        Return True if the given str has no duplicated char. Otherwise, return False.

        Args:
            str(str):

        Returns:
            (boolean)

        """

        appeared_char = set()

        for c in str:

            if c in appeared_char:
                return False
            else:
                appeared_char.add(c)

        return True

    @staticmethod
    def is_isomorphic(s, t):
        """
        Two strings are isomorphic if the characters in s can be replaced to get t.
        All occurrences of a character must be replaced with another character
        while preserving the order of characters.
        No two characters may map to the same character but a character may map to itself.

        Args:
            s(str):
            t(str):

        Returns:
            (boolean)

        """
        if len(s) != len(t):
            return False

        map = {}

        for i in range(len(s)):

            cs = s[i]
            ct = t[i]

            if cs in map:
                if map[cs] != ct:
                    return False
            else:

                if ct in map.values():
                    return False
                else:
                    map[cs] = ct

        return True
