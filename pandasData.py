"""

Data information

ID   PLATE NO      DEPARTEMENT



"""



from database import Bollo

import pandas as pd




df  = pd.read_excel('sample.xlsx')

#addtion=Bollo()

#for i in df['PLATE NO']:
#    plate_no=i
#    departement=df[df['PLATE NO']==i].iloc[0,2]
#    remark=''
#    result=addtion.insertIntoTableNew(plate_no,departement,remark)
#    print(result)


print(df['DEPARTEMENT'].unique())


#print(df[df['PLATE NO']=='3-86644AA'].iloc[0,2])