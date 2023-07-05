class Trie:

    def __init__(self):
        # Have just use a dict of each character
        # dict of the dict of dict.
        self.dict = {}

    def insert(self, word: str) -> None:
        length = len(word)
        current_dict = self.dict
        for x in range(length):
            char = word[x]
            next_dict = current_dict.get(char)
            if next_dict is None:
                # Create new dict
                current_dict[char] = {}
            current_dict = current_dict.get(char)
        current_dict["end"] = True
        # print(self.dict)
        # The last one: Put end = True?

    def search(self, word: str) -> bool:
        length = len(word)
        current_dict = self.dict
        for x in range(length):
            char = word[x]
            next_dict = current_dict.get(char)
            current_dict = next_dict
            if next_dict is None:
                return False
        # end = True?
        exist = current_dict.get("end")
        if exist:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        length = len(prefix)
        current_dict = self.dict
        for x in range(length):
            char = prefix[x]
            next_dict = current_dict.get(char)
            current_dict = next_dict
            if next_dict is None:
                return False
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
obj.search("apple")
obj.search("app")
obj.startsWith("app")
obj.insert("app")
print(obj.search("app"))

# Submission Verified and accepted on leetcode.