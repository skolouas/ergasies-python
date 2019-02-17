import os
#anoigma arxeiou
f=open("sxolia.py","r")
for line in f.readlines() :
    if "#" not in line: 
        print (line, end="")
    elif line.index("#") > 0:
        quote_count=0
        quote_count2=0
        #mona kai dipla antistoixa aytakia
        found_single = False    
        found_double = False    
        for c in line:
            if c == '"' and found_single == False:
                found_double = True
            elif c == "'" and found_double == False:
                found_single = True
 
            if found_double==True:
                if c == '"':
                    quote_count=quote_count+1
                    print(c, end="")
                elif c == "#" and (quote_count%2)==1:
                    print(c, end="")
                elif c == "#" and (quote_count%2)==0:
                    print('\n', end="")
                    break

            if found_single==True:
                if c == "'":
                    quote_count2=quote_count2+1
                    print(c, end="")
                elif c == "#" and (quote_count2%2)==1:
                    print(c, end="")
                elif c == "#" and (quote_count2%2)==0:
                    print('\n', end="")
                    break

            if c == "#" and found_single==False and found_double==False:
                print('\n', end="")
                break
            else:
                print(c, end="")
#kleisimo arxeiou                
f.close()
