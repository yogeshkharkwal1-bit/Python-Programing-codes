class book:
    count=0
    def __init__(self,title,auther,reviews):
        self.title=title
        self.auther=auther 
        self.reviews=reviews
        book.count += 1

    def get_reviews(self):
        return self.reviews
        



book1=book("oops","sharadha mam","nice to learn")               
book2=book("oops1","sharadha mam","good")               
book3=book("oops2","sharadha mam","avg")               
book4=book("oops3","sharadha mam","aammmm")     


print(f"the name of book is: {book1.title} and its auther is: {book1.auther}")
print(f" the total useges of reviews are: {book.count}")
# print(f" the review of {book1.title} is : {book1.get_reviews()}")

def all_reviews():
   print(f" the review of all books are: {book1.get_reviews()}, {book2.get_reviews()}, {book3.get_reviews()}, {book4.get_reviews()}")

print(all_reviews())


