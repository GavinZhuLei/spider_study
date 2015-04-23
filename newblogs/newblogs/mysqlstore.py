# -*- coding: utf-8 -*-
# __author__ = 'gavin'
import MySQLdb
import sys


def save_blog(blog):
    try:
        conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',port=3306)
        cur = conn.cursor()
        conn.select_db('newblogs')
        # cur.execute('SET NAMES \'utf8\';')
        command = 'insert into blog(id,title,url,content) value(%s,%s,%s,%s)'
        values = [long(blog['id'][0]),blog['title'][0].encode('utf-8'),blog['url'][0],blog['content'][0].encode('utf-8')]
        cur.execute(command, values)
        conn.commit()

    except MySQLdb.Error,e:
        with open('error.txt','a') as f:
            f.write(str(e.args[1])+'\n')
        print "Mysql Error %s" % (e.args[0])
    else:
        cur.close()
        conn.close()


def is_exist(id):
    try:
        conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',port=3306)
        cur = conn.cursor()
        conn.select_db('newblogs')

        command = 'select count(*) from blog where id=%s'
        values=[long(id)]
        cur.execute(command, values)
        result = cur.fetchone()
        conn.commit()
        if result[0] > 0:
            return True
        else:
            return False

    except MySQLdb.Error,e:
        with open('error.txt','a') as f:
            f.write(str(e.args[0])+'\n')
        print "Mysql Error %s" % (e.args[0])
    else:
        cur.close()
        conn.close()


def get_all():
    try:
        conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',port=3306)
        cur = conn.cursor()
        conn.select_db('newblogs')

        command = 'select title from blog'
        cur.execute(command)
        result = cur.fetchall()
        conn.commit()
        for row in result:
            # with open('test.html', 'a') as f:
            #     f.write(row[0]+'\n')
            print row[0]

    except MySQLdb.Error,e:
        with open('error.txt','a') as f:
            f.write(str(e.args[0])+'\n')
        print "Mysql Error %s" % (e.args[0])
    else:
        cur.close()
        conn.close()

if __name__ == "__main__":
    get_all()