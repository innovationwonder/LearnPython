'''
练习一 变量的定义和使用
定义两个变量分别为美元和汇率
通过搜索引擎找到美元兑人民币汇率
使用Python计算100美元兑换的人民币数量并用print( )进行输出
'''
dollars = 100 # 定义美元
exchange_rate = 6.9428 # 定义汇率
print('{dol} 美元兑 {yuan} 人民币'.format(dol=dollars, yuan=dollars*exchange_rate))