import os, sys

from Setup import *

#### how many lumi period blocks to make
ndiv=10
#### 


lumifile = open(lumifilepath,"w")
lumifile.write("### Config \n")

print "brilcalc lumi -u /pb --normtag " + normtag + "  -i " + goldenjson
lumifile.write("### Period B--G")
lumifile.write("### brilcalc lumi -u /pb --normtag " + normtag + "  -i " + goldenjson + "\n")

os.system("brilcalc lumi -u /pb --normtag " + normtag + "  -i " + goldenjson + " > golden_BG.txt")              


read_json_lumi_split = open("golden_BG.txt","r")
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

read_json_lumi2_split = open("golden_BG.txt","r")
read_json_lumi2_split2 = open("golden_BG.txt","r")

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



print "brilcalc lumi -u /pb --hltpath HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v* --normtag " + normtag  + " -i  " + goldenjson 
os.system("brilcalc lumi -u /pb --hltpath HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v* --normtag " + normtag  + " -i  " + goldenjson + " > ellumi.log" )


el_read_json_lumi_split = open("ellumi.log","r")
el_CheckLumi=False
el_lumi_total=0.
for line in el_read_json_lumi_split:
       if "#Summary" in line:
           el_CheckLumi=True
       if "nrun" in line:
              continue
       if el_CheckLumi:
           splitlumi = line.split()
           if not "nls" in line:
                  if len(splitlumi) == 13:
                         el_lumi_total+=float(splitlumi[11])


print "Total_lumi (electrons) = " + str(el_lumi_total)

el_read_json_lumi2_split = open("ellumi.log","r")
el_read_json_lumi2_split2 = open("ellumi.log","r")

el_CheckLumi2=False
el_lumi_subtotal=0.

el_CheckLumi2_2=False

el_lumi_division=el_lumi_total/ndiv

for line in el_read_json_lumi2_split:
       if "run:fill" in line:
              el_CheckLumi2=True
       if "#Summary" in line:
              el_CheckLumi2=False
       if el_CheckLumi2:
              splitlumi = line.split()
              if len(splitlumi) == 14:
                     run=splitlumi[1].replace(":"," ")
                     runnumber=run[:6]
                     print "mapLumi["+str(runnumber)+"] = " + splitlumi[12]+ ";"
                     lumifile.write("run_el "+str(runnumber)+" " + splitlumi[12]+ "\n")


for line in el_read_json_lumi2_split2:
       if "run:fill" in line:
              el_CheckLumi2_2=True
       if "#Summary" in line:
              el_CheckLumi2_2=False
       if el_CheckLumi2_2:
              splitlumi = line.split()
              if len(splitlumi) == 14:
                     el_lumi_subtotal+=float(splitlumi[12])
                     run=splitlumi[1].replace(":"," ")
                     runnumber=run[:6]
                     if el_lumi_subtotal > el_lumi_division:
                            print "mapLumiPerBlack["+ str(runnumber) + "] = " + str(el_lumi_subtotal) +";"
                            lumifile.write("block_el "+ str(runnumber) + " " + str(el_lumi_subtotal) +" \n")
                            el_lumi_subtotal=0




lumifile.write("END")
lumifile.close()

os.system("rm golden_BG.txt")
os.system("rm ellumi.log")




