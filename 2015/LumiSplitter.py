import os, sys

#### how many lumi period blocks to make
ndiv=10
#### 

#### configure
lumifile = open("lumi_catversion2016_801.txt","w")
normtag="/afs/cern.ch/user/l/lumipro/public/normtag_file/normtag_DATACERT.json"
goldenjson="/afs/cern.ch/user/j/jalmond/POSTDOC/Analysis/General/Lumi/Bril/jsonfiles/Cert_271036-277148_13TeV_PromptReco_Collisions16_JSON.txt"

lumifile.write("### Config \n")
lumifile.write("### Period B--E ")

print "brilcalc lumi -u /pb --normtag " + normtag + "  -i " + goldenjson
lumifile.write("### Period B--E ")
lumifile.write("### brilcalc lumi -u /pb --normtag " + normtag + "  -i " + goldenjson + "\n")


os.system("brilcalc lumi -u /pb --normtag " + normtag + "  -i " + goldenjson + " > golden_BE.txt")              


read_json_lumi_split = open("golden_BE.txt","r")
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
                   

print "Total_lumi = " + str(lumi_total)

read_json_lumi2_split = open("golden_BE.txt","r")
read_json_lumi2_split2 = open("golden_BE.txt","r")

CheckLumi2=False
lumi_subtotal=0.

CheckLumi2_2=False

lumi_division=lumi_total/ndiv

for line in read_json_lumi2_split:
       if "run:fill" in line:
              CheckLumi2=True
       if "#Summary" in line:
              CheckLumi2=False
       if CheckLumi2:
              splitlumi = line.split()
              if len(splitlumi) == 14:
                     run=splitlumi[1].replace(":"," ")
                     runnumber=run[:6] 
                     print "mapLumi["+str(runnumber)+"] = " + splitlumi[12]+ ";"
                     lumifile.write("run "+str(runnumber)+" " + splitlumi[12]+ "\n")   


for line in read_json_lumi2_split2:
       if "run:fill" in line:
              CheckLumi2_2=True
       if "#Summary" in line:
              CheckLumi2_2=False
       if CheckLumi2_2:
              splitlumi = line.split()
              if len(splitlumi) == 14:
                     lumi_subtotal+=float(splitlumi[12])
                     run=splitlumi[1].replace(":"," ")
                     runnumber=run[:6]
                     if lumi_subtotal > lumi_division:
                            print "mapLumiPerBlack["+ str(runnumber) + "] = " + str(lumi_subtotal) +";"
                            lumifile.write("block "+ str(runnumber) + " " + str(lumi_subtotal) +" \n")
                            lumi_subtotal=0


lumifile.write("END")
lumifile.close()
