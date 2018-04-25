start_time=6*3600+52*60
easy_pace=8*60+15
tempo=7*60+12
end_time=start_time+2*easy_pace+3*tempo
print(end_time)
hrs=end_time//3600        #Calculating hrs as an integer
mins=(end_time%3600)//60  #Calculating hrs fraction in mins
secs=(end_time%3600)%60   #Calculating mins fraction in secs
print("Reach time in hrs:mins:secs ",hrs," : ",mins," : ",secs)