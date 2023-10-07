import  json
from  TaxApp import  TaxApi
from SqlConnection.SqlConnection import SQL_Database

class Json_Reader:
    def __init__(self,id):
        data = TaxApi(id).inquiryapi()
        self.Json = json.loads(data)
        try :
            self.status = self.Json[0]["status"]
            self.packetType = self.Json[0]["packetType"]
        except :
            self.status = "Anonymous"
            self.packetType = "Anonymous"

    def checkstatus(self):
        if self.status == "SUCCESS" or self.packetType == "SUCCESS":
            SendingStatus = 6
        elif self.status == "ERROR" or self.packetType == "ERROR":
           SendingStatus = 7
        elif self.status == "PENDING" or self.packetType == "PENDING":
           SendingStatus = 8
        else:
           SendingStatus = 10
        return  SendingStatus
    
    def errorfild(self):
        if self.status == "SUCCESS" or self.packetType == "SUCCESS":
            Error = None
        elif self.status == "ERROR" or self.packetType == "ERROR":
            Error = self.Json[0]["data"]["error"]["message"]
        elif self.status == "PENDING" or self.packetType == "PENDING":
           Error = "PENDING"
        else:
           Error = "An unexpected error has occurred"
        return  Error

class UpdateDB:
    def __init__(self,id):
        self.SendingStatus = Json_Reader(id).checkstatus()
        self.error = Json_Reader(id).errorfild()
        self.conn = SQL_Database().create_server_connection()
        self.id =  id
    def sendingstatuserror(self):
        query = f"Update	Msg_TaxQueueHeader	Set  SendingStatus = '{self.SendingStatus}' , Errors = '{self.error}' Where	id = {self.id}"
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()
        return self.error

#UpdateDB(11).sendingstatuserror()