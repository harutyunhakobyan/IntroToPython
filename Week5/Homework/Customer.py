import Productcheck

def buy(product, num, price):
    if Productcheck.check(product, num) == True:
        print('You bought', product, 'and spent', num*price)
    else:
        print('Sorry! We are out of this product.')



def main():
    buy('candy', 3, 2000)
    buy('juice', 6, 800)
    buy('pen', 10, 100)



if __name__ == '__main__':
    main()