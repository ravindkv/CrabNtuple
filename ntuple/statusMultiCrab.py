
#///////////////////////////////////////////////////
#                                                  #
# CRAB status of multiple samples                  #
#                                                  #
#///////////////////////////////////////////////////

import FWCore.ParameterSet.Config as cms
import os
import sys
import datetime

#IMPORT MODULES FROM OTHER DIR
sys.path.insert(0, os.getcwd().replace("ntuple","module"))
from dataMiniAOD import muDataSampDict as muData
from dataMiniAOD import eleDataSampDict as eleData
from mcMiniAOD import mcSampDict as mc
from sampleKeyVal import *

#Check availability of samples on DAS
def execme(cmd):
    #toPrint("\033[01;32m"+ "Excecuting: "+ "\033[00m",  cmd)
    os.system(cmd)

#USERS INPUTS
isMu = True
isMC = True
isData = True
range_MC = len(mc)
range_muData = len(muData)
isEle = False
#range_eleData = len(eleData)
#range_MC = 1
#range_muData = 4
range_eleData = 1

def statusMuMC(mc, m):
    crab_dir = "CrabMuMC_20170717"
    crab_subdir = "crab_"+getMCKey(mc, m)+"_MuMC_"+crab_dir.split("_")[1]
    execme("echo  ")
    execme("echo +++++++++++++++++++++++++++++++++++++++++++++++")
    execme("echo NEXT SAMPLE : "+crab_subdir)
    execme("echo +++++++++++++++++++++++++++++++++++++++++++++++")
    execme("crab status --verboseErrors "+crab_dir+"/"+crab_subdir)
    #execme("crab kill -d "+crab_dir+"/"+crab_subdir)
    #execme("crab resubmit -d "+crab_dir+"/"+crab_subdir)

def statusMuData(muData, d):
    crab_dir = "CrabMuData_20170717"
    crab_subdir = "crab_"+getDataKey(muData, d)+"_MuData_"+crab_dir.split("_")[1]
    execme("echo  ")
    execme("echo +++++++++++++++++++++++++++++++++++++++++++++++")
    execme("echo NEXT SAMPLE : "+crab_subdir)
    execme("echo +++++++++++++++++++++++++++++++++++++++++++++++")
    #execme("crab kill -d "+crab_dir+"/"+crab_subdir)
    execme("crab status --verboseErrors "+crab_dir+"/"+crab_subdir)
    #execme("crab resubmit -d "+crab_dir+"/"+crab_subdir)
    #execme("crab report "+crab_dir+"/"+crab_subdir)
    #execme("brilcalc lumi -i "+crab_dir+"/"+crab_subdir+"/results/lumisToProcess.json")
    #execme("brilcalc lumi -i "+crab_dir+"/"+crab_subdir+"/results/processedLumis.json")
    #execme("brilcalc lumi -i "+crab_dir+"/"+crab_subdir+"/results/notFinishedLumis.json")

def statusEleMC(mc, m):
    crab_dir = "CrabEleMC_20170409"
    crab_subdir = "crab_"+getMCKey(mc, m)+"_EleMC_"+crab_dir.split("_")[1]
    execme("echo +++++++++++++++++++++++++++++++++++++++++++++++")
    execme("echo NEXT SAMPLE : "+crab_subdir)
    execme("echo +++++++++++++++++++++++++++++++++++++++++++++++")
    execme("crab status --verboseErrors "+crab_dir+"/"+crab_subdir)

def statusEleData(eleData, d):
    crab_dir = "CrabEleData_20170409"
    execme("echo +++++++++++++++++++++++++++++++++++++++++++++++")
    execme("echo NEXT SAMPLE : "+crab_subdir)
    execme("echo +++++++++++++++++++++++++++++++++++++++++++++++")
    crab_subdir = "crab_"+getDataKey(eleData, d)+"_EleData_"+crab_dir.split("_")[1]
    execme("crab status --verboseErrors "+crab_dir+"/"+crab_subdir)
    execme("crab report "+crab_dir+"/"+crab_subdir)
    execme("brilcalc lumi -i "+crab_dir+"/"+crab_subdir+"/results/lumisToProcess.json")
    execme("brilcalc lumi -i "+crab_dir+"/"+crab_subdir+"/results/processedLumis.json")
    #execme("brilcalc lumi -i "+crab_dir+"/"+crab_subdir+"/results/notFinishedLumis.json")

if isMu:
    if isMC:
        toPrint("Total MC samples",len(mc))
        for m in range(range_MC):
            statusMuMC(mc, m)
            #statusEleMC(mc, m)
    if isData:
        toPrint("Total muon DATA samples",len(muData))
        for d in range(range_muData):
            statusMuData(muData, d)
if isEle:
    if isMC:
        toPrint("Total MC samples",len(mc))
        for m in range(range_MC):
            statusEleMC(mc, m)
            #statusEleMC(mc, m)
    if isData:
        toPrint("Total muon DATA samples",len(eleData))
        for d in range(range_eleData):
            statusEleData(eleData, d)
