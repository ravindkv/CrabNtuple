import FWCore.ParameterSet.Config as cms
import os
import sys
import datetime

#IMPORT MODULES FROM OTHER DIR
sys.path.insert(0, os.getcwd().replace("test","data"))
from AllDataSamples import dataSampDict
from AllMCSamples import mcSampDict

sys.path.insert(0, os.getcwd().replace("test","python"))
from SamplesKeyValue import getMCVal, getMCKey, getDataVal, getDataKey, getPathsAtT2, toPrint

#PRINT SAMPLE INFO
toPrint("Total MC samples",len(mcSampDict))
toPrint("Total DATA samples",len(dataSampDict))
'''
for n in range(len(mcSampDict)):
    #print getMCKey(mcSampDict, n)
    print getMCVal(mcSampDict, n)
for n in range(len(dataSampDict)):
    print getDataVal(dataSampDict, n)
'''

#CRAB PARAMETERS
#users inputs -------------------
isMuons = True
isElectrons = True
isMC = True
isData = True
#range_MC = len(mcSampDict)
#range_Data = len(dataSampDict)
range_MC = 2
range_Data = 2
#-------------------------------

#default CRAB parameters
#https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile#CRAB_configuration_parameters
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.Data.inputDBS = 'global'
config.Data.unitsPerJob = 1
config.Data.splitting = 'FileBased'
config.Data.ignoreLocality = True
config.Site.storageSite = 'T2_IN_TIFR'

#https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRABClientLibraryAPI#Example_submitting_multiple_task

file_of_t2_paths = open("FileOfT2Paths_"+ str(datetime.date.today()).replace("-","") +".py", 'w')
#Muon channel
all_t2_paths = []
from CRABAPI.RawCommand import crabCommand
if isMuons:
    muons_t2_paths = []
    if isMC:
        muons_MC_t2_paths = []
        toPrint("MINIAOD TO NTUPLE OF MC, FOR MUON CHANNEL","")
        file_of_t2_paths.write("MUON_MC\n")
        for m in range(range_MC):
            mu_MC = "MuonsMC"
            config.General.requestName = getMCKey(mcSampDict, m) +"_"+mu_MC
            config.General.workArea = 'Crab' +mu_MC
            config.JobType.psetName = 'muons_miniAOD_to_ntuple_13TeV_cfg.py'
            #specify the dataset. Comment process.source.fileNames in psetName
            config.Data.inputDataset = getMCVal(mcSampDict, m)
            config.Data.outLFNDirBase= '/store/user/rverma/test/Crab'+mu_MC+'/'+getMCKey(mcSampDict, m)+"_"+mu_MC

            toPrint("Path at T2", '/cms'+ str(config.Data.outLFNDirBase))
            muons_MC_t2_paths.append(getPathsAtT2(mu_MC, mcSampDict, m))
            crabCommand('submit', config = config)

    if isData:
        muons_Data_t2_paths = []
        toPrint("MINIAOD TO NTUPLE OF DATA, FOR MUON CHANNEL","")
        for d in range(range_Data):
            mu_Data = "MuonsData"
            config.General.requestName = getDataKey(dataSampDict, d) +"_"+mu_Data
            config.General.workArea = 'Crab'+mu_Data
            config.JobType.psetName = 'muons_miniAOD_to_ntuple_13TeV_cfg.py'
            config.Data.inputDataset = getDataVal(dataSampDict, d)
            path_T2 = '/store/user/rverma/test/Crab'+mu_Data+'/'+getDataKey(dataSampDict, m)+"_"+mu_Data
            config.Data.outLFNDirBase = path_T2
            toPrint("Path at T2",path_T2)
            file_path_T2.write(path_T2+getMCVal(mcSampDict, m).split("/")[1])
            #crabCommand('submit', config = config)
    muons_t2_paths.append(muons_MC_t2_paths)
    muons_t2_paths.append(muons_Data_t2_paths)

#Electron channel
if isElectrons:
    electrons_t2_paths = []
    if isMC:
        electrons_MC_t2_paths = []
        toPrint("MINIAOD TO NTUPLE OF MC, FOR ELECTRON CHANNEL","")
        for m in range(range_MC):
            ele_MC = "ElectronsMC"
            config.General.requestName = getMCKey(mcSampDict, m) +"_"+ele_MC
            config.General.workArea = 'Crab' +ele_MC
            config.JobType.psetName = 'muons_miniAOD_to_ntuple_13TeV_cfg.py'
            config.Data.inputDataset = getMCVal(mcSampDict, m)
            path_T2 = '/store/user/rverma/test/Crab'+ele_MC+'/'+getMCKey(mcSampDict, m)+"_"+ele_MC
            config.Data.outLFNDirBase = path_T2
            toPrint("Path at T2",path_T2)
            #crabCommand('submit', config = config)

    if isData:
        electrons_Data_t2_paths = []
        toPrint("MINIAOD TO NTUPLE OF DATA, FOR ELECTRON CHANNEL","")
        for d in range(range_Data):
            ele_Data = "ElectronsData"
            config.General.requestName = getDataKey(dataSampDict, d) + "_"+ele_Data
            config.General.workArea = 'Crab' +ele_Data
            config.JobType.psetName = 'muons_miniAOD_to_ntuple_13TeV_cfg.py'
            config.Data.inputDataset = getDataVal(dataSampDict, d)
            path_T2 = '/store/user/rverma/test/Crab'+ele_Data+'/'+getDataKey(dataSampDict, m)+"_"+ele_Data
            config.Data.outLFNDirBase = path_T2
            toPrint("Path at T2",path_T2)
            #crabCommand('submit', config = config)
    electrons_t2_paths.append(electrons_MC_t2_paths)
    electrons_t2_paths.append(electrons_Data_t2_paths)

all_t2_paths.append(muons_t2_paths)
all_t2_paths.append(electrons_t2_paths)
file_of_t2_paths.write(all_t2_paths)

