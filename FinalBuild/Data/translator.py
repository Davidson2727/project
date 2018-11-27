





####################################################################################
###__This__#########################################################################
#######__class__####################################################################
##############__is__################################################################
################__still__###########################################################
#####################__not__########################################################
########################__right__###################################################
#######_here we should just be building a dictionary_###############################
#######_Then send that dictionary to the the sql query building class_##############
####################################################################################
####################################################################################
import MySQLdb
from Data.buildDict import buildDict
class translator:

    def insert(object,schemaType):
        print(object._contents)
        dictionary = buildDict(object)
        schemaType+='.txt'
        schema = [line.rstrip('\n') for line in open(schemaType,'r')]
        beginInsert = "INSERT INTO "+schema[0]+'('
        table = ''
        values = ''
        midPoint = ' VALUES ('
        i = 1
        schemaLen = len(schema)-1
        while i <= schemaLen:

            if i != schemaLen:
                print(type(schema[i]))
                attribute = '_'+schema[i]
                string1 = schema[i]+','
                string2 = "'"+dictionary[attribute]+"',"
                table+=string1
                values+=string2
            else:
                print(type(schema[i]))
                attribute = '_'+schema[i]
                string1 = schema[i]+')'
                string2 = "'"+dictionary[attribute]+"')"
                table +=string1
                values += string2
            i+=1
        query = beginInsert+table+midPoint+values
        print(query)
        translator.execute(query)

    def execute(query):
        server = "35.224.154.47"
        userN = "basicUser"
        passw = "root"
        dbName = "synth"
        conn = MySQLdb.connect(host=server,port=3306,user=userN,passwd=passw,db=dbName)
        c = conn.cursor()
        c.execute(query)
        results = c.fetchall()
        for i in results:
            print(i)
        conn.commit()
        c.close()
        conn.close()
