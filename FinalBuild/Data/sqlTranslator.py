import MySQLdb
from Data.buildDict import buildDict
class sqlTranslator:

    def insert(object,schemaType):
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
                attribute = '_'+schema[i]
                string1 = schema[i]+','
                string2 = "'"+dictionary[attribute]+"',"
                table+=string1
                values+=string2
            else:
                attribute = '_'+schema[i]
                string1 = schema[i]+')'
                string2 = "'"+dictionary[attribute]+"')"
                table +=string1
                values += string2
            i+=1
        query = beginInsert+table+midPoint+values
        sqlTranslator.execute(query)

    def execute(query):
        server = "35.224.154.47"
        userN = "basicUser"
        passw = "root"
        dbName = "synth"
        conn = MySQLdb.connect(host=server,port=3306,user=userN,passwd=passw,db=dbName)
        c = conn.cursor()
        c.execute(query)
        conn.commit()
        c.close()
        conn.close()
