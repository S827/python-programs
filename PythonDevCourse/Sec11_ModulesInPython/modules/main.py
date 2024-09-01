import utility
from utility import multiply, divide
# from utility import *
# from shopping.more_shopping.shopping_cart import buy
from shopping.more_shopping import shopping_cart
from pythonBuiltInModules_175 import randomFunc
import sysModule
if __name__ == '__main__':
      print('Please run this')
      print(multiply(10, 22))

      print(divide(300, 15))

      # print(buy)

      # print(buy('car'))
      print(shopping_cart
            .buy('car'))
      print(__name__)
      print(type(utility.st1))
