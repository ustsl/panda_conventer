#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Библиотека преобразования строк


###Краткая документация###

#Вызов - Pandaset
#Данные передачи - data, headers, dimensions, metrics 
#То есть - Датасет из библиотеки Метрика Пресет, Заголовки пандас, количество значений датасета, количество метрик датасета)
#Готовые данные вызываются командой - dataset


class Listdata:

    def __init__ (self, stringdata, dimensions, metrics):
        self.stringdata = stringdata
        self.dimensions = dimensions
        self.metrics = metrics
        self.list_datas = []

    def list_datas_maker(self):

        ### Рабочие переменные

        ld = [] #лист значений
        lm = [] #лист метрик

        d = 0 #стартовое значение
        m = 0 #стартовой значений



        while self.dimensions + self.metrics != 0:
            if self.dimensions != 0:               

                ld.append (self.stringdata['dimensions'][d]['name'])

                self.dimensions -= 1  
                d += 1

            if self.metrics != 0:

                lm.append (self.stringdata['metrics'][m])

                self.metrics -= 1
                m += 1

        self.list_datas = ld + lm
        



#Отдельная либа сборки данных в пандас


import pandas as pd

       
class Pandaset:    
    
    
    #Боевая часть функции преобразования в Пандас    
    
    def __init__ (self, data, headers, dimensions, metrics):
        self.data = data
        self.headers = headers
        self.dimensions = dimensions
        self.metrics = metrics
        self.dataset = []
        
    def give_me_set (self):
        
        print ('')
        print ('Panda_Conventer. Последнее обновление - 17.05.2019')
        print ('Поддержка - IMVO.SITE')
        print ('')
        
        bigdatas = []

        for x in self.data:

            mess = Listdata(x, self.dimensions, self.metrics)
            mess.list_datas_maker()
            bigdatas += [mess.list_datas]    


        rows_d = bigdatas[0:]

        self.dataset = pd.DataFrame.from_records(rows_d, columns = self.headers)

