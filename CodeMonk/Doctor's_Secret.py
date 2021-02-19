#Cheeku will take medicine from him only
# if Length of name of Book is lesser than or equal to 23 and
# number of pages in book is between 500 to 1000.
L,P=map(int,input().split(" "))
if L<=23 and P>=500 and P<=1000:
    print("Take Medicine")
else:
    print("Don't take Medicine")