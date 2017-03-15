
import datetime

#Get nth key, value of MC sample
def getMCVal(dict_MC, n):
    return dict_MC[list(dict_MC)[n]]

def getMCKey(dict_MC, n):
   val = getMCVal(dict_MC, n)
   today_date = datetime.date.today()
   if val !="":
       start_name = val.split("/")[1].split("_")[0]
       key = start_name+"_ntuple_"+str(today_date)
       if start_name == "ST":
           start_name = start_name+ "_" +val.split("/")[1].split("_")[1]
           key = start_name+"_ntuple_"+str(today_date)
           return key
       else:
           return key

#Get nth key, value of DATA sample
def getDataVal(dict_Data, n):
    return dict_Data[list(dict_Data)[n]]

def getDataKey(dict_Data, n):
   val = getDataVal(dict_Data, n)
   today_date = datetime.date.today()
   if val !="":
       start_name = val.split("/")[1].split("_")[0]
       key = start_name+"_ntuple_"+str(today_date)
       return key

