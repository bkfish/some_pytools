#!/usr/bin/python3
import operator

string = input("Please input your string : ")
sort = []
result = {}
for i in string:
    if i not in sort:
        result.update({i:string.count(i)})
        sort.append(i)
sort_x = sorted(result.items(), key = lambda x: x[1], reverse=True)
for i in sort_x:
    print("{0} : {1:3}    ascii:{2:3}   pre char:{3}   next char:{4}".format(i[0],i[1], ord(i[0]), chr(ord(i[0]) - 1), chr(ord(i[0]) + 1)))
if string[-1] == string[-2]:
    baseStr = ""
    difference = ord("=") - ord(string[-1])
    for j in string :
        j = chr( ord(j) + difference )
        baseStr += j
    print("The string may be the base64:" + baseStr)