# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 11:57:59 2016

@author: Richard
修改股票代码和保存文件名称，得到不同股票的价格
"""

import tushare as ts

if __name__ == "__main__":


    #myData = ts.get_h_data('600036',start='2016-01-01',end='2016-12-31') #在这修改股票代码，前复权,从今天数前一年
    #myData.to_csv(r'E:\study\master of TJU\0Subject research\data\core\price_600036.csv')#在这修改保存文件名称
    #myData.to_csv(r'E:\study\master of TJU\0Subject research\code\Important\get_features_of_firm\test_price.csv')#在这修改保存文件名称
    #这个保存在计算数量特征的文件夹里
    calData = ts.get_h_data('600036',start='2015-10-01',end='2016-12-31') #在这修改股票代码，前复权,从今天数前一年
    #calData.to_csv(r'E:\study\master of TJU\0Subject research\code\Important\3_1_get_features_of_firm\test_price.csv')#在这修改保存文件名称