
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
sys.path.insert(0, os.getcwd().replace("test","data"))
from AllDataSamples import dataSampDict
from AllMCSamples import mcSampDict

sys.path.insert(0, os.getcwd().replace("test","python"))
from SamplesKeyValue import *
from MultiCrab import multiCrabSubmit

#PRINT SAMPLE INFO
'''
toPrint("Total MC samples",len(mcSampDict))
toPrint("Total DATA samples",len(dataSampDict))
for n in range(len(mcSampDict)):
    #print getMCKey(mcSampDict, n)
    print getMCVal(mcSampDict, n)
for n in range(len(dataSampDict)):
    print getDataVal(dataSampDict, n)
'''

#CRAB PARAMETERS
#https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#CRAB_configuration_parameters
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

#default CRAB parameters
config.General.transferOutputs = True
config.General.transferLogs = False
config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.JobType.disableAutomaticOutputCollection = True
config.Data.inputDBS = 'global'
#number of files to be run in one go = total files/ unitsPerJob
config.Data.unitsPerJob = 50
config.Data.splitting = 'FileBased'
config.Data.ignoreLocality = True
config.Site.storageSite = 'T2_IN_TIFR'

#USERS INPUTS
#-------------------------------
isMuons = True
isElectrons = False
isMC = False
isData = True
#range_MC = len(mcSampDict)
#range_Data = len(dataSampDict)
range_MC = 1
range_Data = 1
#-------------------------------

#MUON CHANNEL
muons_MC_t2_paths = ["MUON MC:"]
muons_Data_t2_paths = ["MUON DATA:"]
all_t2_paths = []
today_date = str(datetime.date.today()).replace("-","")
file_of_t2_paths = open("NtupleT2Paths_"+ today_date +".txt", 'w')

if isMuons:
    if isMC:
        #toPrint("MUONS, MC ","")
        for m in range(range_MC):
            mu_MC = "MuMC_"+ today_date
            config.General.requestName = getMCKey(mcSampDict, m) +"_"+mu_MC
            config.General.workArea = 'Crab' +mu_MC
            config.JobType.psetName = '../../MiniTree/Selection/test/muons_miniAOD_to_ntuple_13TeV_cfg.py'
            #specify the dataset. Comment process.source.fileNames in psetName
            config.Data.inputDataset = getMCVal(mcSampDict, m)
            config.Data.outLFNDirBase = getLFNDirBaseMC(mu_MC, mcSampDict, m)
            config.JobType.outputFiles = [getMCKey(mcSampDict, m)+ "_Ntuple_"+ mu_MC+ ".root" ]
            config.JobType.pyCfgParams = ["sampleCode="+getMCKey(mcSampDict, m)]
            multiCrabSubmit(config, config.Data.outLFNDirBase)
            muons_MC_t2_paths.append(getPathsAtT2(mu_MC, mcSampDict, m))

    if isData:
        #toPrint("MUONS, DATA ","")
        for d in range(range_Data):
            mu_Data = "MuData_"+ today_date
            config.General.requestName = getDataKey(dataSampDict, d) +"_"+mu_Data
            config.General.workArea = 'Crab'+mu_Data
            config.JobType.psetName = '../../MiniTree/Selection/test/muons_miniAOD_to_ntuple_13TeV_cfg.py'
            config.Data.inputDataset = getDataVal(dataSampDict, d)
            config.Data.outLFNDirBase = getLFNDirBaseData(mu_Data, dataSampDict, d)
            config.JobType.outputFiles = [getMCKey(mcSampDict, d)+ "_Ntuple_"+ mu_Data+ ".root" ]
            config.JobType.pyCfgParams = ["sampleCode="+getMCKey(dataSampDict, d)]
            multiCrabSubmit(config, config.Data.outLFNDirBase)
            muons_Data_t2_paths.append(getPathsAtT2(mu_Data, dataSampDict, d))

file_of_t2_paths.write(str(muons_MC_t2_paths)+",\n\n")
file_of_t2_paths.write(str(muons_Data_t2_paths)+",\n\n")

#ELECTRON CHANNEL
electrons_MC_t2_paths = ["ELECTRON MC:"]
electrons_Data_t2_paths = ["ELECTRON DATA:"]
if isElectrons:
    if isMC:
        #toPrint("ELECTRONS, MC ","")
        for m in range(range_MC):
            ele_MC = "EleMC_"+ today_date
            config.General.requestName = getMCKey(mcSampDict, m) +"_"+ele_MC
            config.General.workArea = 'Crab' +ele_MC
            config.JobType.psetName = '../../MiniTree/Selection/test/electrons_miniAOD_to_ntuple_13TeV_cfg.py'
            config.Data.inputDataset = getMCVal(mcSampDict, m)
            config.Data.outLFNDirBase= getLFNDirBaseMC(ele_MC, mcSampDict, m)
            config.JobType.outputFiles = [getMCKey(mcSampDict, m)+ "_Ntuple"+ ele_MC+ ".root" ]
            config.JobType.pyCfgParams = ["sampleCode="+getMCKey(mcSampDict, m)]
            multiCrabSubmit(config, config.Data.outLFNDirBase)
            electrons_MC_t2_paths.append(getPathsAtT2(ele_MC, mcSampDict, m))

    if isData:
        #toPrint("ELECTRONS, DATA ","")
        for d in range(range_Data):
            ele_Data = "EleData_"+ today_date
            config.General.requestName = getDataKey(dataSampDict, d) + "_"+ele_Data
            config.General.workArea = 'Crab' +ele_Data
            config.JobType.psetName = '../../MiniTree/Selection/test/electrons_miniAOD_to_ntuple_13TeV_cfg.py'
            config.Data.inputDataset = getDataVal(dataSampDict, d)
            config.Data.outLFNDirBase = getLFNDirBaseData(ele_Data, dataSampDict, d)
            config.JobType.outputFiles = [getMCKey(mcSampDict, d)+ "_Ntuple_"+ ele_Data+ ".root" ]
            config.JobType.pyCfgParams = ["sampleCode="+getMCKey(dataSampDict, d)]
            electrons_Data_t2_paths.append(getPathsAtT2(ele_Data, dataSampDict, d))
            multiCrabSubmit(config, config.Data.outLFNDirBase)

#ALL T2 PATHS
file_of_t2_paths.write(str(electrons_MC_t2_paths)+",\n\n")
file_of_t2_paths.write(str(electrons_Data_t2_paths))



