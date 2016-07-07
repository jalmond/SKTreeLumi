import os
trigger_list = ["HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_" ,
                "HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v",
                "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v",
                "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v",
                "HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v",
                "HLT_Ele12_CaloIdL_TrackIdL_IsoVL_PFJet30_v",
                "HLT_Ele12_CaloIdL_TrackIdL_IsoVL_v",
                "HLT_Ele17_CaloIdL_TrackIdL_IsoVL_v",
                "HLT_Ele18_CaloIdL_TrackIdL_IsoVL_PFJet30_v",
                "HLT_Ele23_CaloIdL_TrackIdL_IsoVL_v",
                "HLT_Ele23_CaloIdL_TrackIdL_IsoVL_PFJet30_v",
                "HLT_Ele33_CaloIdL_TrackIdL_IsoVL_PFJet30_v",
                "HLT_Ele23_WPLoose_Gsf_v",
                "HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v",
                "HLT_Mu17_Mu8_DZ_v",
                "HLT_Mu17_Mu8_SameSign_DZ_v",
                "HLT_Mu20_Mu10_SameSign_DZ_v",
                "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v",
                "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v",
                "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v",
                "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v",
                "HLT_Mu8_v",
                "HLT_Mu17_v",
                "HLT_Mu20_v",
                "HLT_IsoMu20_v",
                "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v",
                "HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v",
                "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v",
                "HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v",
                "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v",
                "HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v",
                "HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL_v",
                "HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v",
                "HLT_TripleMu_12_10_5",
                "HLT_DiMu9_Ele9_CaloIdL_TrackIdL"]                


normtag="/afs/cern.ch/user/l/lumipro/public/normtag_file/moriond16_normtag.json"
goldenjson="/afs/cern.ch/user/j/jalmond/POSTDOC/Analysis/General/Lumi/Bril/jsonfiles/Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON_v2.txt"
silverjson="/afs/cern.ch/user/j/jalmond/POSTDOC/Analysis/General/Lumi/Bril/jsonfiles/Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON_Silver_v2.txt"

badjson="/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/BeamSpotIssue_JSON.txt"


os.system("brilcalc lumi -u /pb --normtag " + normtag + "  -i " + goldenjson + " > golden_CD.txt")              
os.system("brilcalc lumi -u /pb --normtag " + normtag + "  -i " + silverjson + " > silver_CD.txt")              
os.system("brilcalc lumi -u /pb --normtag " + normtag + "  -i " + badjson + " > badjs_CD.txt")

#period C
os.system("brilcalc lumi -u /pb --normtag " + normtag + " --end 256464  -i " + goldenjson + " > golden_C.txt")
os.system("brilcalc lumi -u /pb --normtag " + normtag + " --end 256464  -i " + silverjson + " > silver_C.txt")
os.system("brilcalc lumi -u /pb --normtag " + normtag + " --end 256464  -i " + badjson + " > badjs_C.txt")

#period D
os.system("brilcalc lumi -u /pb --normtag " + normtag + " --begin 256630  -i " + goldenjson + " > golden_D.txt")
os.system("brilcalc lumi -u /pb --normtag " + normtag + " --begin 256630  -i " + silverjson + " > silver_D.txt")    
os.system("brilcalc lumi -u /pb --normtag " + normtag + " --begin 256630  -i " + badjson + " > badjs_D.txt")    



read_json_lumi_split = open("golden_CD.txt","r")
CheckLumi=False
lumi_total=0.
for line in read_json_lumi_split:
   
    if "#Summary" in line:
        CheckLumi=True
        if CheckLumi:
            splitlumi = line.split()
        if not "nls" in line:
            if len(splitlumi) == 13:
                lumi_total+=float(splitlumi[11])


read_json_lumi2_split = open("golden_CD.txt","r")
CheckLumi2=False
for line in read_json_lumi2_split:
    
    if "run:fill" in line:
        CheckLumi2=True
    if "#Summary" in line:
        CheckLumi2=True
    if CheckLumi2:
            splitlumi = line.split()
            if not "run:fill":
                if len(splitlumi) == 13:
                    lumi_subtotal+=float(splitlumi[12])
                    print splitlumi[12]  +  " : " + str(lumi_subtotal)
                    
                    


json_CD_list = ["golden_CD.txt","silver_CD.txt"]
json_C_list = ["golden_C.txt","silver_C.txt"]
json_D_list = ["golden_D.txt","silver_D.txt"]

read_bad_C_json_trig = open("badjs_C.txt","r")
CheckC=False
badC=0.
for line in read_bad_C_json_trig:
    if "#Summary" in line:
        CheckC=True
    if CheckC:
        splitlumi = line.split()
        if not "nls" in line:
            print line
            print len(splitlumi)
            if len(splitlumi) == 13:
                badC+=float(splitlumi[11])

read_bad_D_json_trig = open("badjs_D.txt","r")
CheckD=False
badD=0.
for line in read_bad_D_json_trig:
    if "#Summary" in line:
        CheckD=True
    if CheckD:
        splitlumi = line.split()
        if not "nls" in line:
            if len(splitlumi) == 13:
                badD+=float(splitlumi[11])

read_bad_CD_json_trig = open("badjs_CD.txt","r")
CheckCD=False
badCD=0.
for line in read_bad_CD_json_trig:
    if "#Summary" in line:
        CheckCD=True
    if CheckCD:
        splitlumi = line.split()
        if not "nls" in line:
            if len(splitlumi) == 13:
                badCD+=float(splitlumi[11])


for j in json_CD_list:
    read_json_trig = open(j,"r")
    Check=False
    lumi=0. 
    for line in read_json_trig:
        if "#Summary" in line:
            Check=True
        if Check:
            splitlumi = line.split()
            if not "nls" in line:
                if len(splitlumi) == 13:
                    lumi+=float(splitlumi[11])
    print "Lumi for " + j + " = " + str(lumi) + " with bad LS removed = " + str(lumi-badCD)            





for j in json_C_list:
    read_json_trig = open(j,"r")
    Check=False
    lumi=0.
    for line in read_json_trig:
        if "#Summary" in line:
            Check=True
        if Check:
            splitlumi = line.split()
            if not "nls" in line:
                if len(splitlumi) == 13:
                    lumi+=float(splitlumi[11])
    print "Lumi for " + j + " = " + str(lumi) + " with bad LS removed = " + str(lumi-badC)


for j in json_D_list:
    read_json_trig = open(j,"r")
    Check=False
    lumi=0.
    for line in read_json_trig:
        if "#Summary" in line:
            Check=True
        if Check:
            splitlumi = line.split()
            if not "nls" in line:
                if len(splitlumi) == 13:
                    lumi+=float(splitlumi[11])
    print "Lumi for " + j + " = " + str(lumi) + " with bad LS removed = " + str(lumi-badD)


for trig in trigger_list:
    os.system("brilcalc lumi -u /pb --hltpath " + trig + "* --normtag " + normtag  + " -i  " + goldenjson + " > goldentrig.log" )
    os.system("brilcalc lumi -u /pb --hltpath " + trig + "* --normtag " + normtag  + " -i  " + badjson + " > bad_goldentrigger.log")
    
    read_golden_trig = open("goldentrig.log","r")
    read_badjson_trig = open("bad_goldentrigger.log","r")
    Check=False
    trig_lumi=0.
    badjson_trig_lumi=0.

    for line in read_golden_trig:
        if "#Summary" in line:
            Check=True
        if Check:
            if trig in line:
                splittrig = line.split()
                trig_lumi+=float(splittrig[11])
                
    Check=False            
    for line in read_badjson_trig:
        if "#Summary" in line:
            Check=True
        if Check:
            if trig in line:
                splittrig = line.split()
                badjson_trig_lumi+=float(splittrig[11])


                #print "Lumi of " + trig + " = " +str(trig_lumi) + " after removing LS with bad beam spot = " + str(trig_lumi-badjson_trig_lumi)          
                
    if "trig" == "HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v":
        print "  /// Electron triggers "
        print "  // Double Electron   "
    if "trig" == "HLT_Ele8_CaloIdM_TrackIdM_PFJet30_v":
        print " "
        print "    // Single Electon "
    if "trig" == "HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v":
        print " "
        print "   // TriLepton Electron "
        
    if "trig" == "HLT_Mu17_Mu8_DZ_v":
        print " "
        print "   /// Muon Triggers"
        print "    // Double Muon"
    if "trig" == "HLT_Mu8_v":
        print "    // single muon "
    if "trig" == "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v":
        print " "
        print "   /// multilepton"

    print 'else if(triggername.Contains("'+ trig + '")) return (('+ str(trig_lumi-badjson_trig_lumi) +')/tlumi);'
