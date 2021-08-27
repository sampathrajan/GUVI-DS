ones={1:"ONE ",2:"TWO ",3:"THREE ",4:"FOUR ",5:"FIVE ",6:"SIX ",7:"SEVEN ",8:"EIGHT ",9:"NINE "}
tens={1:"TEN ",2:"TWENTY ",3:"THIRTY ",4:"FOURTY ",5:"FIFTY ",6:"SIXTY ",7:"SEVENTY ",8:"EIGHTY ",9:"NINTY "}
teens={11:"ELEVEN ",12:"TWELVE ",13:"THIRTEEN ",14:"FOURTEEN ",15:"FIFTEEN ",16:"SIXTEEN ",17:"SEVENTEEN ",18:"EIGHTEEN ",19:"NINETEEN "}
max=["HUNDRED ","THOUSAND ","LAKH ","CRORE "]

            
def digit2words(val):
    out=""
    if len(str(val))==1:
        if(val>0):
            out+=" "+ones[val]
    elif len(str(val))==2:
        if(val>10 and val<20):
            out+=teens[val]
        else:
            out+=tens[val//10]
            out+=digit2words(val%10)
    elif len(str(val))==3:
            out+=digit2words(val//100)
            if val%100>0:
                out+=max[0]+"AND "
                out+=digit2words(val%100)
    elif len(str(val))==4 or len(str(val))==5:
            out+=digit2words(val//1000)
            out+=max[1]
            out+=digit2words(val%1000)
    elif len(str(val))==6 or len(str(val))==7:
            out+=digit2words(val//100000)
            out+=max[2]
            out+=digit2words(val%100000)
    elif len(str(val))>7:
            out+=digit2words(val//10000000)
            out+=max[3]
            out+=digit2words(val%10000000)
    return out
a=int(input())
print(digit2words(a) +"ONLY")
