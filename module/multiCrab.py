
#//////////////////////////////////////////////////////
#                                                     #
# CRAB Command to submit multiple datasets in one go. #
#                                                     #
#//////////////////////////////////////////////////////

from subprocess import call, check_output
import sys, os
from CRABAPI.RawCommand import crabCommand
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException
from sampleKeyVal import toPrint

#Documentations about multicrab:
#https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRABClientLibraryAPI#Example_submitting_multiple_task
#https://lost-contact.mit.edu/afs/cern.ch/ubackup/z/zdemirag/public/forSid/crabNero_80X.py

def multiCrabSubmit(config, path_T2):
    ### for some reason only the first dataset is submitted correctly, work around
    if len(sys.argv) ==1:
        ## book the command and run python
        cmd = "python " + sys.argv[0] + " '" + config.General.requestName + "'"
        print ""
        print "calling: "+cmd
        call(cmd,shell=True)
        return
    if len(sys.argv) > 1:
        ## if it is not in the request try the next
        if sys.argv[1] !=  config.General.requestName: return
        toPrint("Submitting", "\033[01;32m" + config.Data.inputDataset.split('/')[1] + "\033[00m")
        #toPrint("outLFNDirBase at T2", "/cms"+path_T2)
        config.Data.outputDatasetTag = config.General.requestName
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)


