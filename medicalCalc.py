
from tkinter import *

def addLabel(columnIndex, rowIndex, initText):
	Label(root, text=initText).grid(row=rowIndex, column=columnIndex)

def addButton(columnIndex, initText, func):
	Button(root, text=initText, command=func).grid(row=1, column=columnIndex)

def setupLabel(initVal, rowIndex):
	points = StringVar()
	resultEntry = Entry(root, textvariable=points)
	resultEntry.grid(row=rowIndex, column=0)
	points.set(initVal)
	return resultEntry, points

allLabels = []

def doSomeCalculation(weightA, weightB):
	offsetA         = tms - 100
	fractionOffsetA = offsetA / 10
	fractionA1      = weightA / 2
	fractionA2      = weightA / 6
	fractionB       = abi / 900
	productA        = fractionOffsetA * fractionA2
	productB        = weightB * fractionB
	labelVar        = StringVar()
	resultValue     = fractionA1 + productA + productB
	resultLabel     = Label(root, textvariable=labelVar)
	labelVar.set(resultValue)
	allLabels.append(labelVar)
	return resultValue, resultLabel, labelVar

root = Tk()
root.geometry("800x500")
TMS_DEFAULT = 42
ABI_DEFAULT = 24

GewictAbiH = 46
GewictTMSH = 44
GewictAbiC = 20
GewictTMSC = 60

GewictAbiRWTH = 95
GewictTMSRWTH = 5
GewictAbiLMU  = 51
GewictTMSLMU  = 24

abi = ABI_DEFAULT
tms = TMS_DEFAULT

Abientry,  abiPoints = setupLabel(abi, 3)
TMSpunkte, tmsPoints = setupLabel(tms, 4)

def readTextFields():
	global abi, tms
	abi = int(abiPoints.get())
	tms = int(tmsPoints.get())

def clear_func():
	TMSpunkte.insert(0, '')
	Abientry.insert( 0, '')
	addLabel(2, 5, "                                     ")
	addLabel(2, 6, "                                    ")
	addLabel(2, 7, "                                  ")
	addLabel(2, 8, "                                  ")

	for labelVar in allLabels:
		labelVar.set('')

def calculateAcceptance(acceptThreshold, points, rowIndex, notEnoughField):
	if points >= acceptThreshold:
		addLabel(2, rowIndex, "Angenommen!")
	else:
		notEnoughField.grid(row=rowIndex, column=2)

def calc_func(): 
	readTextFields()
	calc_step(GewictTMSH,    GewictAbiH,    74.7, 63.2, 5)
	calc_step(GewictTMSRWTH, GewictAbiRWTH, 63.2, 74.7, 6)
	calc_step(GewictTMSC,    GewictAbiC,    63.2, 62.6, 7)
	calc_step(GewictTMSLMU,  GewictAbiLMU,  62.6, 47,   8)

def calc_step(weightA, weightB, offset, acceptThreshold, rowIndex):
	res, lbl, strVar = doSomeCalculation(weightA, weightB)
	txt = "Nicht genug! Du brauchst " + str((acceptThreshold - res)) + " Punkte noch!"
	strVar2 = StringVar()
	strVar2.set(txt)
	notEnoughCell = Label(root, textvariable=strVar2)
	if not (strVar2 in allLabels):
		allLabels.append(strVar2)
	calculateAcceptance( acceptThreshold, res, rowIndex, notEnoughCell)
	strVar.set(res)
	lbl.grid(row=rowIndex, column=1 )

	# ErgebnisH,    LabelErgebnisH,    strVarH = doSomeCalculation(GewictTMSH,    GewictAbiH)
	# ErgebnisRWTH, LabelErgebnisRWTH, strVarR = doSomeCalculation(GewictTMSRWTH, GewictAbiRWTH)
	# ErgebnisC,    LabelErgebnisC,    strVarC = doSomeCalculation(GewictTMSC,    GewictAbiC)
	# ErgebnisLMU,  LabelErgebnisLMU , strVarL = doSomeCalculation(GewictTMSLMU,  GewictAbiLMU)
	
	# nichtgenugRWTH_text = "Nicht genug! Du brauchst " + str((74.7 - ErgebnisRWTH)) + " Punkte noch!"
	# nichtgenugH_text    = "Nicht genug! Du brauchst " + str((63.2 - ErgebnisH))    + " Punkte noch!"
	# nichtgenugLMU_text  = "Nicht genug! Du brauchst " + str((63.2 - ErgebnisLMU))  + " Punkte noch!"
	# nichtgenugC_text    = "Nicht genug! Du brauchst " + str((62.6 - ErgebnisC))    + " Punkte noch!"

	# aText = StringVar()
	# bText = StringVar()
	# cText = StringVar()
	# dText = StringVar()

	# aText.set(nichtgenugRWTH_text)
	# bText.set(nichtgenugH_text)
	# cText.set(nichtgenugLMU_text)
	# dText.set(nichtgenugC_text)
	
	# nichtgenugRWTH = Label(root, textvariable=aText)
	# nichtgenugH    = Label(root, textvariable=bText)
	# nichtgenugLMU  = Label(root, textvariable=cText)
	# nichtgenugC    = Label(root, textvariable=dText)

	# if not (aText in allLabels):
	# 	allLabels.append(aText)
	# if not (bText in allLabels):
	# 	allLabels.append(bText)
	# if not (cText in allLabels):
	# 	allLabels.append(cText)
	# if not (dText in allLabels):
	# 	allLabels.append(dText)
	# calculateAcceptance( 63.2, ErgebnisH,    5, nichtgenugH)
	# calculateAcceptance( 74.7, ErgebnisRWTH, 6, nichtgenugRWTH)
	# calculateAcceptance( 62.6, ErgebnisC,    7, nichtgenugC)
	# calculateAcceptance( 47,   ErgebnisLMU,  8, nichtgenugLMU)

	# strVarH.set(ErgebnisH)
	# strVarR.set(ErgebnisRWTH)
	# strVarC.set(ErgebnisC)
	# strVarL.set(ErgebnisLMU)

	# LabelErgebnisH.grid(    row=5, column=1 )
	# LabelErgebnisRWTH.grid( row=6, column=1 )
	# LabelErgebnisC.grid(    row=7, column=1 )
	# LabelErgebnisLMU.grid(  row=8, column=1 )

def mainFunction():
	# labels:
	addLabel(0, 0, "Zulassung nach Auswahlkriterien")
	addLabel(0, 5, "Ruprecht-Karls-Universität Heidelberg")
	addLabel(0, 6, "RWTH Aachen")
	addLabel(0, 7, "Charité – Universitätsmedizin Berlin")
	addLabel(0, 8, "LMU München")
	# buttons:
	addButton(0, "Berechnen", calc_func)
	addButton(1, "Löschen",   clear_func)
	root.mainloop()

if __name__ == "__main__":
	mainFunction()
