class Article:
    all = []
    def __init__(self, author, magazine, title):

        if not isinstance(title, str):
            raise Exception("Title must be a string")
        if len(title) < 5 or len(title) > 50:
            raise Exception("Title must be between 5 and 50 characters")
        
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
    
     pass

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be an instance of Author class")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be an instance of Magazine class")
        self._magazine = value

class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if len(name.strip()) == 0:
            raise Exception("Name cannot be empty")
        self._name = name


    @property
    def name(self):
        return self._name
    

    @name.setter
    def name(self, value):
        pass

    def articles(self):
         return [article for article in Article.all if article.author == self]


    def magazines(self):
        return list({article.magazine for article in self.articles()})


    def add_article(self, magazine, title): 
        return Article(self, magazine, title)


    def topic_areas(self):
        if len(self.magazines()) == 0:
         return None
        return list({mag.category for mag in self.magazines()})
    

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            return 
        if len(value) < 2 or len(value) > 16:
            return 
        self._name = value

    
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})


    def article_titles(self):
       titles = [article.title for article in Article.all if article.magazine == self]
       return titles if titles else None

    def contributing_authors(self):
       authors = []
       for author in self.contributors():
        count = len([article for article in Article.all if article.magazine == self and article.author == author])
        if count > 2:
            authors.append(author)
       return authors if authors else None