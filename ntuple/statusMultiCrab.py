
#///////////////////////////////////////////////////
#                                                  #
# CRAB configuration to run over Multiple samples  #
#                                                  #
#///////////////////////////////////////////////////

import FWCore.ParameterSet.Config as cms
import os
import sys
import datetime

#IMPORT MODULES FROM OTHER DIR
sys.path.insert(0, os.getcwd().replace("ntuple","module"))
from dataMiniAOD import dataSampDict as data
from mcMiniAOD import mcSampDict as mc
from sampleKeyVal import *

#Check availability of samples on DAS
def execme(cmd):
    print "\033[01;32m"+ "Excecuting: "+ "\033[00m",  cmd
    os.system(cmd)
toPrint("Total MC samples",len(mc))
for n in range(len(mc)):
    #print getMCKey(mc, n)
    print getMCVal(mc, n)
    das = "das_client.py --limit=1 --query=\"file dataset=%s\"" %getMCVal(mc, n)
    #execme(das)

toPrint("Total DATA samples",len(data))
for n in range(len(data)):
    #print getDataKey(data, n)
    print getDataVal(data, n)
    das = "das_client.py --limit=1 --query=\"file dataset=%s\"" %getDataVal(data, n)
    #execme(das)

#-------------------------------
#USERS INPUTS
isMu = True
isEle = True
isMC = True
isData = True
range_MC = len(mc)
range_Data = len(data)
#-------------------------------

if isMu:
    if isMC:
        for m in range(range_MC):
            muMC_T2Paths.append(getNtupleT2Paths(mu_MC, mc, m))

    if isData:
        for d in range(range_Data):
            muData_T2Paths.append(getNtupleT2Paths(mu_Data, data, d))

if isEle:
    if isMC:
        for m in range(range_MC):
            electrons_MC_t2_paths.append(getNtupleT2Paths(ele_MC, mc, m))

    if isData:
        for d in range(range_Data):
            multiCrabSubmit(config, config.Data.outLFNDirBase)

