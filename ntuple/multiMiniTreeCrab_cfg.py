
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
from dataMiniAOD import muDataSampDict as muData
from dataMiniAOD import eleDataSampDict as eleData
from mcMiniAOD import mcSampDict as mc
from sampleKeyVal import *
from multiCrab import *

#Check availability of samples on DAS
def execme(cmd):
    print "\033[01;32m"+ "Excecuting: "+ "\033[00m",  cmd
    os.system(cmd)

toPrint("Total MC samples",len(mc))
for n in range(len(mc)):
    #print getMCKey(mc, n)
    #print getMCVal(mc, n)
    das = "das_client.py --limit=1 --query=\"file dataset=%s\"" %getMCVal(mc, n)
    #execme(das)

toPrint("Total single muon DATA samples",len(muData))
for n in range(len(muData)):
    #print getDataKey(data, n)
    #print getDataVal(muData, n)
    das = "das_client.py --limit=1 --query=\"file dataset=%s\"" %getDataVal(muData, n)
    #execme(das)

toPrint("Total single electron DATA samples",len(eleData))
for n in range(len(eleData)):
    #print getDataKey(data, n)
    #print getDataVal(eleData, n)
    das = "das_client.py --limit=1 --query=\"file dataset=%s\"" %getDataVal(eleData, n)
    #execme(das)

#-------------------------------
#USERS INPUTS
isMu = True
isEle = False
isMC = False
isMuData = True
isEleData = False
range_MC = len(mc)
#range_Data = len(data)
#range_MC = 2
range_muData = len(muData)
range_eleData = 1
#-------------------------------

#CRAB PARAMETERS
#https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#CRAB_configuration_parameters
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

#default CRAB parameters
config.General.transferOutputs = True
config.General.transferLogs = False
config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
#config.JobType.disableAutomaticOutputCollection = True
config.Data.inputDBS = 'global'
config.Data.unitsPerJob = 20
config.Data.splitting = 'FileBased'
config.JobType.maxMemoryMB = 4000
config.Data.ignoreLocality = True
config.Site.storageSite = 'T2_IN_TIFR'

#MUON CHANNEL
muMC_T2Paths = ["MUON MC:"]
muData_T2Paths = ["MUON DATA:"]
date = str(datetime.date.today()).replace("-","")
all_T2Paths = open("ntupleT2Paths_"+ date +".txt", 'w')

if isMu:
    if isMC:
        #toPrint("MUONS, MC ","")
        for m in range(range_MC):
            mu_MC = "MuMC_"+ date
            createMuMCpsetFile(mu_MC, "../../MiniTree/Selection/test/muonNtuple_cfg.py", mc, m)
            config.General.requestName = getMCKey(mc, m) +"_"+mu_MC
            config.General.workArea = 'Crab' +mu_MC
            config.JobType.psetName = 'config/'+config.General.requestName+ "_cfg.py"
            config.Data.inputDataset = getMCVal(mc, m)
            config.Data.outLFNDirBase = getLFNDirBaseMC(mu_MC, mc, m)
            #config.JobType.outputFiles = [getMCKey(mc, m)+ mu_MC+ "_Ntuple.root" ]
            #config.JobType.pyCfgParams = ["sampleCode="+getMCKey(mc, m)]
            multiCrabSubmit(config, config.Data.outLFNDirBase)
            muMC_T2Paths.append(getNtupleT2Paths(mu_MC, mc, m))

    if isMuData:
        #toPrint("MUONS, DATA ","")
        for d in range(range_muData):
            mu_Data = "MuData_"+ date
            createMuDatapsetFile(mu_Data, "../../MiniTree/Selection/test/muonNtuple_cfg.py", muData, d)
            config.General.requestName = getDataKey(muData, d) +"_"+mu_Data
            config.General.workArea = 'Crab'+mu_Data
            config.JobType.psetName = 'config/'+config.General.requestName+ "_cfg.py"
            #config.Data.lumiMask = "https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON_MuonPhys.txt"
            config.Data.lumiMask = "https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"
            config.Data.inputDataset = getDataVal(muData, d)
            config.Data.outLFNDirBase = getLFNDirBaseData(mu_Data, muData, d)
            #config.JobType.outputFiles = [getDataKey(muData, d)+ mu_Data+ "_Ntuple.root" ]
            #config.JobType.pyCfgParams = ["sampleCode="+getDataKey(muData, d)]
            multiCrabSubmit(config, config.Data.outLFNDirBase)
            muData_T2Paths.append(getNtupleT2Paths(mu_Data, muData, d))

all_T2Paths.write(str(muMC_T2Paths)+",\n\n")
all_T2Paths.write(str(muData_T2Paths)+",\n\n")

#ELECTRON CHANNEL
electrons_MC_t2_paths = ["ELECTRON MC:"]
electrons_Data_t2_paths = ["ELECTRON DATA:"]
if isEle:
    if isMC:
        #toPrint("ELECTRONS, MC ","")
        for m in range(range_MC):
            ele_MC = "EleMC_"+ date
            createEleMCpsetFile(ele_MC, "../../MiniTree/Selection/test/electronNtuple_cfg.py", mc, m)
            config.General.requestName = getMCKey(mc, m) +"_"+ele_MC
            config.General.workArea = 'Crab' +ele_MC
            config.JobType.psetName = 'config/'+config.General.requestName+ "_cfg.py"
            config.Data.inputDataset = getMCVal(mc, m)
            config.Data.outLFNDirBase= getLFNDirBaseMC(ele_MC, mc, m)
            #config.JobType.outputFiles = [getMCKey(mc, m)+ ele_MC+ "_Ntuple.root" ]
            #config.JobType.pyCfgParams = ["sampleCode="+getMCKey(mc, m)]
            multiCrabSubmit(config, config.Data.outLFNDirBase)
            electrons_MC_t2_paths.append(getNtupleT2Paths(ele_MC, mc, m))

    if isEleData:
        #toPrint("ELECTRONS, DATA ","")
        for d in range(range_eleData):
            ele_Data = "EleData_"+ date
            createEleDatapsetFile(ele_Data, "../../MiniTree/Selection/test/electronNtuple_cfg.py", eleData, d)
            config.General.requestName = getDataKey(eleData, d) + "_"+ele_Data
            config.General.workArea = 'Crab' +ele_Data
            config.JobType.psetName = 'config/'+config.General.requestName+ "_cfg.py"
            config.Data.inputDataset = getDataVal(eleData, d)
            config.Data.outLFNDirBase = getLFNDirBaseData(ele_Data, eleData, d)
            #config.JobType.outputFiles = [getDataKey(eleData, d)+ ele_Data+ "_Ntuple.root" ]
            #config.JobType.pyCfgParams = ["sampleCode="+getDataKey(eleData, d)]
            electrons_Data_t2_paths.append(getNtupleT2Paths(ele_Data, eleData, d))
            multiCrabSubmit(config, config.Data.outLFNDirBase)

#ALL T2 PATHS
all_T2Paths.write(str(electrons_MC_t2_paths)+",\n\n")
all_T2Paths.write(str(electrons_Data_t2_paths))

