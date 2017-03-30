
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
    #toPrint("\033[01;32m"+ "Excecuting: "+ "\033[00m",  cmd)
    os.system(cmd)

#USERS INPUTS
isMu = True
isEle = True
isMC = True
isData = True
range_MC = len(mc)
range_Data = len(data)
#range_MC = 1
#range_Data = 1

def statusMuMC(mc, m):
    crab_dir = "CrabMuMC_20170329"
    crab_subdir = "crab_"+getMCKey(mc, m)+"_MuMC_"+crab_dir.split("_")[1]
    execme("crab status "+crab_dir+"/"+crab_subdir)

def statusMuData(data, d):
    crab_dir = "CrabMuData_20170329"
    crab_subdir = "crab_"+getDataKey(data, d)+"_MuData_"+crab_dir.split("_")[1]
    execme("crab status "+crab_dir+"/"+crab_subdir)

def statusEleMC(mc, m):
    crab_dir = "CrabEleMC_20170329"
    crab_subdir = "crab_"+getMCKey(mc, m)+"_EleMC_"+crab_dir.split("_")[1]
    execme("crab status "+crab_dir+"/"+crab_subdir)

def statusEleData(data, d):
    crab_dir = "CrabEleData_20170329"
    crab_subdir = "crab_"+getDataKey(data, d)+"_EleData_"+crab_dir.split("_")[1]
    execme("crab status "+crab_dir+"/"+crab_subdir)

toPrint("Total MC samples",len(mc))
for m in range(range_MC):
    statusMuMC(mc, m)
    statusEleMC(mc, m)

toPrint("Total DATA samples",len(data))
for d in range(range_Data):
    statusMuData(data, d)
    statusEleData(data, d)


