import os
from collections import namedtuple
import pandas as pd  

_PHRASES = "PickTipMultiplexValidation,Pip1,ValidateTip,resistance sensor,"
_DIRPATH = r'./_PUT_EXECUTED_LOG_FILE_TXT_HERE/'
_RESULTPATH = './_RESULT/result.csv'
_HEADER = ""

def GetLogFilesInFolder(dir_path):
  # list to store files
  res = []
  # Iterate directory
  for file in os.listdir(dir_path):
      # check only text files
      if file.endswith('.txt'):
          res.append(file)

  print("FOUND:",len(res),"FILES IN",dir_path)
  return res

def GetDataByPhrases(phrases,path,filename):
    result = []
    Data = namedtuple('Data', ['FileName', 'LineNumber', 'Text'])
    isExisting = os.path.exists(path+filename)
    if(isExisting):
      with open(path+filename) as myFile:
          try:
            for num, line in enumerate(myFile, 1):
                if phrases in line:
                    #print ('found at line:', num)
                    datain = Data(filename, num, line)
                    result.append(datain)
          except:
            print(filename,"failed to extract")
            return result
    print(filename,"found",len(result))
    return result
                
def ExtractLog():
  files = GetLogFilesInFolder(_DIRPATH)
  result = []
  for file in files:
    data = GetDataByPhrases(_PHRASES,_DIRPATH,file)
    if(len(data) != 0):
      for value in data:
        csvdata = str(value.FileName)+","+str(value.LineNumber)+","+str(value.Text)
        result.append(csvdata)
  return result

def SaveToCsv(result):
  with open(_RESULTPATH, 'w') as out:
    if(_HEADER != ""):
      out.write(_HEADER)
    for value in result:
      out.write(value)

result = ExtractLog()
SaveToCsv(result)