class Sorts:

    @staticmethod
    def sort_anagram(words:list) -> None:
        """

        Args:
            words(str[]): list of words

        Returns:
            str[]: sorted array of words such that anagram stay together

        """

        # if words is empty
        if len(words) == 0:
            return []

        # if words is not empty

        # Build anagram map to group anagram together
        anagram_map = dict()

        for word in words:

            key = "".join(sorted(word))

            # update map with current word
            if key in anagram_map:
                anagram_map[key].append(word)
            else:
                anagram_map[key] = [word]

        # Build list where anagram are put together from map
        res = []

        for key in anagram_map:
            res += anagram_map[key]

        return res
