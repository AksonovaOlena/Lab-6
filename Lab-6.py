class Library:
    def init(self):
        self.bookshelf=[]
    def add_home(self, data):
        data=data.split()
        self.bookshelf.append(data)
    def find_author(self, author):
        for data in self.bookshelf:
            if ' '.join(data[:2])==author:
                return ' '.loin(data)
    def find_genre(self, genre):
        for data in self.bookshelf:
            if data[3].splat(':')[1].strip()==genre: 
                return ' '.join(data)
if __name__=='__main__':
    data='''Марк Твен "Пригоди Тома Сойєра" Жанр: роман Джон Чейз "Помилка Тоні Вендіса" Жанр: детектив Стівен Кінг "Переляк" Жанр: фантастика'''
home=Library()
for line in data.split('\n'):
    home.add_home(line)
print(home.find_author('Марк Твен'))
#print(home.find_genre('фантастика'))

            
input()
