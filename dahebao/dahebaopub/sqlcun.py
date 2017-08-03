# -*- coding: utf-8 -*-
import pymysql
from vars import glovar as glovar
#import pandas as pd
def select_list(sqlcmd):
    result = []
    try:
        conn = pymysql.connect(
            host="127.0.0.1",
            user="root",
            passwd="fqy123456",
            db="vonhehe$default",
            charset="utf8")
        cursor = conn.cursor()
        cursor.execute(sqlcmd)
        results = cursor.fetchall()
        for i in results:
            result.append(i[0])
        return result
        
    except Exception as err:
        print("ERROR:" + err)
        
    finally:
        cursor.close()
        conn.close()
    
def get_txt(sqlcmd,filename):
    results = select_list(sqlcmd)
    with open(filename, 'w', encoding='utf-8') as f:
        for i in results:
            f.write(str(i)+'\n')
        print("数据写入txt文件结束！")
        
def main():
    fl = 'tb_'+ glovar.set_ndata().replace('-','_').replace('/','_')
    sqlcmd = "SELECT body FROM "+ fl +";"
    filename = r"./results/data.txt"
    get_txt(sqlcmd, filename)

if __name__ == '__main__':
    main()
    
    
    
    
    
    

