import mysql.connector as msc
from prettytable import PrettyTable
mydb = msc.connect(host="localhost",user="root",password="root",allow_local_infile=True)

crs=mydb.cursor()

qry01 = "CREATE DATABASE if not exists sample"
crs.execute(qry01)
qry02 = "USE sample"
crs.execute(qry02)
qry03 =  "CREATE TABLE if not exists Profiles (id_profile INT AUTO_INCREMENT PRIMARY KEY,Username varchar(25),Email varchar(25),Followers int(4),Following int(4),Owned_Posts int(20),Comments int(5));"
crs.execute(qry03)
qry31 = "INSERT INTO Profiles(Username,Email ,Followers ,Following,Owned_Posts,Comments) VALUES('AleXa','alx21@gmail.com',10,2,5,10)"
qry32 = "INSERT INTO  Profiles(Username,Email ,Followers ,Following,Owned_Posts,Comments)   VALUES('Ram','ram00@gmail.com',4,2,1,2)"
qry33 = "INSERT INTO Profiles(Username,Email ,Followers ,Following,Owned_Posts,Comments)   VALUES ('Rony','rony@gmail.com',3,3,1,2)  "
qry34 = "INSERT INTO Profiles(Username,Email ,Followers ,Following,Owned_Posts,Comments)    VALUES ('Anna','anna@gmail.com',7,5,2,4)"
qry35 = "INSERT INTO Profiles(Username,Email ,Followers ,Following,Owned_Posts,Comments)  VALUES('Lovera','ralov@gmail.com',0,4,0,0)  "
qry36 = "INSERT INTO Profiles(Username,Email ,Followers ,Following,Owned_Posts,Comments)  VALUES ('Andrea','32and@gmail.com',3,8,1,2)"
qry37 = "INSERT INTO Profiles(Username,Email ,Followers ,Following,Owned_Posts,Comments)    VALUES('Mark','marklop@gmail.com',5,2,3,6)"
qry38 = "INSERT INTO Profiles(Username,Email ,Followers ,Following,Owned_Posts,Comments)   VALUES('Sandra','zandra@gmail.com',0,3,4,8)"
qry39 = "INSERT INTO Profiles(Username,Email ,Followers ,Following,Owned_Posts,Comments)   VALUES('Carlos','losandrew@gmail.com',1,1,2,5)"
qry40 = "INSERT INTO Profiles(Username,Email ,Followers ,Following,Owned_Posts,Comments)   VALUES('Mike','mikelonch@gmail.com',5,4,1,3)  "
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

qry07="CREATE TABLE IF NOT EXISTS  categor(cat_id INT AUTO_INCREMENT PRIMARY KEY,cat_name VARCHAR(25));"
crs.execute(qry07)
qry300="INSERT INTO categor  VALUES (1001,'MATHS')"
qry301="INSERT INTO categor  VALUES (1002,'PHYSICS')"
qry302="INSERT INTO categor  VALUES (1003,'CHEMISTRY')"
qry303="INSERT INTO categor  VALUES (1004,'COMPUTER')"
qry304="INSERT INTO categor  VALUES (1005,'HISTORY')"
crs.execute(qry300)
crs.execute(qry301)
crs.execute(qry302)
crs.execute(qry303)
crs.execute(qry304)

qry04 = """CREATE TABLE IF NOT EXISTS qns (post_id INT AUTO_INCREMENT PRIMARY KEY,id_profile INT,user_name VARCHAR(25),cat_id INT,question VARCHAR(300),FOREIGN KEY (id_profile) REFERENCES Profiles(id_profile),FOREIGN KEY (cat_id) REFERENCES categor(cat_id))"""
crs.execute(qry04)
qry51 = "INSERT INTO qns(user_name,cat_id,question) VALUES ('AleXa',1001,'FACTORS OF 196')"
qry52 = "INSERT INTO qns(user_name,cat_id,question) VALUES ('AleXa',1002,'WORKING PRINCIPLE OF A WASHING MACHINE')"
qry53 = "INSERT INTO qns(user_name,cat_id,question) VALUES ('AleXa',1004,'WHO IS THE FATHER OF COMPUTER')"
qry54 = "INSERT INTO qns(user_name,cat_id,question) VALUES ('AleXa',1003,'SOLUBILITY OF ALCOHOL IN WATER IS DUE TO')"
qry55 = "INSERT INTO qns(user_name,cat_id,question) VALUES ('AleXa',1005,'WHO WAS THE FIRST EMPEROR OF INDIA')"
qry56 = "INSERT INTO qns(user_name,cat_id,question) VALUES ('Ram',1001,'20+(90/2) IS EQUAL TO')"
qry57 = "INSERT INTO qns(user_name,cat_id,question) VALUES ('Rony',1005,'WHO IS KNOWN AS THE FATHER OF INDIA')"
qry58 = "INSERT INTO qns(user_name,cat_id,question) VALUES ('Anna',1004,'WHAT IS THE FULLFORM OF CPU')"
qry59 = "INSERT INTO qns(user_name,cat_id,question) VALUES ('Anna',1003,'AN AIR BUBBLE IN WATER WILL ACT LIKE A')"
qry60 = "INSERT INTO qns(user_name,cat_id,question) VALUES ('Andrea',1003,'WHO IS KNOWN AS FATHER OF CHEMISTRY')"
qry61 = "INSERT INTO qns(user_name,cat_id,question) VALUES ('Mark',1001,'WHAT IS THE NEXT 2 PRIME NUMBERS AFTER 5')"
qry62 = "INSERT INTO qns(user_name,cat_id,question) VALUES ('Mark',1001,'HOW MANY METERS ARE IN A KILOMETER')"
qry63 = "INSERT INTO qns(user_name,cat_id,question) VALUES ('Mark',1004,'THE ABBREVIATION BPS STANDS FOR')"
qry64 = "INSERT INTO qns(user_name,cat_id,question) VALUES ('Sandra',1002,'WHO IS THE FATHER OF PHYSICS')"
qry65 = "INSERT INTO qns(user_name,cat_id,question) VALUES ('Sandra',1005,'WHO WAS THE FIRST WOMEN PRIME MINISTER OF INDIA')"
qry66 = "INSERT INTO qns(user_name,cat_id,question) VALUES ('Sandra',1004,'SMALLEST UNIT OF DATA IN A COMPUTER')"
qry67 = "INSERT INTO qns(user_name,cat_id,question) VALUES ('Sandra',1003,'THE STRONGEST METAL ON EARTH' )"
qry68 = "INSERT INTO qns(user_name,cat_id,question) VALUES ('Carlos',1001,'HOW MANY FACES DOES A CUBE HAVE')"
qry69 = "INSERT INTO qns(user_name,cat_id,question) VALUES ('Carlos',1002,'UNIT OF POWER')"
qry70 = "INSERT INTO qns(user_name,cat_id,question) VALUES ('Mike',1005,'WHO WROTE THE INDIAN NATIONAL ANTHEM')"
crs.execute(qry51)
crs.execute(qry52)
crs.execute(qry53)
crs.execute(qry54)
crs.execute(qry55)
crs.execute(qry56)
crs.execute(qry57)
crs.execute(qry58)
crs.execute(qry59)
crs.execute(qry60)
crs.execute(qry61)
crs.execute(qry62)
crs.execute(qry63)
crs.execute(qry64)
crs.execute(qry65)
crs.execute(qry66)
crs.execute(qry67)
crs.execute(qry68)
crs.execute(qry69)
crs.execute(qry70)

qry05 = "CREATE TABLE IF NOT EXISTS qns_ans(post_id INT,cat_id INT,question varchar(300), comment varchar(20),FOREIGN KEY (post_id) REFERENCES qns(post_id),FOREIGN KEY (cat_id) REFERENCES categor(cat_id));"
crs.execute(qry05)
qry92="INSERT INTO qns_ans(question,comment) VALUES('FACTORS OF 196','1,2,4,14,98')"
qry93 ="INSERT INTO qns_ans(question,comment)  VALUES('FACTORS OF 196','1,2,4,7,14')"
qry94 ="INSERT INTO qns_ans(question,comment)  VALUES('WORKING PRINCIPLE OF A WASHING MACHINE','CENTRIFUGATION')"
qry95 ="INSERT INTO qns_ans(question,comment)  VALUES('WORKING PRINCIPLE OF A WASHING MACHINE','CENTRIFUGATION')"
qry96 ="INSERT INTO qns_ans(question,comment)  VALUES('WORKING PRINCIPLE OF A WASHING MACHINE','DIFFUSION')"
qry97 ="INSERT INTO qns_ans(question,comment)  VALUES('WHO IS THE FATHER OF COMPUTER','CHARLES')"
qry98 ="INSERT INTO qns_ans(question,comment)  VALUES('WHO IS THE FATHER OF COMPUTER','CHARLES BABBAGE')"
qry99 ="INSERT INTO qns_ans(question,comment)  VALUES('SOLUBILITY OF ALCOHOL IN WATER IS DUE TO','HYDROGEN BONDING')"
qry100 ="INSERT INTO qns_ans(question,comment)  VALUES('SOLUBILITY OF ALCOHOL IN WATER IS DUE TO','OXIDATION')"
qry101="INSERT INTO qns_ans(question,comment)  VALUES('WHO WAS THE FIRST EMPEROR OF INDIA','RAJA RAM')"
qry102="INSERT INTO qns_ans(question,comment)  VALUES('WHO WAS THE FIRST EMPEROR OF INDIA','CHANDRAGUPTHA')"
qry103 ="INSERT INTO qns_ans(question,comment)  VALUES('20+(90/2) IS EQUAL TO','65')"
qry104="INSERT INTO qns_ans(question,comment)  VALUES('20+(90/2) IS EQUAL TO','65')"
qry105="INSERT INTO qns_ans(question,comment)  VALUES('WHO IS KNOWN AS THE FATHER OF INDIA','GANDHIJI')"
qry106="INSERT INTO qns_ans(question,comment)  VALUES('WHO IS KNOWN AS THE FATHER OF INDIA','MAHATMA GANDHI')"
qry107="INSERT INTO qns_ans(question,comment)  VALUES('WHICH YEAR PYHTON DEVELOPED','1991')"
qry108="INSERT INTO qns_ans(question,comment)  VALUES('WHICH YEAR PYHTON DEVELOPED','1991')"
qry109="INSERT INTO qns_ans(question,comment)  VALUES('AN AIR BUBBLE IN WATER WILL ACT LIKE A','CONVEX LENS')"
qry110="INSERT INTO qns_ans(question,comment)  VALUES('AN AIR BUBBLE IN WATER WILL ACT LIKE A','CONCAVE LENS')"
qry111="INSERT INTO qns_ans(question,comment)  VALUES('WHO IS KNOWN AS FATHER OF CHEMISTRY','LAVOISIER')"
qry112="INSERT INTO qns_ans(question,comment)  VALUES('WHO IS KNOWN AS FATHER OF CHEMISTRY','ANTOINE LAVOISIER')"
qry113="INSERT INTO qns_ans(question,comment)  VALUES('WHAT IS THE NEXT 2 PRIME NUMBERS AFTER 5','6,7')"
qry114="INSERT INTO qns_ans(question,comment)  VALUES('WHAT IS THE NEXT 2 PRIME NUMBERS AFTER 5','7,11')"
qry115="INSERT INTO qns_ans(question,comment)  VALUES('HOW MANY METERS ARE IN A KILOMETER','1000')"
qry116="INSERT INTO qns_ans(question,comment)  VALUES('HOW MANY METERS ARE IN A KILOMETER','1029')"
qry117="INSERT INTO qns_ans(question,comment)  VALUES('THE ABBREVIATION BPS STANDS FOR','BITS PER SECOND')"
qry118="INSERT INTO qns_ans(question,comment)  VALUES('THE ABBREVIATION BPS STANDS FOR','BYTES PER SECONDS')"
qry119="INSERT INTO qns_ans(question,comment)  VALUES('WHO IS THE FATHER OF PHYSICS','ISSAC NEWTON')"
qry120="INSERT INTO qns_ans(question,comment)  VALUES('WHO IS THE FATHER OF PHYSICS','ALBERT EINSTEN')"
qry121="INSERT INTO qns_ans(question,comment)  VALUES('WHO WAS THE FIRST WOMEN PRIME MINISTER OF INDIA','INDIRA GANDHI')"
qry122="INSERT INTO qns_ans(question,comment)  VALUES('WHO WAS THE FIRST WOMEN PRIME MINISTER OF INDIA','INDIRA GANDHI')"
qry123="INSERT INTO qns_ans(question,comment)  VALUES('SMALLEST UNIT OF DATA IN A COMPUTER','BIT')"
qry124="INSERT INTO qns_ans(question,comment)  VALUES('SMALLEST UNIT OF DATA IN A COMPUTER','BYTE')"
qry125="INSERT INTO qns_ans(question,comment)  VALUES('THE STRONGEST METAL ON EARTH ','TUNGESTEN')"
qry126="INSERT INTO qns_ans(question,comment)  VALUES('THE STRONGEST METAL ON EARTH','IRON')"
qry127="INSERT INTO qns_ans(question,comment)  VALUES('HOW MANY FACES DOES A CUBE HAVE','6')"
qry128="INSERT INTO qns_ans(question,comment)  VALUES('HOW MANY FACES DOES A CUBE HAVE','3')"
qry129="INSERT INTO qns_ans(question,comment)  VALUES('HOW MANY FACES DOES A CUBE HAVE','6')"
qry130="INSERT INTO qns_ans(question,comment)  VALUES('UNIT OF POWER','WATT(W)')"
qry131="INSERT INTO qns_ans(question,comment)  VALUES('UNIT OF POWER','WATT(W)')"
qry132="INSERT INTO qns_ans(question,comment)  VALUES('WHO WROTE THE INDIAN NATIONAL ANTHEM','TAGORE')"
qry133="INSERT INTO qns_ans(question,comment)  VALUES('WHO WROTE THE INDIAN NATIONAL ANTHEM','RABINDRA NADH')"
qry134="INSERT INTO qns_ans(question,comment)  VALUES('WHO WROTE THE INDIAN NATIONAL ANTHEM','RABINDRA')"
crs.execute(qry92)
crs.execute(qry93)
crs.execute(qry94)
crs.execute(qry95)
crs.execute(qry96)
crs.execute(qry97)
crs.execute(qry98)
crs.execute(qry99)
crs.execute(qry100)
crs.execute(qry101)
crs.execute(qry102)
crs.execute(qry103)
crs.execute(qry104)
crs.execute(qry105)
crs.execute(qry106)
crs.execute(qry107)
crs.execute(qry108)
crs.execute(qry109)
crs.execute(qry110)
crs.execute(qry111)
crs.execute(qry112)
crs.execute(qry113)
crs.execute(qry114)
crs.execute(qry115)
crs.execute(qry116)
crs.execute(qry117)
crs.execute(qry118)
crs.execute(qry119)
crs.execute(qry120)
crs.execute(qry121)
crs.execute(qry122)
crs.execute(qry123)
crs.execute(qry124)
crs.execute(qry125)
crs.execute(qry126)
crs.execute(qry127)
crs.execute(qry128)
crs.execute(qry129)
crs.execute(qry130)
crs.execute(qry131)
crs.execute(qry132)
crs.execute(qry133)
crs.execute(qry134)

qry200= "CREATE TABLE comments (post_id INT,id_profile INT,cat_id INT ,user_name varchar(25),cmt varchar(50),FOREIGN KEY (post_id) REFERENCES qns(post_id),FOREIGN KEY (id_profile) REFERENCES Profiles(id_profile),FOREIGN KEY (cat_id) REFERENCES categor(cat_id));"
crs.execute(qry200)
qry201="INSERT INTO qns_ans(question,comment)  VALUES('FACTORS OF 196','1,2,4,14,98')"
qry202 ="INSERT INTO qns_ans(question,comment)  VALUES('FACTORS OF 196','1,2,4,7,14')"
qry203 ="INSERT INTO qns_ans(question,comment)  VALUES('WORKING PRINCIPLE OF A WASHING MACHINE','CENTRIFUGATION')"
qry204="INSERT INTO qns_ans(question,comment)  VALUES('WORKING PRINCIPLE OF A WASHING MACHINE','CENTRIFUGATION')"
qry205="INSERT INTO qns_ans(question,comment)  VALUES('WORKING PRINCIPLE OF A WASHING MACHINE','DIFFUSION')"
qry206="INSERT INTO qns_ans(question,comment)  VALUES('WHO IS THE FATHER OF COMPUTER','CHARLES')"
qry207="INSERT INTO qns_ans(question,comment)  VALUES('WHO IS THE FATHER OF COMPUTER','CHARLES BABBAGE')"
qry208="INSERT INTO qns_ans(question,comment)  VALUES('SOLUBILITY OF ALCOHOL IN WATER IS DUE TO','HYDROGEN BONDING')"
qry209 ="INSERT INTO qns_ans(question,comment)  VALUES('SOLUBILITY OF ALCOHOL IN WATER IS DUE TO','OXIDATION')"
qry210="INSERT INTO qns_ans(question,comment)  VALUES('WHO WAS THE FIRST EMPEROR OF INDIA','RAJA RAM')"
qry211="INSERT INTO qns_ans(question,comment)  VALUES('WHO WAS THE FIRST EMPEROR OF INDIA','CHANDRAGUPTHA')"
qry212 ="INSERT INTO qns_ans(question,comment)  VALUES('20+(90/2) IS EQUAL TO','65')"
qry213="INSERT INTO qns_ans(question,comment)  VALUES('20+(90/2) IS EQUAL TO','65')"
qry214="INSERT INTO qns_ans(question,comment)  VALUES('WHO IS KNOWN AS THE FATHER OF INDIA','GANDHIJI')"
qry215="INSERT INTO qns_ans(question,comment)  VALUES('WHO IS KNOWN AS THE FATHER OF INDIA','MAHATMA GANDHI')"
qry216="INSERT INTO qns_ans(question,comment)  VALUES('WHICH YEAR PYHTON DEVELOPED','1991')"
qry217="INSERT INTO qns_ans(question,comment)  VALUES('WHICH YEAR PYHTON DEVELOPED','1991')"
qry218="INSERT INTO qns_ans(question,comment)  VALUES('AN AIR BUBBLE IN WATER WILL ACT LIKE A','CONVEX LENS')"
qry219="INSERT INTO qns_ans(question,comment)  VALUES('AN AIR BUBBLE IN WATER WILL ACT LIKE A','CONCAVE LENS')"
qry220="INSERT INTO qns_ans(question,comment)  VALUES('WHO IS KNOWN AS FATHER OF CHEMISTRY','LAVOISIER')"
qry221="INSERT INTO qns_ans(question,comment)  VALUES('WHO IS KNOWN AS FATHER OF CHEMISTRY','ANTOINE LAVOISIER')"
qry222="INSERT INTO qns_ans(question,comment)  VALUES('WHAT IS THE NEXT 2 PRIME NUMBERS AFTER 5','6,7')"
qry223="INSERT INTO qns_ans(question,comment)  VALUES('WHAT IS THE NEXT 2 PRIME NUMBERS AFTER 5','7,11')"
qry224="INSERT INTO qns_ans(question,comment)  VALUES('HOW MANY METERS ARE IN A KILOMETER','1000')"
qry225="INSERT INTO qns_ans(question,comment)  VALUES('HOW MANY METERS ARE IN A KILOMETER','1029')"
qry226="INSERT INTO qns_ans(question,comment)  VALUES('THE ABBREVIATION BPS STANDS FOR','BITS PER SECOND')"
qry227="INSERT INTO qns_ans(question,comment) VALUES('THE ABBREVIATION BPS STANDS FOR','BYTES PER SECONDS')"
qry228="INSERT INTO qns_ans(question,comment) VALUES('WHO IS THE FATHER OF PHYSICS','ISSAC NEWTON')"
qry229="INSERT INTO qns_ans(question,comment) VALUES('WHO IS THE FATHER OF PHYSICS','ALBERT EINSTEN')"
qry230="INSERT INTO qns_ans(question,comment) VALUES('WHO WAS THE FIRST WOMEN PRIME MINISTER OF INDIA','INDIRA GANDHI')"
qry231="INSERT INTO qns_ans(question,comment) VALUES('WHO WAS THE FIRST WOMEN PRIME MINISTER OF INDIA','INDIRA GANDHI')"
qry232="INSERT INTO qns_ans(question,comment) VALUES('SMALLEST UNIT OF DATA IN A COMPUTER','BIT')"
qry233="INSERT INTO qns_ans(question,comment) VALUES('SMALLEST UNIT OF DATA IN A COMPUTER','BYTE')"
qry234="INSERT INTO qns_ans(question,comment) VALUES('THE STRONGEST METAL ON EARTH ','TUNGESTEN')"
qry235="INSERT INTO qns_ans(question,comment) VALUES('THE STRONGEST METAL ON EARTH','IRON')"
qry236="INSERT INTO qns_ans(question,comment) VALUES('HOW MANY FACES DOES A CUBE HAVE','6')"
qry237="INSERT INTO qns_ans(question,comment) VALUES('HOW MANY FACES DOES A CUBE HAVE','3')"
qry238="INSERT INTO qns_ans(question,comment) VALUES('HOW MANY FACES DOES A CUBE HAVE','6')"
qry239="INSERT INTO qns_ans(question,comment) VALUES('UNIT OF POWER','WATT(W)')"
qry240="INSERT INTO qns_ans(question,comment) VALUES('UNIT OF POWER','WATT(W)')"
qry241="INSERT INTO qns_ans(question,comment) VALUES('WHO WROTE THE INDIAN NATIONAL ANTHEM','TAGORE')"
qry242="INSERT INTO qns_ans(question,comment) VALUES('WHO WROTE THE INDIAN NATIONAL ANTHEM','RABINDRA NADH')"
qry243="INSERT INTO qns_ans(question,comment) VALUES('WHO WROTE THE INDIAN NATIONAL ANTHEM','RABINDRA')"
crs.execute(qry201)
crs.execute(qry202)
crs.execute(qry203)
crs.execute(qry204)
crs.execute(qry205)
crs.execute(qry206)
crs.execute(qry207)
crs.execute(qry208)
crs.execute(qry209)
crs.execute(qry210)
crs.execute(qry211)
crs.execute(qry212)
crs.execute(qry213)
crs.execute(qry214)
crs.execute(qry215)
crs.execute(qry216)
crs.execute(qry217)
crs.execute(qry218)
crs.execute(qry219)
crs.execute(qry220)
crs.execute(qry221)
crs.execute(qry222)
crs.execute(qry223)
crs.execute(qry224)
crs.execute(qry225)
crs.execute(qry226)
crs.execute(qry227)
crs.execute(qry228)
crs.execute(qry229)
crs.execute(qry230)
crs.execute(qry231)
crs.execute(qry232)
crs.execute(qry233)
crs.execute(qry234)
crs.execute(qry235)
crs.execute(qry236)
crs.execute(qry237)
crs.execute(qry238)
crs.execute(qry239)
crs.execute(qry240)
crs.execute(qry242)
crs.execute(qry242)
crs.execute(qry243)




mydb.commit()
crs.close()


def create():
    import mysql.connector as msc
    from prettytable import PrettyTable
    mydb = msc.connect(host="localhost",user="root",password="root",allow_local_infile=True)
    crs=mydb.cursor()
    qry02 = "USE sample"
    crs.execute(qry02)
    print("TO CREATE BLOGS")
    username = input("Enter your username here: ")
    categor = input("Enter the category (MATHS, PHYSICS, CHEMISTRY, HISTORY, COMPUTER): ")
    quest = input("Enter your text here: ")

    # Map category to cat_id
    categories = {
        "MATHS": 1001,
        "PHYSICS": 1002,
        "CHEMISTRY": 1003,
        "HISTORY": 1004,
        "COMPUTER": 1005
    }
    cat_id = categories.get(categor.upper())
    if cat_id is None:
        print("Invalid category")
        return

    # Insert data using parameterized query
    crs.execute("INSERT INTO qns (user_name, cat_id, question) VALUES (%s, %s, %s)", (username, cat_id, quest))

    # Fetch and display data
    crs.execute("SELECT user_name, question FROM qns WHERE user_name = %s", (username,))
    data7 = crs.fetchall()
    table = PrettyTable()
    table.field_names = ["user_name", "question"]
    for ab in data7:
        table.add_row(ab)
    print(table)
    print("Blog created successfully!!!\n")
    menu()

# Call the create function
create()

mydb.commit()
crs.close
 
# def create():
#     import mysql.connector as msc
#     from prettytable import PrettyTable
#     mydb = msc.connect(host="localhost",user="root",password="root",allow_local_infile=True)
#     crs=mydb.cursor()
#     qry02 = "USE sample"
#     crs.execute(qry02)
#     print("TO CREATE BLOGS")
    
#     # Username1 = input("Enter your username here: ")
#     # categor = input("Enter the category (MATHS, PHYSICS, CHEMISTRY, HISTORY, COMPUTER): ")
#     # quest = input("Enter your text here: ")
    
#     # crs.execute('INSERT INTO qns(user_name, cat_id, question) VALUES (%s, %d, %s)', (Username1, categor, quest))
#     Username1 = input("Enter your username here: ")
#     categor = input("Enter the category (MATHS, PHYSICS, CHEMISTRY, HISTORY, COMPUTER): ")
#     quest = input("Enter your text here: ")

# # Using %s for all placeholder values-------
#     crs.execute('INSERT INTO qns(user_name, cat_id, question) VALUES (%s, %d, %s)', (Username1, categor, quest))

#     crs.execute('SELECT user_name, question FROM qns WHERE user_name = (%s)', (Username1,))
#     data7 = crs.fetchall()
    
#     table = PrettyTable()
#     table.field_names = ["user_name", "question"]
    
#     for ab in data7:
#         table.add_row(ab)
    
#     print(table)
#     print("Blog created successfully!!!\n")
#     menu()

    
# mydb.commit()
# crs.close
    
def read():
    import mysql.connector as msc
    from prettytable import PrettyTable
    mydb = msc.connect(host="localhost", user="root", password="root", allow_local_infile=True)
    crs = mydb.cursor()
    qry02 = "USE sample"
    crs.execute(qry02)
    global Username
    print("To read blogs")
    category = input("Select the category (MATHS, PHYSICS, CHEMISTRY, HISTORY, COMPUTER): ")
    if category == 'MATHS':
        crs.execute("SELECT post_id, user_name, question FROM qns WHERE Categories='MATHS'")
        data12 = crs.fetchall()
        table = PrettyTable()
        table.field_names = ["post_id", "user_name", "question"]
        for ab1 in data12:
            table.add_row(ab1)
        print(table)
        menu()

    elif category == 'PHYSICS':
        crs.execute("SELECT post_id, user_name, question FROM qns WHERE Categories='PHYSICS'")
        data13 = crs.fetchall()
        table = PrettyTable()
        table.field_names = ["post_id", "user_name", "question"]
        for ab2 in data13:
            table.add_row(ab2)
        print(table)
        menu()

    elif category == 'CHEMISTRY':
        crs.execute("SELECT post_id, user_name, question FROM qns WHERE Categories='CHEMISTRY'")
        data14 = crs.fetchall()
        table = PrettyTable()
        table.field_names = ["post_id", "user_name", "question"]
        for ab3 in data14:
            table.add_row(ab3)
        print(table)
        menu()

    elif category == 'HISTORY':
        crs.execute("SELECT post_id, user_name, question FROM qns WHERE Categories='HISTORY'")
        data15 = crs.fetchall()
        table = PrettyTable()
        table.field_names = ["post_id", "user_name", "question"]
        for ab4 in data15:
            table.add_row(ab4)
        print(table)
        menu()

    elif category == 'COMPUTER':
        crs.execute("SELECT post_id, user_name, question FROM qns WHERE Categories='COMPUTER'")
        data16 = crs.fetchall()
        table = PrettyTable()
        table.field_names = ["post_id", "user_name", "question"]
        for ab5 in data16:
            table.add_row(ab5)
        print(table)
        menu()

    else:
        print("     XX INVALID CHOICE XX")
        menu()


    qry_comments = "SELECT question, comment FROM qns_ans"
    crs.execute(qry_comments)
    comments = crs.fetchall()
    table_comments = PrettyTable()
    table_comments.field_names = ["question", "comment"]
    for comment in comments:
        table_comments.add_row(comment)
    print(table_comments)

    choice2 = input("DO YOU WANT TO COMMENT THE POST(y/n) : ")
    if choice2 == 'y':
        post_id1 = int(input("ENTER the post id :"))
        name=input("Enter your Username: ")
        crs.execute('SELECT post_id, question FROM qns WHERE post_id=(%s)', (post_id1,))
        question_data = crs.fetchall()
        table_question = PrettyTable()
        table_question.field_names = ["post_id", "question"]
        for q_row in question_data:
            table_question.add_row(q_row)
        print(table_question)
    
    # Get user comment
        cmt1 = input("Enter your comment here : ")
    
    # Insert user comment into comments table
        crs.execute("INSERT INTO comments (post_id,user_name, cmt) VALUES (%s, %s, %s, %s)", (post_id1,name, cmt1))
    
    # Increment the number of comments in Profiles table
        crs.execute('UPDATE Profiles SET num_comments=num_comments+1 WHERE user_name=(%s)', (name,))
    crs.close()
    mydb.commit()


def profile():
    import mysql.connector as msc
    from prettytable import PrettyTable
    mydb = msc.connect(host="localhost",user="root",password="root",allow_local_infile=True)
    crs=mydb.cursor()
    qry02 = "USE sample"
    crs.execute(qry02)
    print("profile")
    a1=input("Enter your Username: ")
    crs.execute('select id_profile,Username,Followers,Following,Owned_Posts from Profiles where Username=(%s) ',(a1, ))
    data=crs.fetchall()
    table=PrettyTable()
    table.field_names=["id_profile","Username","Followers","Following","Owned_Posts"]
    for ab in data :
        table.add_row(ab)
        print(table)
        homepage()
    print("YOU CAN REMOVE YOUR ACCOUNT OR POSTS HERE")
    del_pfl=input("TO REMOVE ACCOUNT ENTER (a) \n TO REMOVE POST ENTER (p) : ")
    if del_pfl== 'a':
        username=input("Enter your user name")
        crs.execute('DELETE FROM Profiles WHERE Username=(%s)',(username))
        print("ACCOUNT DELETED SUCCESSFULLY")
    elif del_pfl== 'p':
        username1=input("Enter your user name") 
        crs.execute('select post_id,question from qns where user_name=(%s)',(username1, ))
        data18=crs.fetchall()
        table=PrettyTable()
        table.field_names=["post_id","question"]
        for ab7 in data18 :
            table.add_row(ab7)
        print(table)
            
        post_id=input("enter the post_id you want to delete from the above table:")
        crs.execute('UPDATE Profiles SET Owned_Posts=Owned_Posts-1 where post_id=(%s)',(post_id, ))
        print("POST DELETED SUCCESSFULLY")
    else :
        print("in")
        homepage()

    mydb.commit()
    crs.close()

def menu():
         print(                          """            ===============  MAIN MENU  ===============
                                                             +--------------------------------+
                                                             |           a.Create a post      |
                                                             +--------------------------------+         
                                                             +--------------------------------+
                                                             |           b.Read               |
                                                             +--------------------------------+                                         
                                                             +--------------------------------+
                                                             |           c.Profile            |
                                                             +--------------------------------+  
                                                             +--------------------------------+
                                                             |           d.Exit               |
                                                             +--------------------------------+ 
                                                                                                              """)
         a5=input("Enter your choice : ")
         if a5 == 'a':
             create()
         elif a5 == 'b':
             read()
         elif a5 == 'c' :
             profile()
         elif a5 == 'd' :
             exit()
         else:
             print("     XX INVALID CHOICE XX")




def user():
    from prettytable import PrettyTable
    mydb = msc.connect(host="localhost",user="root",password="root",allow_local_infile=True)
    crs=mydb.cursor()
    qry02 = "USE sample"
    crs.execute(qry02)
    print("USER PANEL")
    u1=int(input("select (1) If You  do not have an account here\n select (2) If you have an account to continue"))
    if u1== 1 :
        print("Create account")
        Username4=input("Enter your new username: ")
        email=input("enter your email: ")
        Followers=0
        Following=0
        Owned_Posts=0
        crs.execute('insert into qns(user_name) values(%s) ',(Username4, ))
        crs.execute('insert into Profiles(Username,Email,Followers,Following,Owned_Posts) values(%s,%s,%s,%s,%s)',(Username4,email, Followers, Following,Owned_Posts))
        crs.execute('select id_profile,Username,Followers,Following,Owned_Posts from Profiles where Username=(%s) ',( Username4, ))
        data3=crs.fetchall()
        table=PrettyTable()
        table.field_names=["id_profile","Username","Followers","Following","Owned_Posts"]
        for ab in data3 :
            table.add_row(ab)
        print(table)
        
        mydb.commit()
        crs.close()
        print("CREATED ACCOUNT SUCCESSFULLY")
        print()
        menu()
        print()
    elif u1 == 2 :
        menu()
    else:
         print("     XX  INVALID CHOICE  XX")




def profilemng():
    import mysql.connector as msc
    from prettytable import PrettyTable
    mydb = msc.connect(host="localhost",user="root",password="root",allow_local_infile=True)
    crs=mydb.cursor()
    qry02 = "USE sample"
    crs.execute(qry02)
    print(" To manage profile")
    print("___________________")
    qry06 = "SELECT * FROM Profiles"
    crs.execute(qry06)
    rows = crs.fetchall()
    table = PrettyTable()
    table.field_names = ["id_profile", "Username", "Email", "Followers", "Following", "Owned_Posts", "Comments"]
    for rows in rows:
        table.add_row(rows)
    print(table)
    username2=input("enter username")
    crs.execute('select question from qns where user_name=(%s)', (username2, ))
    data7=crs.fetchall()
    table=PrettyTable()
    #table.field_names=["question"]
    for ab in data7 :
        table.add_row(ab)
    print(table)
    cd=input("wanna delete profile(y) or go to dashboard (n) :")
    if cd== 'y' :
        username3=input("Enter your user name")
        crs.execute('DELETE FROM Profiles WHERE Username=(%s)',(username3))
        print("ACCOUNT DELETED SUCCESSFULLY")
    elif cd== 'n':
        dashboard()
    else :
        print("     XX  INVALID CHOICE  XX")
    crs.close()
    mydb.commit()
    


def categorymng():
    import mysql.connector as msc
    from prettytable import PrettyTable
    mydb = msc.connect(host="localhost",user="root",password="root",allow_local_infile=True)
    crs=mydb.cursor()
    qry02 = "USE sample"
    crs.execute(qry02)
    category=input("Select the category(MATHS,PHYSICS,CHEMISTRY,HISTORY,COMPUTER)....:")
    if category=='MATHS' :
        crs.execute("SELECT post_id,user_name,question FROM qns WHERE cat_id=1001")
        data12=crs.fetchall()
        table=PrettyTable()
        table.field_names=["post_id","user_name","question"]
        for ab1 in data12 :
            table.add_row(ab1)
        print(table)
        dashboard()
            
    elif category=='PHYSICS' :
        crs.execute("SELECT post_id,user_name,question FROM qns WHERE cat_id=1002")
        data13=crs.fetchall()
        table=PrettyTable()
        table.field_names=["post_id","user_name","question"]
        for ab2 in data13 :
            table.add_row(ab2)
        print(table)
        dashboard()
            
    elif category=='CHEMISTRY' :
        crs.execute("SELECT post_id,user_name,question FROM qns WHERE cat_id=1003")
        data14=crs.fetchall()
        table=PrettyTable()
        table.field_names=["post_id","user_name","question"]
        for ab3 in data14 :
            table.add_row(ab3)
        print(table)
        dashboard()
            
    elif category=='HISTORY' :
        crs.execute("SELECT post_id,user_name,question FROM qns WHERE cat_id=1005")
        data15=crs.fetchall()
        table=PrettyTable()
        table.field_names=["post_id","user_name","question"]
        for ab4 in data15 :
            table.add_row(ab4)
        print(table)
        dashboard()
        
    elif category=='COMPUTER' :
        crs.execute("SELECT post_id,user_name,question FROM qns WHERE cat_id=1004")
        data16=crs.fetchall()
        table=PrettyTable()
        table.field_names=["post_id","user_name","question"]
        for ab5 in data16 :
            table.add_row(ab5)
        print(table)
        dashboard()
            
    else :
        print("     XX INVALID CHOICE XX")
        dashboard()
    crs.close()
    mydb.commit()

    
def exit():
    print("                                                            THANK YOU FOR VISITING")
    print("                                                                    ƪ(˘⌣˘)ʃ   ")
    print()
    print("                                                           ***BLOG MANAGEMENT SYSTEM***")
    print("                                                             BY")
    print("                                                             DEVIKS PS")
    print("                                                             DRISYA C C")
    print("                                                             RINIT ROLLY")
    print("                                                             CHRISTEENA FRANCIS\n ")
    e1=input("DO YOU WANT TO GO TO HOMEPAGE? (y/n):  ")
    if e1=='y':
        homepage()
    elif e1=='n':
        exit()
    else:
        print("     XX INVALID CHOICE XX")
    


def dashboard(): 
    print("                                                                 WELCOME TO ADMIN PANEL")
    print()
    print("                                                                        DASHBOARD")
    print(      "                                                       =========================================")
    print("\n")
    print("                                                                 WHAT YOU WANTED TO MANAGE ? ")
    print(""" 
                                                            +--------------------------------+
                                                            |          1.Profile manage      |
                                                            +--------------------------------+         
                                                            +--------------------------------+
                                                            |          2.Category manage     |
                                                            +--------------------------------+
                                                            +--------------------------------+
                                                            |          3.Exit                |
                                                            +--------------------------------+  
                                                                                                              """)

    a4 = int(input("Enter your choice :"))
    if a4 == 1:
        profilemng()
    elif a4 == 2:
        categorymng()
    elif a4 == 3:
        print("EXIT")
        exit()
    else:
       print("     XX   INVALID CHOICE   XX")


def admin():
    print("Enter the password to log in to the ADMIN PANEL \n (Remember you have only 3 chances to login ) ")
    num=1
    while num <= 3:
        a2 = int(input("Enter the password here :"))
        if a2 == 1234:
            dashboard()
        else :
            print("password is incorrect!!")
        num = num + 1
        print(" !!!you have no more chances!!!")

def admin():
    print("Enter the password to log in to the ADMIN PANEL \n (Remember you have only 3 chances to login ) ")
    num = 1
    while num <= 3:
        a2 = int(input("Enter the password here: "))
        if a2 == 1234:
            dashboard()
            return  # Exit the function if the password is correct
        else:
            print("Password is incorrect!!")
            if num == 3:  # Check if it's the last attempt
                print("!!! You have no more chances !!!")
        num = num + 1


def homepage():

    print()
    print("                                         Enter 1 for logging into Admin panel  ||   Enter 2 for log in as a user")
    print()
    print(""" 
                                                     ===============  HOMEPAGE  ===============
                                                         +--------------------------------+
                                                         |           1.Admin Panel        |
                                                         +--------------------------------+         
                                                         +--------------------------------+
                                                         |           2.User               |
                                                         +--------------------------------+                                           """)

    a1 = int(input("Enter your choice :"))
    if a1 == 1:
        print("Admin panel")
        admin()
    elif a1 == 2:
        print("User")
        user()
    else:
        print("please enter valid choice")

while True:
   
   print("____________________________________________________________________________________________________________________________________________________________")
   print()
   print("                                                                 BLOG MANAGEMENT SYSTEM")
   print("                                                  ____________________________________________________")
   homepage()
   break




    
        # print()
        # print("""                                                       MAIN MENU          
        #                                                      +--------------------------------+
        #                                                      |           a.Create a post      |
        #                                                      +--------------------------------+         
        #                                                      +--------------------------------+
        #                                                      |           b.Read               |
        #                                                      +--------------------------------+                                         
        #                                                      +--------------------------------+
        #                                                      |           c.Profile            |
        #                                                      +--------------------------------+ 
        #                                                                                         """)
                                                                    
        # a6=input("Enter your choice : ")       
        # if a6 == 'a':
        #     create()
        # elif a6 == 'b':
        #     read()
        # elif a6 == 'c' :
        #     profile()
        # else:
        #     print(" Enter valid choice ")
    
    # elif u1== 2 :
    #      print(                          """                           c MAIN MENU
    #                                                          +--------------------------------+
    #                                                          |           a.Create a post      |
    #                                                          +--------------------------------+         
    #                                                          +--------------------------------+
    #                                                          |           b.Read               |
    #                                                          +--------------------------------+                                         
    #                                                          +--------------------------------+
    #                                                          |           c.Profile            |
    #                                                          +--------------------------------+  
    #                                                                                                           """)
    #      a5=input("Enter your choice : ")
    #      if a5 == 'a':
    #          create()
    #      elif a5 == 'b':
    #          read()
    #      elif a5 == 'c' :
    #          profile()
    #      else:
    #          print(" Enter valid choice ")
