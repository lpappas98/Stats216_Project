from datetime import datetime


file = open("comments.csv","r",encoding = "utf-8")

outFile = open("tableu_file.csv","w",encoding = "utf-8")


outFile.write("subreddit,date,comment_score,toxic,toxic_level,sport_or_esport" + "\n")


sports = ["nfl","baseball","soccer","nba","hockey"]
esports = ["leagueoflegends","Rainbow6","GlobalOffensive","DotA2","Competitiveoverwatch"]

file.readline()

for each_line in file:
    line_list = each_line.split(",")

    subreddit = line_list[0]
    unix = float(line_list[1])
    score = line_list[2]
    
    
    try:
        value = float(line_list[4].strip())
    except ValueError:

        try:
            value = int(line_list[4].strip())
        except:
            pass
    
    if value > 0:
        toxic = "yes"
    else:
        toxic = "no"


    if line_list[0] in sports:
        option = "sport"
    elif line_list[0] in esports:
        option = "esports"
    else:
        option = "???"

        
    toxic_level = line_list[4].strip()

    utc_time = datetime.utcfromtimestamp(unix)
    newDate = (utc_time.strftime("%Y-%m-%d %H:%M:%S.%f"))    
    
    outFile.write(subreddit + "," + \
                  str(newDate) + "," + \
                  str(score) + "," + \
                  str(toxic) + "," + \
                  str(toxic_level) + "," + \
                  str(option) + "\n")


outFile.close()
file.close()


