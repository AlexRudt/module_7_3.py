class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def find(self,word):
        places = {}
        for value, key in get_all_words().items():
            if word.lower() in key:
                places[value] = key.index(word.lower()) + 1
        return places

    def count(self,word):
        counters = {}
        for value, key in get_all_words().items():
            words_count = key.count(word.lower())
            counters[value] = words_count
        return counters


    def get_all_words(self):
        all_words = {}
        l = ''
        punc = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for self.file_names in self.file_names:
            with open(self.file_names, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                for i in line:
                    if i in punc:
                        line = line.replace(i,'')
                l = l + line
            all_words.update({self.file_names:l.split()})
        return all_words






finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
