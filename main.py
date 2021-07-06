#Copyright 2021 J. Daniel Moore (Joshua Moore)

#This desktop application is released under the MIT license with exception to selling copies or derivatives, which is strictly prohibited. Further, this applies only to the desktop versions (Windows/Mac/Linux).  Your use of this software is consent to these terms. Any other versions, such as on mobile platforms, will be released under different licensing

#The MIT License (MIT)
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
from playsound import playsound
import webbrowser

root = Tk()
root.title("English Hacks American English Ear Trainer")
root.iconbitmap("LOGO_ICON.ico")

#NOTE: Positioning code taken from here: https://pythonprogramming.altervista.org/how-to-center-your-window-with-tkinter-in-python/

window_height = 630
window_width = 900
 
def center_screen():
	""" gets the coordinates of the center of the screen """
	global screen_height, screen_width, x_cordinate, y_cordinate
 
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
        # Coordinates of the upper left corner of the window to make the window appear in the center
	x_cordinate = int((screen_width/2) - (window_width/2))
	y_cordinate = int((screen_height/2) - (window_height/2))
	root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
 
center_screen()


exampleLists ={
"EEexamples":["see", "we", "eat", "peak", "keep"],
"IHexamples":["sit", "in", "him", "with", "fix"],
"EHexamples":["set", "men", "Ken", "best", "head"],
"AHexamples":["sat", "man", "can", "fast", "bag"],
"AWexamples":["saw", "on", "hot", "talk", "thought"],
"UHexamples":["sun", "must", "what", "other", "of"],
"ERexamples":["her", "were", "learn", "turn", "word"],
"Uexamples":["you", "who", "do", "June", "new"],
"Oexamples":["so", "go", "boat", "hope", "no"],
"UUHexamples":["book", "took", "push", "good", "put"],
"EIexamples":["say", "day", "make", "great", "they"],
"AIexamples":["I", "lie", "my", "kind", "why"],
"OIexamples":["boy", "toy", "coin", "choice", "voice"],
"OWexamples":["now", "loud", "town", "out", "how"],
"EER-IHRexamples":["here", "we're", "near", "fear", "cheer"],
"EHRexamples":["where", "hair", "fair", "bear", "care"],
"AWRexamples":["are", "car", "start", "heart", "part"],
"ORexamples":["store", "door", "more", "or", "pour"],
"EELexamples":["feel", "he'll", "deal", "we'll", "peel"],
"IHLexamples":["fill", "will", "kill", "until", "bill"],
"EHLexamples":["sell", "well", "tell", "bell", "gel"],
"AHLexamples":["pal", "malware", "gal", "shall", "Sal"],
"AWLexamples":["all", "call", "wall", "ball", "tall"],
"ERLexamples":["girl", "world", "twirl", "pearl", "curl"],
"ULexamples":["you'll", "cool", "tool", "who'll", "rule"],
"OLexamples":["old", "goal", "told", "bowl", "role"],
"Half-Lexamples":["people", "pull", "full", "tackle", "puzzle", "adult"],
"Hexamples":["he", "his", "have", "house", "heart"],
"Fexamples":["half", "from", "far", "after", "laugh"],
"Vexamples":["very", "have", "we've", "save", "move"],
"TH Voicelessexamples":["think", "thought", "earth", "through", "with"],
"TH Voicedexamples":["this", "that", "other", "whether", "the"],
"Mexamples":["me", "I'm", "make", "seem", "most"],
"Nexamples":["no", "new", "next", "on", "in"],
"NGexamples":["long", "bang", "sing", "wrong", "sung"],
"Strong Pexamples":["peak", "apply", "pass", "part", "improve"],
"Weak Pexamples":["apple", "pretend", "perform", "rapper", "keeper"],
"Stop Pexamples":["stop", "keep", "cup", "type", "hope"],
"Strong Bexamples":["big", "about", "boat", "debate", "bought"],
"Weak Bexamples":["able", "habit", "public", "maybe", "number"],
"Stop Bexamples":["web", "job", "verb", "club", "tube"],
"Strong Kexamples":["kiss", "keep", "cool", "kind", "care"],
"Weak Kexamples":["tackle", "packing", "maker", "broken", "react"],
"Stop Kexamples":["back", "take", "week", "peak", "lock"],
"Strong Gexamples":["go", "begin", "give", "great", "again"],
"Weak Gexamples":["bigger", "ugly", "guitar", "eager", "August"],
"Stop Gexamples":["bag", "big", "dog", "hug", "leg"],
"Strong Texamples":["talk", "time", "take", "attack", "hotel"],
"Weak Texamples":["today", "tonight", "winter", "filter", "splinter"],
"Stop Texamples":["it", "shot", "eat", "at", "what"],
"Strong Dexamples":["dog", "idea", "done", "door", "adult"],
"Weak Dexamples":["desire", "wonder", "defeat", "under", "advice"],
"Stop Dexamples":["bad", "we'd", "did", "made", "said"],
"Flap Dexamples":["audio", "study", "reading", "writing", "water"],
"Sexamples":["so", "see", "passing", "kiss", "lost"],
"Zexamples":["zoo", "as", "lazy", "does", "zip"],
"SHexamples":["she", "ship", "nation", "passion", "show"],
"ZHexamples":["measure", "pleasure", "occasion", "beige", "decision"],
"CHexamples":["choose", "train", "teach", "watch", "achieve"],
"Jexamples":["job", "joke", "age", "gel", "draw"],
"Rexamples":["run", "really", "around", "rest", "red"],
"Full-Lexamples":["like", "look", "lose", "allow", "land"],
"Wexamples":["we", "will", "with", "were", "want"],
"Yexamples":["yes", "you", "young", "year", "yet"],
"'Dental' Dexamples":["this(2)", "that(2)", "other(2)", "whether(2)", "the(2)"],
"'Dental' Texamples":["think(2)", "thought(2)", "within(2)", "through(2)", "theme(2)"],
"EILexamples":["fail", "male", "jail", "rail", "sale"],
"AILexamples":["I'll", "while", "file", "trial", "smile"],
"OILexamples":["oil", "boil", "toil", "royal", "loyal"],
"OWLexamples":["owl", "growl", "towel", "bowel", "foul"]
}


def isChecked():
	
	selected = []
	if cb.get() == 1:
		selected.append(EE.cget("text"))
	if cb2.get() == 1:
		selected.append(IH.cget("text"))
	if cb3.get() == 1:
		selected.append(EH.cget("text"))
	if cb4.get() == 1:
		selected.append(AH.cget("text"))
	if cb5.get() == 1:
		selected.append(AW.cget("text"))
	if cb6.get() == 1:
		selected.append(UH.cget("text"))
	if cb7.get() == 1:
		selected.append(ER.cget("text"))
	if cb8.get() == 1:
		selected.append(U.cget("text"))
	if cb9.get() == 1:
		selected.append(O.cget("text"))
	if cb10.get() == 1:
		selected.append(UUH.cget("text"))
	if cb11.get() == 1:
		selected.append(HalfL.cget("text"))
	
	if cb12.get() == 1:
		selected.append(H.cget("text"))
	if cb13.get() == 1:
		selected.append(F.cget("text"))
	if cb14.get() == 1:
		selected.append(V.cget("text"))
	if cb15.get() == 1:
		selected.append(TH.cget("text"))
	if cb16.get() == 1:
		selected.append(THVoice.cget("text"))
	if cb17.get() == 1:
		selected.append(M.cget("text"))
	if cb18.get() == 1:
		selected.append(N.cget("text"))
	if cb19.get() == 1:
		selected.append(NG.cget("text"))
	if cb20.get() == 1:
		selected.append(P.cget("text"))
	if cb21.get() == 1:
		selected.append(B.cget("text"))
	if cb22.get() == 1:
		selected.append(K.cget("text"))
	if cb23.get() == 1:
		selected.append(G.cget("text"))
	if cb24.get() == 1:
		selected.append(T.cget("text"))
	if cb25.get() == 1:
		selected.append(D.cget("text"))
	if cb26.get() == 1:
		selected.append(S.cget("text"))
	if cb27.get() == 1:
		selected.append(Z.cget("text"))
	if cb28.get() == 1:
		selected.append(SH.cget("text"))
	if cb29.get() == 1:
		selected.append(ZH.cget("text"))
	if cb30.get() == 1:
		selected.append(CH.cget("text"))
	if cb31.get() == 1:
		selected.append(J.cget("text"))
	if cb32.get() == 1:
		selected.append(R.cget("text"))
	if cb33.get() == 1:
		selected.append(L.cget("text"))
	if cb34.get() == 1:
		selected.append(W.cget("text"))
	if cb35.get() == 1:
		selected.append(Y.cget("text"))
	
	if cb36.get() == 1:
		selected.append(EI.cget("text"))
	if cb37.get() == 1:
		selected.append(AI.cget("text"))
	if cb38.get() == 1:
		selected.append(OI.cget("text"))
	if cb39.get() == 1:
		selected.append(OW.cget("text"))
	if cb40.get() == 1:
		selected.append(EER.cget("text"))
	if cb41.get() == 1:
		selected.append(EHR.cget("text"))
	if cb42.get() == 1:
		selected.append(AWR.cget("text"))
	if cb43.get() == 1:
		selected.append(OR.cget("text"))
	if cb44.get() == 1:
		selected.append(EEL.cget("text"))
	if cb45.get() == 1:
		selected.append(IHL.cget("text"))
	if cb46.get() == 1:
		selected.append(EHL.cget("text"))
	if cb47.get() == 1:
		selected.append(AHL.cget("text"))
	if cb48.get() == 1:
		selected.append(AWL.cget("text"))
	if cb50.get() == 1:
		selected.append(ERL.cget("text"))
	if cb51.get() == 1:
		selected.append(UL.cget("text"))
	if cb52.get() == 1:
		selected.append(OL.cget("text"))


	if cb54.get() == 1:
		selected.append(wP.cget("text"))
	if cb55.get() == 1:
		selected.append(stopP.cget("text"))
	if cb56.get() == 1:
		selected.append(wB.cget("text"))
	if cb57.get() == 1:
		selected.append(stopB.cget("text"))
	if cb58.get() == 1:
		selected.append(wT.cget("text"))
	if cb59.get() == 1:
		selected.append(stopT.cget("text"))
	if cb60.get() == 1:
		selected.append(wD.cget("text"))
	if cb61.get() == 1:
		selected.append(flapD.cget("text"))
	if cb62.get() == 1:
		selected.append(stopD.cget("text"))
	if cb63.get() == 1:
		selected.append(wK.cget("text"))
	if cb64.get() == 1:
		selected.append(stopK.cget("text"))
	if cb65.get() == 1:
		selected.append(wG.cget("text"))
	if cb66.get() == 1:
		selected.append(stopG.cget("text"))
	if cb67.get() == 1:
		selected.append(dentalD.cget("text"))
	if cb68.get() == 1:
		selected.append(dentalT.cget("text"))
	if cb69.get() == 1:
		selected.append(EIL.cget("text"))
	if cb70.get() == 1:
		selected.append(AIL.cget("text"))
	if cb71.get() == 1:
		selected.append(OIL.cget("text"))
	if cb72.get() == 1:
		selected.append(OWL.cget("text"))
	
	return selected
	

	
cb = IntVar()
cb2 = IntVar()
cb3 = IntVar()
cb4 = IntVar()
cb5 = IntVar()
cb6 = IntVar()
cb7 = IntVar()
cb8 = IntVar()
cb9 = IntVar()
cb10 = IntVar()
cb11 = IntVar()

cb12 = IntVar()
cb13 = IntVar()
cb14 = IntVar()
cb15 = IntVar()
cb16 = IntVar()
cb17 = IntVar()
cb18 = IntVar()
cb19 = IntVar()
cb20 = IntVar()
cb21 = IntVar()
cb22 = IntVar()
cb23 = IntVar()
cb24 = IntVar()
cb25 = IntVar()
cb26 = IntVar()
cb27 = IntVar()
cb28 = IntVar()
cb29 = IntVar()
cb30 = IntVar()
cb31 = IntVar()
cb32 = IntVar()
cb33 = IntVar()
cb34 = IntVar()
cb35 = IntVar()

cb36 = IntVar()
cb37 = IntVar()
cb38 = IntVar()
cb39 = IntVar()
cb40 = IntVar()
cb41 = IntVar()
cb42 = IntVar()
cb43 = IntVar()
cb44 = IntVar()
cb45 = IntVar()
cb46 = IntVar()
cb47 = IntVar()
cb48 = IntVar()
cb50 = IntVar()
cb51 = IntVar()
cb52 = IntVar()


cb54 = IntVar()
cb55 = IntVar()
cb56 = IntVar()
cb57 = IntVar()
cb58 = IntVar()
cb59 = IntVar()
cb60 = IntVar()
cb61 = IntVar()
cb62 = IntVar()
cb63 = IntVar()
cb64 = IntVar()
cb65 = IntVar()
cb66 = IntVar()

cb67 = IntVar()
cb68 = IntVar()

cb69 = IntVar()
cb70 = IntVar()
cb71 = IntVar()
cb72 = IntVar()




wrapper = LabelFrame(root)
wrapper["borderwidth"] = 0


mainHeading = Label(wrapper, text="Sound Selection", font="times 36 underline")
headDesc = Label(wrapper, text="Please select between 1 and 4 sounds to work with")

mode = LabelFrame(wrapper, text="Mode", bd=5, bg="#F0F8FF", font="times 20 bold")

r=IntVar()

r.set(1)

basic = Radiobutton(mode, text="Basic Sounds Only", variable=r, value=1, bg="#F0F8FF")
examples = Radiobutton(mode, text="Example Words", variable=r, value=2, bg="#F0F8FF")



#Vowel Section and inner divisions
vowelSection = LabelFrame(wrapper, text ="Vowel Sounds", bd=3, bg="white", font="times 20 bold")
mono = LabelFrame(vowelSection, text="Monophthongs")
dipth = LabelFrame(vowelSection, text="Diphthongs")
rcolor = LabelFrame(vowelSection, text="R-Colored")
lcolor = LabelFrame(vowelSection, text="L-Colored")


#Vowel check boxes
EE = Checkbutton(mono, text="EE", variable=cb, onvalue=1, offvalue=0, command=isChecked)
IH = Checkbutton(mono, text="IH", variable=cb2, onvalue=1, offvalue=0, command=isChecked)
EH = Checkbutton(mono, text="EH", variable=cb3, onvalue=1, offvalue=0, command=isChecked)
AH = Checkbutton(mono, text="AH", variable=cb4, onvalue=1, offvalue=0, command=isChecked)
AW = Checkbutton(mono, text="AW", variable=cb5, onvalue=1, offvalue=0, command=isChecked)
UH = Checkbutton(mono, text="UH", variable=cb6, onvalue=1, offvalue=0, command=isChecked)
ER = Checkbutton(mono, text="ER", variable=cb7, onvalue=1, offvalue=0, command=isChecked)
U = Checkbutton(mono, text="U", variable=cb8, onvalue=1, offvalue=0, command=isChecked)
O = Checkbutton(mono, text="O", variable=cb9, onvalue=1, offvalue=0, command=isChecked)
UUH = Checkbutton(mono, text="UUH", variable=cb10, onvalue=1, offvalue=0, command=isChecked)
HalfL = Checkbutton(mono, text="Half-L", variable=cb11, onvalue=1, offvalue=0, command=isChecked)

EI = Checkbutton(dipth, text="EI", variable=cb36, onvalue=1, offvalue=0, command=isChecked)
AI = Checkbutton(dipth, text="AI", variable=cb37, onvalue=1, offvalue=0, command=isChecked)
OI = Checkbutton(dipth, text="OI", variable=cb38, onvalue=1, offvalue=0, command=isChecked)
OW = Checkbutton(dipth, text="OW", variable=cb39, onvalue=1, offvalue=0, command=isChecked)

EER = Checkbutton(rcolor, text="EER-IHR", variable=cb40, onvalue=1, offvalue=0, command=isChecked)
EHR = Checkbutton(rcolor, text="EHR", variable=cb41, onvalue=1, offvalue=0, command=isChecked)
AWR = Checkbutton(rcolor, text="AWR", variable=cb42, onvalue=1, offvalue=0, command=isChecked)
OR = Checkbutton(rcolor, text="OR", variable=cb43, onvalue=1, offvalue=0, command=isChecked)

EEL = Checkbutton(lcolor, text="EEL", variable=cb44, onvalue=1, offvalue=0, command=isChecked)
IHL = Checkbutton(lcolor, text="IHL", variable=cb45, onvalue=1, offvalue=0, command=isChecked)
EHL = Checkbutton(lcolor, text="EHL", variable=cb46, onvalue=1, offvalue=0, command=isChecked)
AHL = Checkbutton(lcolor, text="AHL", variable=cb47, onvalue=1, offvalue=0, command=isChecked)
AWL = Checkbutton(lcolor, text="AWL", variable=cb48, onvalue=1, offvalue=0, command=isChecked)
ERL = Checkbutton(lcolor, text="ERL", variable=cb50, onvalue=1, offvalue=0, command=isChecked)
UL = Checkbutton(lcolor, text="UL", variable=cb51, onvalue=1, offvalue=0, command=isChecked)
OL = Checkbutton(lcolor, text="OL", variable=cb52, onvalue=1, offvalue=0, command=isChecked)
EIL = Checkbutton(lcolor, text="EIL", variable=cb69, onvalue=1, offvalue=0, command=isChecked)
AIL = Checkbutton(lcolor, text="AIL", variable=cb70, onvalue=1, offvalue=0, command=isChecked)
OIL = Checkbutton(lcolor, text="OIL", variable=cb71, onvalue=1, offvalue=0, command=isChecked)
OWL = Checkbutton(lcolor, text="OWL", variable=cb72, onvalue=1, offvalue=0, command=isChecked)



ConsonantSection = LabelFrame(wrapper, text ="Consonant Sounds", bd=3, bg="white", font="times 20 bold")

stop = LabelFrame(ConsonantSection, text="Stop Consonants")
consonantSounds = LabelFrame(ConsonantSection, text="Other Consonant Sounds")
dentalFrame = LabelFrame(ConsonantSection, text="TH Sounds")



#Consonant check boxes
F = Checkbutton(consonantSounds, text="F", variable=cb13, onvalue=1, offvalue=0, command=isChecked)
V = Checkbutton(consonantSounds, text="V", variable=cb14, onvalue=1, offvalue=0, command=isChecked)
TH = Checkbutton(dentalFrame, text="TH Voiceless", variable=cb15, onvalue=1, offvalue=0, command=isChecked)
THVoice = Checkbutton(dentalFrame, text="TH Voiced", variable=cb16, onvalue=1, offvalue=0, command=isChecked)
S = Checkbutton(consonantSounds, text="S", variable=cb26, onvalue=1, offvalue=0, command=isChecked)
Z = Checkbutton(consonantSounds, text="Z", variable=cb27, onvalue=1, offvalue=0, command=isChecked)
SH = Checkbutton(consonantSounds, text="SH", variable=cb28, onvalue=1, offvalue=0, command=isChecked)
ZH = Checkbutton(consonantSounds, text="ZH", variable=cb29, onvalue=1, offvalue=0, command=isChecked)
M = Checkbutton(consonantSounds, text="M", variable=cb17, onvalue=1, offvalue=0, command=isChecked)
N = Checkbutton(consonantSounds, text="N", variable=cb18, onvalue=1, offvalue=0, command=isChecked)
NG = Checkbutton(consonantSounds, text="NG", variable=cb19, onvalue=1, offvalue=0, command=isChecked)
P = Checkbutton(stop, text="Strong P", variable=cb20, onvalue=1, offvalue=0, command=isChecked)
B = Checkbutton(stop, text="Strong B", variable=cb21, onvalue=1, offvalue=0, command=isChecked)
K = Checkbutton(stop, text="Strong K", variable=cb22, onvalue=1, offvalue=0, command=isChecked)
G = Checkbutton(stop, text="Strong G", variable=cb23, onvalue=1, offvalue=0, command=isChecked)
T = Checkbutton(stop, text="Strong T", variable=cb24, onvalue=1, offvalue=0, command=isChecked)
D = Checkbutton(stop, text="Strong D", variable=cb25, onvalue=1, offvalue=0, command=isChecked)
CH = Checkbutton(consonantSounds, text="CH", variable=cb30, onvalue=1, offvalue=0, command=isChecked)
J = Checkbutton(consonantSounds, text="J", variable=cb31, onvalue=1, offvalue=0, command=isChecked)
R = Checkbutton(consonantSounds, text="R", variable=cb32, onvalue=1, offvalue=0, command=isChecked)
L = Checkbutton(consonantSounds, text="Full-L", variable=cb33, onvalue=1, offvalue=0, command=isChecked)
W = Checkbutton(consonantSounds, text="W", variable=cb34, onvalue=1, offvalue=0, command=isChecked)
Y = Checkbutton(consonantSounds, text="Y", variable=cb35, onvalue=1, offvalue=0, command=isChecked)
H = Checkbutton(consonantSounds, text="H", variable=cb12, onvalue=1, offvalue=0, command=isChecked)

wP = Checkbutton(stop, text="Weak P", variable=cb54, onvalue=1, offvalue=0, command=isChecked)
wB = Checkbutton(stop, text="Weak B", variable=cb56, onvalue=1, offvalue=0, command=isChecked)
wK = Checkbutton(stop, text="Weak K", variable=cb63, onvalue=1, offvalue=0, command=isChecked)
wG = Checkbutton(stop, text="Weak G", variable=cb65, onvalue=1, offvalue=0, command=isChecked)
wT = Checkbutton(stop, text="Weak T", variable=cb58, onvalue=1, offvalue=0, command=isChecked)
wD = Checkbutton(stop, text="Weak D", variable=cb60, onvalue=1, offvalue=0, command=isChecked)
stopP = Checkbutton(stop, text="Stop P", variable=cb55, onvalue=1, offvalue=0, command=isChecked)
stopB = Checkbutton(stop, text="Stop B", variable=cb57, onvalue=1, offvalue=0, command=isChecked)
stopK = Checkbutton(stop, text="Stop K", variable=cb64, onvalue=1, offvalue=0, command=isChecked)
stopG = Checkbutton(stop, text="Stop G", variable=cb66, onvalue=1, offvalue=0, command=isChecked)
stopT = Checkbutton(stop, text="Stop T", variable=cb59, onvalue=1, offvalue=0, command=isChecked)
stopD = Checkbutton(stop, text="Stop D", variable=cb62, onvalue=1, offvalue=0, command=isChecked)
flapD = Checkbutton(stop, text="Flap D", variable=cb61, onvalue=1, offvalue=0, command=isChecked)

dentalD = Checkbutton(dentalFrame, text="'Dental' D", variable=cb67, onvalue=1, offvalue=0, command=isChecked)
dentalT = Checkbutton(dentalFrame, text="'Dental' T", variable=cb68, onvalue=1, offvalue=0, command=isChecked)



def modeCheck():
	if(r.get() == 1 and len(isChecked()) == 1):
		messagebox.showinfo("message", "Basic sound mode selected, but with only one sound. Changing to example words mode.")
		r.set(2)
	elif(r.get() == 2 and len(isChecked()) > 1):
		messagebox.showinfo("message", "Example words mode selected, but with more than one sound. Changing to basic sound mode.")


def exampleWords():
	if(r.get() == 2):
		newSelected = []
		for word in exampleLists[str(isChecked()[0])+"examples"]:
			newSelected.append(word)
			print(newSelected)
		return newSelected


def startCheck():
		
	if(len(isChecked()) == 1):
		soundOne = "C:/Program Files (x86)/English Hacks Ear Trainer/{}examples/{}.mp3".format(isChecked()[0], exampleWords()[0])
		start.config(command=buttonClicked())
	elif(len(isChecked()) == 2):
		soundOne = "C:/Program Files (x86)/English Hacks Ear Trainer/{}.mp3".format(isChecked()[0])
		soundTwo = "C:/Program Files (x86)/English Hacks Ear Trainer/{}.mp3".format(isChecked()[1])
		start.config(command=buttonClicked())
	elif(len(isChecked()) == 3):
		soundOne = "C:/Program Files (x86)/English Hacks Ear Trainer/{}.mp3".format(isChecked()[0])
		soundTwo = "C:/Program Files (x86)/English Hacks Ear Trainer/{}.mp3".format(isChecked()[1])
		soundThree = "C:/Program Files (x86)/English Hacks Ear Trainer/{}.mp3".format(isChecked()[2])
		start.config(command=buttonClicked())
	elif(len(isChecked()) == 4):
		soundOne = "C:/Program Files (x86)/English Hacks Ear Trainer/{}.mp3".format(isChecked()[0])
		soundTwo = "C:/Program Files (x86)/English Hacks Ear Trainer/{}.mp3".format(isChecked()[1])
		soundThree = "C:/Program Files (x86)/English Hacks Ear Trainer/{}.mp3".format(isChecked()[2])
		soundFour = "C:/Program Files (x86)/English Hacks Ear Trainer/{}.mp3".format(isChecked()[3])
		start.config(command=buttonClicked())
	else:
		messagebox.showinfo("message", "Please select between 1 and 4 sounds to work with.")


start = Button(root, text="Start!", width = 10, bg="blue", fg="white", font="40", command=lambda:[modeCheck(), startCheck()])


#Create the window for the ear trainer itself
def buttonClicked():
	trainer = Toplevel(root)
	root.withdraw()
	trainer.title("Ear Trainer")
	trainer.iconbitmap("LOGO_ICON.ico")
	trainer.geometry("1050x750")
	
	window_height = 560
	window_width = 1550
 
	def center_screen():
		""" gets the coordinates of the center of the screen """
		global screen_height, screen_width, x_cordinate, y_cordinate
 
		screen_width = trainer.winfo_screenwidth()
		screen_height = trainer.winfo_screenheight()
        	# Coordinates of the upper left corner of the window to make the window appear in the center
		x_cordinate = int((screen_width/2) - (window_width/2))
		y_cordinate = int((screen_height/2) - (window_height/2))
		trainer.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
 
	center_screen()

	#button that closes the trainer window and returns to the main screen
	def goBack():
		trainer.destroy()
		root.deiconify()

	#button that will replay the audio that played upon starting
	def replayAudio():
		
		playsound(firstSound, False)
	
	def removeWords(listed, index):
		listed.pop(index)
		print(listed)
		return listed

	
#########################################################################################################################

	#ONLY ONE SOUND
	if(len(isChecked()) == 1):

		def getRandom():
			randomStart = random.randint(0, len(exampleWords())-1)
			return randomStart
	
		randomNum = getRandom()

		
		firstSound = "C:/Program Files (x86)/English Hacks Ear Trainer/{}examples/{}.mp3".format(isChecked()[0], exampleWords()[randomNum])

		
		
		playsound(firstSound, False)

				
		def replayAnswer():
			
			playsound(firstSound, False)
		
		examplesNew = exampleWords()
		examplesNew.pop(randomNum)
		
		def ending(button):
			messagebox.showinfo("message", "End of examples. Returning to Sound Selection")
			trainer.destroy()
			root.deiconify()

		#button that will go to next question
		def changeStart(button):

			def getRandomNew():
				randomStart = random.randint(0, len(examplesNew)-1)
				return randomStart

			randomNum2 = getRandomNew()

			firstSound = "C:/Program Files (x86)/English Hacks Ear Trainer/{}examples/{}.mp3".format(isChecked()[0], examplesNew[randomNum2])
	
			answerLabel.config(text=examplesNew[randomNum2])

			answerLabel.pack(ipadx=25)
			
			playsound(firstSound, False)

			
		

			def replayAnswer():
				playsound(firstSound, False)

			examplesNew.pop(randomNum2)
			print(examplesNew)
			
		
			def newReplay():
				playsound(firstSound, False)

			replay.config(command=newReplay)

			if(len(examplesNew) == 0):
				moveNext.bind("<Button-1>", ending)

		



		answerHolder = LabelFrame(trainer, pady=180)
		answerLabel = Label(answerHolder, text=exampleWords()[randomNum], font = "times 52", width=5, height=2, bd = 4, bg= "white", fg= "black", relief=SUNKEN)

		answerHolder.pack(fill=BOTH)
		answerLabel.pack(ipadx=25)
		
	


		back = Button(trainer, text="Back to Selection", command=goBack).pack(side=LEFT, padx=(15, 0))
		replay = Button(trainer, text="Replay Audio", command=replayAudio)
		replay.pack(side=LEFT, padx=(150,15))
		moveNext = Button(trainer, text="Next")
		moveNext.bind("<Button-1>", changeStart)
		moveNext.pack(side=RIGHT, padx=(0, 15))

		


########################################################################################################################################

	#MORE THAN ONE SOUND
	if(len(isChecked()) > 1):
		#get a random number from the list in isChecked to randomly play one of the selected sound's audio first
		def getRandom():
			randomStart = random.randint(0, len(isChecked())-1)
			return randomStart
	
		randomNum = getRandom()

		
		firstSound = "C:/Program Files (x86)/English Hacks Ear Trainer/{}.mp3".format(isChecked()[randomNum])
	
		
		playsound(firstSound, False)
		
	
		#button that will show the answer
		def showAnswer():
			
			soundList = []

			if(len(isChecked()) == 2):
				soundOne = "C:/Program Files (x86)/English Hacks Ear Trainer/{}.mp3".format(isChecked()[0])
				answerLabel.pack(side=LEFT, padx=60, ipadx=75)
				soundList.append(soundOne)
				soundTwo = "C:/Program Files (x86)/English Hacks Ear Trainer/{}.mp3".format(isChecked()[1])
				otherLabel.pack(side=RIGHT, padx=60, ipadx=75)
				soundList.append(soundTwo)
			elif(len(isChecked()) == 3):
				soundOne = "C:/Program Files (x86)/English Hacks Ear Trainer/{}.mp3".format(isChecked()[0])
				answerLabel.pack(side=LEFT, padx=20, ipadx=75)
				soundTwo = "C:/Program Files (x86)/English Hacks Ear Trainer/{}.mp3".format(isChecked()[1])
				otherLabel.pack(side=LEFT, padx=20, ipadx=75)
				soundThree = "C:/Program Files (x86)/English Hacks Ear Trainer/{}.mp3".format(isChecked()[2])
				label3.config(text=isChecked()[2], font = "times 52", width=5, height=2, bd = 4, bg= "white", fg= "black", relief=SUNKEN)
				label3.pack(side=LEFT, padx=20, ipadx=75)
			elif(len(isChecked()) == 4):
				soundOne = "C:/Program Files (x86)/English Hacks Ear Trainer/{}.mp3".format(isChecked()[0])
				answerLabel.pack(side=LEFT, ipadx=75)
				soundTwo = "C:/Program Files (x86)/English Hacks Ear Trainer/{}.mp3".format(isChecked()[1])
				otherLabel.pack(side=LEFT, ipadx=75)
				soundThree = "C:/Program Files (x86)/English Hacks Ear Trainer/{}.mp3".format(isChecked()[2])
				label3.config(text=isChecked()[2], font = "times 52", width=5, height=2, bd = 4, bg= "white", fg= "black", relief=SUNKEN)
				label3.pack(side=LEFT, ipadx=75)
				soundFour = "C:/Program Files (x86)/English Hacks Ear Trainer/{}.mp3".format(isChecked()[3])
				label4.config(text=isChecked()[3], font = "times 52", width=5, height=2, bd = 4, bg= "white", fg= "black", relief=SUNKEN)
				label4.pack(side=LEFT, ipadx=75)

			emptyHolder.pack_forget()

			
			
			
			playsound(firstSound, False)
		
			def normalStateOther():
				otherLabel.config(bg= "white", fg= "black", font = "times 52")

			def normalStateAnswer():
				answerLabel.config(bg= "white", fg= "black", font = "times 52")

			def normalState3():
				label3.config(bg= "white", fg= "black", font = "times 52")

			def normalState4():
				label4.config(bg= "white", fg= "black", font = "times 52")



			def answerLabelUpdate():
				answerLabel.config(bg= "white", fg= "black", font = "times 52")
				otherLabel.config(bg= "#FEFEDA", fg= "blue", font = "times 52 bold")
				playsound(soundTwo, False)
				
			
			def otherLabelUpdate():
				otherLabel.config(bg= "white", fg= "black", font = "times 52")
				label3.config(bg= "#FEFEDA", fg= "blue", font = "times 52 bold")
				playsound(soundThree, False)

			def label3Update():
				label3.config(bg= "white", fg= "black", font = "times 52")
				label4.config(bg= "#FEFEDA", fg= "blue", font = "times 52 bold")
				playsound(soundFour, False)
			

			#Highlight the answer after clicking "show answer" button
			if(answerLabel.cget("text") == isChecked()[randomNum]):
				answerLabel.config(bg= "#FEFEDA", fg= "blue", font = "times 52 bold")
				answerLabel.after(1000, normalStateAnswer)
			elif(otherLabel.cget("text") == isChecked()[randomNum]):
				otherLabel.config(bg= "#FEFEDA", fg= "blue", font = "times 52 bold")
				otherLabel.after(1000, normalStateOther)
			elif(label3.cget("text") == isChecked()[randomNum]):
				label3.config(bg= "#FEFEDA", fg= "blue", font = "times 52 bold")
				label3.after(1000, normalState3)
			elif(label4.cget("text") == isChecked()[randomNum]):
				label4.config(bg= "#FEFEDA", fg= "blue", font = "times 52 bold")
				label4.after(1000, normalState4)


			def replayAnswer():
				
				playsound(soundOne, False)
				
				if(answerLabel.cget("text") == isChecked()[0]):
					answerLabel.config(bg= "#FEFEDA", fg= "blue", font = "times 52 bold")
					answerLabel.after(1000, answerLabelUpdate)
					otherLabel.after(2000, otherLabelUpdate)
					label3.after(3000, label3Update)
					label4.after(4000, normalState4)
					


			answer.config(text = "Compare Sounds", command=replayAnswer, bg="blue", font="bold", fg="white")
			
		
		
		#button that will go to next question
		def changeStart(button):
			#get a random number from the list in isChecked to randomly play one of the selected sound's audio first
			randomNum2 = getRandom()
			

			firstSound = "C:/Program Files (x86)/English Hacks Ear Trainer/{}.mp3".format(isChecked()[randomNum2])
	

			
			playsound(firstSound, False)

			answerLabel.pack_forget()
			otherLabel.pack_forget()
			label3.pack_forget()
			label4.pack_forget()
			emptyHolder.pack(pady=(0, 82))


			def showAnswerNew():
				emptyHolder.pack_forget()

				
		

				
				playsound(firstSound, False)
		
				if(len(isChecked()) == 2):
					soundOne = "C:/Program Files (x86)/English Hacks Ear Trainer/{}.mp3".format(isChecked()[0])
					answerLabel.pack(side=LEFT, padx=60, ipadx=75)
					soundTwo = "C:/Program Files (x86)/English Hacks Ear Trainer/{}.mp3".format(isChecked()[1])
					otherLabel.pack(side=RIGHT, padx=60, ipadx=75)
				elif(len(isChecked()) == 3):
					soundOne = "C:/Program Files (x86)/English Hacks Ear Trainer/{}.mp3".format(isChecked()[0])
					answerLabel.pack(side=LEFT, padx=50, ipadx=75)
					soundTwo = "C:/Program Files (x86)/English Hacks Ear Trainer/{}.mp3".format(isChecked()[1])
					otherLabel.pack(side=LEFT, padx=50, ipadx=75)
					soundThree = "C:/Program Files (x86)/English Hacks Ear Trainer/{}.mp3".format(isChecked()[2])
					label3.config(text=isChecked()[2], font = "times 52", width=5, height=2, bd = 4, bg= "white", fg= "black", relief=SUNKEN)
					label3.pack(side=LEFT, padx=50, ipadx=75)
				elif(len(isChecked()) == 4):
					soundOne = "C:/Program Files (x86)/English Hacks Ear Trainer/{}.mp3".format(isChecked()[0])
					answerLabel.pack(side=LEFT, padx=20, ipadx=75)
					soundTwo = "C:/Program Files (x86)/English Hacks Ear Trainer/{}.mp3".format(isChecked()[1])
					otherLabel.pack(side=LEFT, padx=20, ipadx=75)
					soundThree = "C:/Program Files (x86)/English Hacks Ear Trainer/{}.mp3".format(isChecked()[2])
					label3.config(text=isChecked()[2], font = "times 52", width=5, height=2, bd = 4, bg= "white", fg= "black", relief=SUNKEN)
					label3.pack(side=LEFT, padx=20, ipadx=75)
					soundFour = "C:/Program Files (x86)/English Hacks Ear Trainer/{}.mp3".format(isChecked()[3])
					label4.config(text=isChecked()[3], font = "times 52", width=5, height=2, bd = 4, bg= "white", fg= "black", relief=SUNKEN)
					label4.pack(side=LEFT, padx=20, ipadx=75)

				def normalStateOther():
					otherLabel.config(bg= "white", fg= "black", font = "times 52")

				def normalStateAnswer():
					answerLabel.config(bg= "white", fg= "black", font = "times 52")

				def normalState3():
					label3.config(bg= "white", fg= "black", font = "times 52")

				def normalState4():
					label4.config(bg= "white", fg= "black", font = "times 52")



				def answerLabelUpdate():
					answerLabel.config(bg= "white", fg= "black", font = "times 52")
					otherLabel.config(bg= "#FEFEDA", fg= "blue", font = "times 52 bold")
					playsound(soundTwo, False)
				
			
				def otherLabelUpdate():
					otherLabel.config(bg= "white", fg= "black", font = "times 52")
					label3.config(bg= "#FEFEDA", fg= "blue", font = "times 52 bold")
					playsound(soundThree, False)

				def label3Update():
					label3.config(bg= "white", fg= "black", font = "times 52")
					label4.config(bg= "#FEFEDA", fg= "blue", font = "times 52 bold")
					playsound(soundFour, False)
			

				#Highlight the answer after clicking "show answer" button
				if(answerLabel.cget("text") == isChecked()[randomNum2]):
					answerLabel.config(bg= "#FEFEDA", fg= "blue", font = "times 52 bold")
					answerLabel.after(1000, normalStateAnswer)
				elif(otherLabel.cget("text") == isChecked()[randomNum2]):
					otherLabel.config(bg= "#FEFEDA", fg= "blue", font = "times 52 bold")
					otherLabel.after(1000, normalStateOther)
				elif(label3.cget("text") == isChecked()[randomNum2]):
					label3.config(bg= "#FEFEDA", fg= "blue", font = "times 52 bold")
					label3.after(1000, normalState3)
				elif(label4.cget("text") == isChecked()[randomNum2]):
					label4.config(bg= "#FEFEDA", fg= "blue", font = "times 52 bold")
					label4.after(1000, normalState4)


				def replayAnswer():
					
					playsound(soundOne, False)
				
					if(answerLabel.cget("text") == isChecked()[0]):
						answerLabel.config(bg= "#FEFEDA", fg= "blue", font = "times 52 bold")
						answerLabel.after(1000, answerLabelUpdate)
						otherLabel.after(2000, otherLabelUpdate)
						label3.after(3000, label3Update)
						label4.after(4000, normalState4)


				answer.config(text = "Compare Sounds", command=replayAnswer, bg="blue", font="bold", fg="white")
				

		
			answer.config(text = "Show Answer", command=showAnswerNew, bg="white", fg="black")
			
		
			def newReplay():
				
				playsound(firstSound, False)

			replay.config(command=newReplay)


		answerHolder = LabelFrame(trainer, pady=170)
		emptyHolder = Label(answerHolder, text="Listen Closely...", font = "times 52")
		answerLabel = Label(answerHolder, text=isChecked()[0], font = "times 52", width=5, height=2, bd = 4, bg= "white", fg= "black", relief=SUNKEN)
		otherLabel = Label(answerHolder, text=isChecked()[1], font = "times 52", width=5, height=2, bd = 4, bg= "white", fg= "black", relief=SUNKEN)
		label3 = Label(answerHolder)
		label4 = Label(answerHolder)

		answerHolder.pack(fill=BOTH)
		emptyHolder.pack(pady=(0, 82))
	


		back = Button(trainer, text="Back to Selection", command=goBack).pack(side=LEFT, padx=(15, 0))
		replay = Button(trainer, text="Replay Audio", command=replayAudio)
		replay.pack(side=LEFT, padx=(150,15))
		answer = Button(trainer, text="Show Answer", command=showAnswer)
		answer.pack(side=LEFT)
		moveNext = Button(trainer, text="Next")
		moveNext.bind("<Button-1>", changeStart)
		moveNext.pack(side=RIGHT, padx=(0, 15))

	#reshow the main window if X is hit on trainer window
	trainer.protocol("WM_DELETE_WINDOW", goBack)

	
	trainer.mainloop()

def openYoutube():
	webbrowser.open("https://www.youtube.com/channel/UCTnrAJf55CqtRnevjwdISrA")

def openTranscription():
	webbrowser.open("https://docs.google.com/document/d/1JaEGFgOFcwOZ1kz_6fpwpLx-ePTYnVPu/")

def openSite():
	webbrowser.open("https://jdanielauthor.com/downloads/")


copyright = Label(root, text="Copyright 2021 J. Daniel Moore", font="times 11")

transcript = Button(root, text="English Hacks Phonetic Transcription Guide", command=openTranscription)
youtube = Button(root, text="English Hacks YouTube Channel", command=openYoutube)
resources = Button(root, text="More Resources", command=openSite)

#Pack items onto the screen
wrapper.pack(fill="both", expand="yes", padx=80, pady=(5, 10))
mainHeading.pack()
headDesc.pack()
mode.pack(pady=5, ipady=5)
vowelSection.pack(side="left", padx=50, ipadx=15)
mono.pack(pady=3)
dipth.pack(pady=3)
rcolor.pack(pady=3)
lcolor.pack(pady=3) 
ConsonantSection.pack(side="right", padx=10)
stop.pack(pady=3, padx=20, ipadx=30)
dentalFrame.pack(side="left", pady=3, padx=20)
consonantSounds.pack(side="left", pady=3, padx=5)
start.pack(pady=(0, 15), ipadx=10, ipady=10)

transcript.pack(side=LEFT, padx=10)
youtube.pack(side=LEFT, padx=10)
resources.pack(side=LEFT, padx=10, pady=10)
copyright.pack(side=RIGHT, padx=10)

#Place Vowels
EE.grid(row=0, column=0)
IH.grid(row=0, column=1)
EH.grid(row=0, column=2)
AH.grid(row=0, column=3)
AW.grid(row=1, column=0)
UH.grid(row=1, column=1)
ER.grid(row=1, column=2)
U.grid(row=1, column=3)
O.grid(row=2, column=0)
UUH.grid(row=2, column=1)
HalfL.grid(row=2, column=2)

EI.grid(row=0, column=0)
AI.grid(row=0, column=1)
OI.grid(row=0, column=2)
OW.grid(row=0, column=3)

EER.grid(row=0, column=0)
EHR.grid(row=0, column=1)
AWR.grid(row=0, column=2)
OR.grid(row=0, column=3)

EEL.grid(row=0, column=0)
IHL.grid(row=0, column=1)
EHL.grid(row=0, column=2)
AHL.grid(row=0, column=3)
AWL.grid(row=1, column=0)
ERL.grid(row=1, column=1)
UL.grid(row=1, column=2)
OL.grid(row=1, column=3)
EIL.grid(row=2, column=0)
AIL.grid(row=2, column=1)
OIL.grid(row=2, column=2)
OWL.grid(row=2, column=3)


#Place Consonants
F.grid(row=0, column=0)
V.grid(row=0, column=1)
S.grid(row=0, column=2)
Z.grid(row=0, column=3)
SH.grid(row=1, column=0)
ZH.grid(row=1, column=1)
CH.grid(row=1, column=2)
J.grid(row=1, column=3)
R.grid(row=2, column=0)
L.grid(row=2, column=1)
W.grid(row=2, column=2)
Y.grid(row=2, column=3)
M.grid(row=3, column=0)
N.grid(row=3, column=1)
NG.grid(row=3, column=2)
H.grid(row=3, column=3)

P.grid(row=0, column=0)
wP.grid(row=0, column=1)
stopP.grid(row=0, column=2)
B.grid(row=1, column=0)
wB.grid(row=1, column=1)
stopB.grid(row=1, column=2)
K.grid(row=2, column=0)
wK.grid(row=2, column=1)
stopK.grid(row=2, column=2)
G.grid(row=3, column=0)
wG.grid(row=3, column=1)
stopG.grid(row=3, column=2)
T.grid(row=4, column=0)
wT.grid(row=4, column=1)
stopT.grid(row=4, column=2)
D.grid(row=5, column=0)
wD.grid(row=5, column=1)
stopD.grid(row=5, column=2)
flapD.grid(row=5, column=3)

TH.grid(row=0, column=0)
THVoice.grid(row=2, column=0)
dentalT.grid(row=1, column=0)
dentalD.grid(row=3, column=0)

#Places modes
basic.pack(side=LEFT)
examples.pack(side=LEFT)


root.mainloop()
