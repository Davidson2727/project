import MySQLdb
from Data.buildDict import buildDict
#Last updated: 04DEC2018
#This class translates all the data for the database.
#Contributing Authors: Jacob Butler

class sqlTranslator:

    def buildCols(cols):
        length = len(cols)
        columns = ''
        i = 0
        while i < length:
            if i != length - 1:
                columns +=cols[i] + ','
            else:
                columns += cols[i]
            i += 1
        return columns


    def buildCondsOR(cols, conds):
        length = len(conds)
        conditions = ''
        i = 0
        while i<length:
            if i != length - 1:
                conditions += cols[i] + '=' + "'" + conds[i] + "' OR "
            else:
                conditions += cols[i] + '=' + "'" + conds[i] + "'"
            i += 1
        return conditions


    def buildCondsAND(cols, conds):
        length = len(conds)
        conditions = ''
        i = 0
        while i<length:
            if i != length - 1:
                conditions += cols[i] + '=' + "'" + conds[i] + "' AND "
            else:
                conditions += cols[i] + '=' + "'" + conds[i] + "'"
            i += 1
        return conditions


    def insert(object, schemaType):
        dictionary = buildDict(object)
        schemaType += '.txt'
        schema = [line.rstrip('\n') for line in open(schemaType,'r')]
        beginInsert = "INSERT INTO " + schema[0] + '('
        table = ''
        values = ''
        midPoint = ' VALUES ('
        i = 1
        schemaLen = len(schema) - 1
        while i <= schemaLen:
            if i != schemaLen:
                attribute = '_' + schema[i]
                string1 = schema[i] + ','
                string2 = "'" + dictionary[attribute] + "',"
                table += string1
                values += string2
            else:
                attribute = '_' + schema[i]
                string1 = schema[i] + ')'
                string2 = "'" + dictionary[attribute] + "')"
                table += string1
                values += string2
            i += 1
        query = beginInsert + table + midPoint + values
        sqlTranslator.toServer(query)


    def login(self, cols, conds):
        query = 'SELECT '
        table = self.__class__.__name__
        columns = sqlTranslator.buildCols(cols)
        conditions = sqlTranslator.buildCondsAND(cols,conds)

        query = query + columns + ' FROM ' + table + ' WHERE ' + conditions
        results = sqlTranslator.toServer(query)
        return results


    def select(object, cols, conds):
        query = 'SELECT '
        columns = ''
        table = object.__class__.__name__
        conditions = ''
        length = len(cols)
        i = 0
        if length == 1:
            pass
        else:
            while i < length:
                if i != length - 1:
                    columns += cols[i]+','
                    conditions += cols[i] + '=' + "'" + conds[i] + "' OR "
                else:
                    columns += cols[i]
                    conditions += cols[i] + '=' + "'" + conds[i] + "'"
                i += 1


        query = query + columns + ' FROM ' + table + ' WHERE ' + conditions
        results = sqlTranslator.toServer(query)
        return results


    def toServer(query):
        server = "35.224.154.47"
        userN = "basicUser"
        passw = "root"
        dbName = "synth"
        conn = MySQLdb.connect(host = server,port = 3306,user = userN,passwd = passw,db = dbName)
        c = conn.cursor()
        c.execute(query)
        conn.commit()
        results = c.fetchall()
        c.close()
        conn.close()
        return results
