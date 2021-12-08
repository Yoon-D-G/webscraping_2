
class Book_Info:
    def __init__(self, full_book_html, category):
        self.full_book_html = full_book_html
        self.category = category.capitalize()
        self.full_dict = {}
        self.lst = []

    def Title(self):
        return 'Title={}'.format(self.full_book_html.title.text.split('|')[0].strip())

    def Description(self):
        for p in self.full_book_html.find_all('p', attrs={'class': None}):
            return 'Description={}'.format(str(p).strip('<p></p>'))

    def find_table(self):
        self.book_table_data = self.full_book_html.find_all("tr")
        for t in self.book_table_data:
            self.lst.append(t)
        
    def UPC(self):
        self.find_table()
        UPC = self.lst[0].text.strip()[3:]
        return f'UPC={UPC}'

    def Product_type(self):
        self.find_table()
        Product_type = self.lst[1].text.strip()[len('Product_type'):]
        return f'Product_type={Product_type}'

    def Price_excl__tax__(self):
        self.find_table()
        Price_excl__tax__ = self.lst[2].text.strip()[len('Price_excl__tax__'):]
        return f'Price_excl__tax__={Price_excl__tax__}'   
                    
    def Price_incl__tax__(self):
        self.find_table()
        Price_incl__tax__ = self.lst[3].text.strip()[len('Price_incl__tax__'):]
        return f'Price_incl__tax__={Price_incl__tax__}'  

    def Tax(self):
        self.find_table()
        Tax = self.lst[4].text.strip()[len('Tax'):]
        return f'Tax={Tax}'   

    def Availability(self):
        self.find_table()
        Availability = self.lst[5].text.strip()[len('Availability'):]
        return f'Availability={Availability.strip()}'   

    def Number_of_reviews(self):
        self.find_table()
        Number_of_reviews = self.lst[6].text.strip()[len('Number_of_reviews'):]
        return f'Number of reviews={Number_of_reviews.strip()}' 
        