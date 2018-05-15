class Sorts:

    @staticmethod
    def sort_anagram(words: list) -> list:
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

            # update map with base_color word
            if key in anagram_map:
                anagram_map[key].append(word)
            else:
                anagram_map[key] = [word]

        # Build list where anagram are put together from map
        res = []

        for key in anagram_map:
            res += anagram_map[key]

        return res

    @staticmethod
    def sort_colors(colors):
        """
        sorted the given colors in-place
        the same color are adjacent, with the colors in the order red, white and blue.
        we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

        Args:
            colors(List[int]): list of colors codes
                               0 = red,
                               1 = white
                               2 = blue

        Returns:

        """
        i = 1

        while i < len(colors):

            j = i - 1

            base_color = colors[i]

            while j >= 0 and colors[j] > base_color:
                colors[j + 1] = colors[j]
                j -= 1

            colors[j + 1] = base_color

            i += 1
