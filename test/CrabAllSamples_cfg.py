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

#default CRAB parameters
#https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#CRAB_configuration_parameters
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.Data.inputDBS = 'global'
config.Data.unitsPerJob = 10
config.Data.splitting = 'FileBased'
config.Data.ignoreLocality = True
config.Site.storageSite = 'T2_IN_TIFR'

#https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRABClientLibraryAPI#Example_submitting_multiple_task
#users inputs ------------------
isMuons = True
isElectrons = False
isMC = True
isData = True
#range_MC = len(mcSampDict)
#range_Data = len(dataSampDict)
range_MC = 1
range_Data = 1
#-------------------------------

file_of_t2_paths = open("FileOfT2Paths_"+ str(datetime.date.today()).replace("-","") +".py", 'w')
#Muon channel
all_t2_paths = []
muons_MC_t2_paths = ["MUONS, MC: "]
muons_Data_t2_paths = ["MUONS, DATA: "]

if isMuons:
    if isMC:
        #toPrint("MUONS, MC ","")
        for m in range(range_MC):
            mu_MC = "MuMC"
            config.General.requestName = getMCKey(mcSampDict, m) +"_"+mu_MC
            config.General.workArea = 'Crab' +mu_MC
            config.JobType.psetName = 'muons_miniAOD_to_ntuple_13TeV_cfg.py'
            #specify the dataset. Comment process.source.fileNames in psetName
            config.Data.inputDataset = getMCVal(mcSampDict, m)
            config.Data.outLFNDirBase= getLFNDirBaseMC(mu_MC, mcSampDict, m)
            #config.Data.outLFNDirBase= '/store/user/rverma/test/Crab'+mu_MC+'/'+getMCKey(mcSampDict, m)+"_"+mu_MC
            multiCrabSubmit(config, config.Data.outLFNDirBase)
            muons_MC_t2_paths.append(getPathsAtT2(mu_MC, mcSampDict, m))

    from CRABAPI.RawCommand import crabCommand
    if isData:
        #toPrint("MUONS, DATA ","")
        for d in range(range_Data):
            mu_Data = "MuData"
            config.General.requestName = getDataKey(dataSampDict, d) +"_"+mu_Data
            config.General.workArea = 'Crab'+mu_Data
            config.JobType.psetName = 'muons_miniAOD_to_ntuple_13TeV_cfg.py'
            config.Data.inputDataset = getDataVal(dataSampDict, d)
            config.Data.outLFNDirBase = getLFNDirBaseData(mu_Data, dataSampDict, m)
            #config.Data.outLFNDirBase ='/store/user/rverma/test/Crab'+mu_Data+'/'+getDataKey(dataSampDict, m)+"_"+mu_Data
            multiCrabSubmit(config, config.Data.outLFNDirBase)
            muons_Data_t2_paths.append(getPathsAtT2(mu_Data, dataSampDict, d))

file_of_t2_paths.write(str(muons_MC_t2_paths)+",\n")
file_of_t2_paths.write(str(muons_Data_t2_paths)+",\n")

#Electron channel
electrons_MC_t2_paths = ["ELECTRONS, MC: "]
electrons_Data_t2_paths = ["ELECTRONS, DATA: "]
if isElectrons:
    if isMC:
        #toPrint("ELECTRONS, MC ","")
        for m in range(range_MC):
            ele_MC = "EleMC"
            config.General.requestName = getMCKey(mcSampDict, m) +"_"+ele_MC
            config.General.workArea = 'Crab' +ele_MC
            config.JobType.psetName = 'muons_miniAOD_to_ntuple_13TeV_cfg.py'
            config.Data.inputDataset = getMCVal(mcSampDict, m)
            config.Data.outLFNDirBase= getLFNDirBaseMC(ele_MC, mcSampDict, m)
            #config.Data.outLFNDirBase = '/store/user/rverma/test/Crab'+ele_MC+'/'+getMCKey(mcSampDict, m)+"_"+ele_MC
            multiCrabSubmit(config, config.Data.outLFNDirBase)
            electrons_MC_t2_paths.append(getPathsAtT2(ele_MC, mcSampDict, m))

    if isData:
        #toPrint("ELECTRONS, DATA ","")
        for d in range(range_Data):
            ele_Data = "EleData"
            config.General.requestName = getDataKey(dataSampDict, d) + "_"+ele_Data
            config.General.workArea = 'Crab' +ele_Data
            config.JobType.psetName = 'muons_miniAOD_to_ntuple_13TeV_cfg.py'
            config.Data.inputDataset = getDataVal(dataSampDict, d)
            config.Data.outLFNDirBase = getLFNDirBaseData(ele_Data, dataSampDict, m)
            #config.Data.outLFNDirBase = '/store/user/rverma/test/Crab'+ele_Data+'/'+getDataKey(dataSampDict, m)+"_"+ele_Data
            electrons_Data_t2_paths.append(getPathsAtT2(ele_Data, dataSampDict, d))
            multiCrabSubmit(config, config.Data.outLFNDirBase)

file_of_t2_paths.write(str(electrons_MC_t2_paths)+",\n")
file_of_t2_paths.write(str(electrons_Data_t2_paths))



