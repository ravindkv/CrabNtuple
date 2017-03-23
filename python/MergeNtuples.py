
#//////////////////////////////////////////////////
#                                                 #
# Copy Ntuple root files from T2_IN_TIFR to T3.   #
# Merge them into a single root file at T3.       #
# Send the merged file back to T2_IN_TIFR.        #
# Store the full path of merged file for Analysis #
#                                                 #
#//////////////////////////////////////////////////


import FWCore.ParameterSet.Config as cms
import os
import sys
import datetime


#USERS INPUTS
#-------------------------------
isMuon = True
isElectron = True
isMC = True
isData = True
#range_muMC = len(muMC_T2Paths)
#range_muData = len(muData_T2Paths)
#range_eleMC = len(eleMC_T2Paths)
#range_eleData = len(eleData_T2Paths)
range_muMC = 1
range_muData = 1
range_eleMC = 1
range_eleData = 1
#-------------------------------


#Sample paths at T2
muMC_T2Paths = []
muData_T2Paths = []
eleMC_T2Paths = []
eleData_T2Paths = []

def getSampName(line, sampName, sampPaths):
    if line.find(sampName)!=-1:
        s1 = line.replace("]","").split(",")
        for n in range(1, len(s1)-1):
            sampPaths.append(s1[n].replace(" ",""))

for line in open("NtupleT2Paths_20170318.txt"):
    line = line.strip()
    if len(line)!=0:
        getSampName(line, "MUON MC", muMC_T2Paths)
        getSampName(line, "MUON DATA", muData_T2Paths)
        getSampName(line, "ELECTRON MC", eleMC_T2Paths)
        getSampName(line, "ELECTRON DATA", eleData_T2Paths)


def execme(command):
    print ""
    print "\033[01;32m"+ "Excecuting: "+ "\033[00m",  command
    print ""
    os.system(command)

#read T2 Paths of ntuples, merge them, send merged file back to T2
def mergeNtuples(T2Paths, range_):
    for m in range(range_):
        path_T2 = T2Paths[m].replace("'","")
        print path_T2

        #local dir at T3 for the CRAB, samples
        dir_T3 = path_T2.split("/")[-4]
        dir_samp_T3 = path_T2.split("/")[-1]

        #command to be excecuted to merge ntuples
        cmd_T3 = []
        cmd_T3.append("mkdir %s" % dir_T3)
        cmd_T3.append("cd %s" % dir_T3)
        cmd_T3.append("mkdir %s" % dir_samp_T3)
        cmd_T3.append("cd %s" % dir_samp_T3)

        #copy files from T2 to T3, get the last dir containg ntuples
        cmd_T3.append("xrdcp -r root://se01.indiacms.res.in:1094/"+path_T2+" .")
        for x in os.walk(dir_samp_T3):
            for x in os.walk(x[0]):
                pass
        print x[0]

        #total number of ntuple files
        tot_files = len([name for name in os.listdir(x[0])])
        merged_ntuple = dir_samp_T3+ "_Ntuple_Merged.root"
        cmd_T3.append("cd %s" %x[0])

        #merge all the ntuples by hadd command
        cmd_T3.append("hadd -k "+ merged_ntuple+ dir_samp_T3+"_Ntuple_{1.."+str(tot_files)+"}.root")

        #move the merged ntuple to back to T2
        cmd_T3.append("xrdcp -r "+merged_ntuple+ " root://se01.indiacms.res.in:1094/"+path_T2)
        cmd_T3.append("rm -r *")

        #execute all the commands, in one go
        cmd_T3_comb = ''
        for cmd in cmd_T3:
            if cmd!=cmd_T3[-1]:
                cmd_T3_comb += cmd +" && "
            else:
                cmd_T3_comb += cmd
        execme(cmd_T3_comb)

#muon channel
if isMuon:
    if isMC:
        mergeNtuples(muMC_T2Paths, range_muMC)
    if isData:
        mergeNtuples(muData_T2Paths, range_muData)

#electron channel
if isElectron:
    if isMC:
        mergeNtuples(eleMC_T2Paths, range_eleMC)
    if isData:
        mergeNtuples(eleData_T2Paths, range_eleData)

#store the paths of all merged files
today_date = str(datetime.date.today()).replace("-","")
file_merged_paths = open("MergedT2Paths_"+ today_date +".txt", 'w')

all_merged_paths = []
def getMergedPath(ntuple_T2Paths):
    for n in range(len(ntuple_T2Paths)):
        all_merged_paths.append(ntuple_T2Paths[n]+"_Ntuple_Merged.root")
    all_merged_paths.append("\n")

getMergedPath(muMC_T2Paths)
getMergedPath(muData_T2Paths)
getMergedPath(eleMC_T2Paths)
getMergedPath(eleData_T2Paths)
file_merged_paths.write(all_merged_paths)

