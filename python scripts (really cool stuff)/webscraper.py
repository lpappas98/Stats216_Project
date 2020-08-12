import praw


reddit = praw.Reddit(client_id = '1QXvLj7o-Jp94g',
                     client_secret = 'pqM88B6b6Eabk3diA7JUfMSIFWk',
                     username = 'ReeseLoganStat216',
                     password = 'seanyawrocks',
                     user_agent = 'stat216')


#output_file = open("output.csv","w")




subreddit = reddit.subreddit('politics')




def calculateToxicity(comment):
    toxicWords = open("toxic.txt","r")
    toxicList = []
    toxicity += 1
    for eachLine in toxicWords:
        toxicList.append(eachLine.strip())

    commentAsList = comment.body.split(" ")
    
    for eachWord in commentAsList:
        if eachWord in toxicList:
            toxicity += 1

    commentScore = comment.score

    return toxicity


hot_page = subreddit.hot(limit = 50)
total_count = 0
count = 0
with open("output.csv","w",encoding = "utf-8") as file:
    file.write("Subreddit,Date,Comment Score,Comment,Toxicity Level" + "\n")
    for each_thread in hot_page:
        #if not each_thread.stickied:

        count = 0
        print(each_thread.title)


        print("Expected :",each_thread.num_comments)
        
        each_thread.comments.replace_more(limit=0)
    
        for each_comment in each_thread.comments.list():

            toxicity = calculateToxicity(each_comment)
            
            #if each_comment.score <= 0:  
            file.write(str(each_comment.subreddit) + "," + \
                           str(each_comment.created_utc) + "," + \
                           str(each_comment.score)+ "," + \
                           each_comment.body.replace(",","").replace("\n"," ") + \
                           str(toxicity) + "\n")
            count += 1
            
            #for each_reply in each_comment.replies.list():
                
                #file.write(str(each_reply.score) + ">" + each_reply.body.replace(",","").replace("\n"," ") + "\n")
                #count += 1
            
                #for another_reply in each_reply.replies.list():
                    #file.write(">>" + another_reply.body.replace(",","").replace("\n"," ") + "\n")
                    #count += 1
            
        
        file.write("NEW THREAD" + "\n")
        print("Got:",count)
        total_count += count
        if total_count > 10000:
            break
        
        

print(total_count)
