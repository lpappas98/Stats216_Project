

#analyze the data

comments = {}
toxicComments = {}

file = open("tableu_file.csv","r",encoding = "utf-8")
file.readline()
name = []


sports = ["nfl","baseball","soccer","nba","hockey"]
esports = ["leagueoflegends","Rainbow6","GlobalOffensive","DotA2","Competitiveoverwatch"]

sportsCom = 0
esportsCom = 0
sportsTox = 0
esportsTox = 0


for eachline in file:
    linelist = eachline.split(",")

    if linelist[0] not in comments:

        if linelist[3] == 'yes':
            comments[linelist[0]] = 1
            toxicComments[linelist[0]] = 1
        else:
            comments[linelist[0]] = 1
            toxicComments[linelist[0]] = 0
    else:

        if linelist[3] == 'yes':
            comments[linelist[0]] += 1
            toxicComments[linelist[0]] += 1
            
        elif linelist[3] == 'no':
            comments[linelist[0]] += 1

    if linelist[0] not in name:
        name.append(linelist[0])


    if linelist[0] in sports:
        sportsCom += 1

        if linelist[3] == 'yes':
            sportsTox += 1

    if linelist[0] in esports:
        esportsCom += 1

        if linelist[3] == 'yes':
            esportsTox += 1
        
    



        
outfile = open("results.txt","w",encoding = "utf-8")

outfile.write("Reddit Toxicity results" + "\n")
outfile.write("Created by Reese Pearsall and Logan Pappas" + "\n")
outfile.write("" + "\n")

for eachName in name:
    if eachName != ' ':
        numCom = comments[eachName]
        numTox = toxicComments[eachName]
        proportion = toxicComments[eachName] / comments[eachName]


        print("Subreddit name:",eachName)
        print("# of comments:",numCom)
        print("# of toxic comments:",numTox)
        print("Proportion:",proportion,"or",str(proportion*100)+"%")
        print("------------------------------")


        


    
        outfile.write("Subreddit name: " + eachName + "\n")
        outfile.write("# of comments: " + str(numCom) + "\n")
        outfile.write("# of toxic comments: " + str(numTox) + "\n")
        outfile.write("Proportion: " + str(proportion) + " or " + str(proportion*100)+"%" + "\n")
        outfile.write("------------------------------" +"\n")


sportsPro = sportsTox / sportsCom
esportsPro = esportsTox/ esportsCom

print("Sports")
print("# of comments:",sportsCom)
print("# of toxic comments:",sportsTox)
print("Proportion:",sportsPro,"or",str(sportsPro*100)+"%")
print("------------------------------")

print("Esports")
print("# of comments:",esportsCom)
print("# of toxic comments:",esportsTox)
print("Proportion:",esportsPro,"or",str(esportsPro*100)+"%")
print("------------------------------")


outfile.write("Sports pooled" + "\n")
outfile.write("# of comments: " + str(sportsCom) + "\n")
outfile.write("# of toxic comments: " + str(sportsTox) + "\n")
outfile.write("Proportion: " + str(sportsPro) + " or " + str(sportsPro*100)+"%" + "\n")
outfile.write("------------------------------" +"\n")

outfile.write("Esports pooled" + "\n")
outfile.write("# of comments: " + str(esportsCom) + "\n")
outfile.write("# of toxic comments: " + str(esportsTox) + "\n")
outfile.write("Proportion: " + str(esportsPro) + " or " + str(esportsPro*100)+"%" + "\n")
outfile.write("------------------------------" +"\n")












outfile.close()
