from Driver import Driver

"""
It has 4 parameters.
1) Integer - Source file type. enter 1. DB - SQL Server \n 2. MySQL \n 3. DB - Oracle \n 4. DB - MS Access  \n 5. DB - Netezza "
               6. Others \n
2) Absolute path of source file. Enclosed with Double quotes
3) Absolute path where Data Extract to be placed. Enclosed with Double quotes 
"""

data_1 = Driver(1,"F:\xxxxx\python\\Data_2.csv","F:\xxxxx\python\\",['pk_3','pk_4','pk_5'])
data_2 = Driver(1,"F:\xxxxx\python\\Input_data_1.csv","F:\xxxxx\python\\",['pk_3','pk_4','pk_5'])
data_3 = Driver(1,"F:\xxxxx\python\\Data_2.csv","F:\xxxxx\python\\",['pk_3','pk_4','pk_5'])
data_4 = Driver(1,"F:\xxxxx\python\\Input_data_1.csv","F:\xxxxx\python\\",['pk_3','pk_4','pk_5'])
data_5 = Driver(1,"F:\xxxxx\python\\Data_2.csv","F:\xxxxx\python\\",['pk_3','pk_4','pk_5'])
data_6 = Driver(1,"F:\xxxxx\python\\Input_data_1.csv","F:\xxxxx\python\\",['pk_3','pk_4','pk_5'])
data_7 = Driver(1,"F:\xxxxx\python\\Data_2.csv","F:\xxxxx\python\\",['pk_3','pk_4','pk_5'])
data_8 = Driver(1,"F:\xxxxx\python\\Input_data_1.csv","F:\xxxxx\python\\",['pk_3','pk_4','pk_5'])