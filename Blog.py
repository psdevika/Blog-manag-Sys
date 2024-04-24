import mysql.connector as msc
mydb=msc.connect(host="localhost",
                user="root",
                password="root",
                allow_local_infile=True)
crs=mydb.cursor()
qry01="CREATE DATABASE if not exists blog"
crs.execute(qry01)
qry02="USE blog "
crs.execute(qry02)
qry03="CREATE TABLE if not exists Profile (id_profile int(10),Username varchar(25),Email varchar(25),Followers int(4),Following int(4),Owned_Posts int(20),Comments int(5));"
crs.execute(qry03)
qry31="INSERT INTO Profile   VALUES(0001,'AleXa','alx21@gmail.com',10,2,5,2)"
qry32="INSERT INTO  Profile   VALUES  (0002,'Ram','ram00@gmail.com',4,2,0,5)"  
qry33="INSERT INTO Profile   VALUES (0003,'Rony','rony@gmail.com',3,3,1,4)  "
qry34="INSERT INTO Profile    VALUES   (0004,'Anna','anna@gmail.com',7,5,2,3)"  
qry35="INSERT INTO Profile  VALUES(0005,'Lovera','ralov@gmail.com',0,4,0,0)  "
qry36="INSERT INTO Profile  VALUES   (0006,'Andrea','32and@gmail.com',3,8,0,2)"  
qry37="INSERT INTO Profile    VALUES (0007,'Mark','marklop@gmail.com',5,2,3,0)"
qry38="INSERT INTO Profile    VALUES (0008,'Sandra','zandra@gmail.com',0,3,4,1)"  
qry39="INSERT INTO Profile    VALUES (0009,'Carlos','losandrew@gmail.com',1,1,2,5)"
qry40="INSERT INTO Profile    VALUES (0010,'Mike','mikelonch@gmail.com',5,4,1,0)  "
crs.execute(qry31)
crs.execute(qry32)
crs.execute(qry33)
crs.execute(qry34)
crs.execute(qry35)
crs.execute(qry36)
crs.execute(qry37)
crs.execute(qry38)
crs.execute(qry39)
crs.execute(qry40)

mydb.commit()
crs.close()
