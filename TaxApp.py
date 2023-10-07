import requests
import json
import pandas as pd
from SqlConnection.SqlConnection import SQL_Database

class TaxApi():
    def __init__(self,id):
      conn = SQL_Database().create_server_connection()
      query ="Select	BaseURL,SendURL,InquiryURL,Token From	Msg_TaxConfig"
      config = pd.read_sql(query, conn)
      query ="Select 	EconomicCode From	Z_Company "
      company = pd.read_sql(query, conn)
      query =f"Select 	JsonRequest,JsonInquiryRequest From Msg_TaxQueueHeader	Where	Id	=	{id} "
      heder = pd.read_sql(query, conn)
      
      self.BaseURL = config['BaseURL'][0]
      self.SendURL = config['SendURL'][0]
      self.InquiryURL = config['InquiryURL'][0]
      self.Token = config['Token'][0]
      self.x_orgid = company['EconomicCode'][0]
      self.JsonRequest = heder['JsonRequest'][0]
      self.JsonInquiryRequest = heder['JsonInquiryRequest'][0]
      self.conn = conn
      self.id = id


    def sendapi(self):
       url = self.BaseURL + self.SendURL
       print(url)

    def inquiryapi(self):
       url = self.BaseURL + self.InquiryURL
       headers = {"Content-Type": "application/json",
           "X-OrgID": self.x_orgid,
           'Authorization': 'Bearer ' + self.Token}
       body = json.loads(self.JsonInquiryRequest)
       try:
        post_response = requests.post(url ,headers=headers ,json=body)
        my_json_str = json.dumps(post_response.json(), indent=4)
        cursor = self.conn.cursor()
        query = f"Update	Msg_TaxQueueHeader	Set  JsonInquiryRequetResponse = '{my_json_str}' Where	id = {self.id}"
        cursor.execute(query)
        self.conn.commit()
        print(post_response.status_code)
        file2write=open("Json Responce.txt",'w')
        file2write.write(my_json_str)
        file2write.close()
        return  my_json_str
       except:
        print("Receive error!!!!!!!!!!!!!!!!!!!")


#TaxApi(id = 11).inquiryapi()
    

