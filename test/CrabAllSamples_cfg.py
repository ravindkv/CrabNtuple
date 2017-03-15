import FWCore.ParameterSet.Config as cms
import os
import sys
import datetime

#IMPORT MODULES FROM OTHER DIR
sys.path.insert(0, os.getcwd().replace("test","data"))
from AllDataSamples import dataSampDict
from AllMCSamples import mcSampDict

sys.path.insert(0, os.getcwd().replace("test","python"))
from SamplesKeyValue import getMCVal, getMCKey, getDataVal, getDataKey, toPrint

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

file_of_t2_paths = open("PathsAtT2_"+str(datetime.date.today())+".py", 'w')
#Muon channel
from CRABAPI.RawCommand import crabCommand
if isMuons:
    if isMC:
        toPrint("MINIAOD TO NTUPLE OF MC, FOR MUON CHANNEL","")
        file_of_t2_paths.write("MUON_MC\n")
        for m in range(range_MC):
            mu_MC = "MuonsMC"
            local_crab_dir = 'Crab' +mu_MC
            local_crab_subdir = getMCKey(mcSampDict, m) +"_"+mu_MC

            #dirName of the output Ntuples at T2
            config.General.requestName = local_crab_subdir
            config.General.workArea = local_crab_dir
            #fileName of output Ntuples at T2 are taken form psetName, e.g process.TFileService.fileName
            config.JobType.psetName = 'muons_miniAOD_to_ntuple_13TeV_cfg.py'
            #specify the dataset. Comment process.source.fileNames in psetName
            config.Data.inputDataset = str(getMCVal(mcSampDict, m))
            #dir(/cms/store/user/rverma/) at T2

            t2_user_dir = '/store/user/rverma'
            t2_crab_dir = '/test/Crab'+mu_MC+'/'+local_crab_subdir
            t2_samp_name = "/"+getMCVal(mcSampDict, m).split("/")[1]
            t2_samp_subdir = "/crab_"+local_crab_subdir
            t2_crab_submit_time = "/"+"s"
            config.Data.outLFNDirBase = t2_user_dir+t2_crab_dir

            t2_full_path = '/cms'+ t2_user_dir+ t2_crab_dir+ t2_samp_name+ t2_samp_subdir+ t2_crab_submit_time
            toPrint("Path at T2", '/cms'+ t2_user_dir+ t2_crab_dir)
            file_of_t2_paths.write(t2_full_path+"\n")
            crabCommand('submit', config = config)

    if isData:
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

#Electron channel
if isElectrons:
    if isMC:
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

