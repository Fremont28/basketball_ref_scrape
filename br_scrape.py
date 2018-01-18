#scraping basketball reference (2017 NBA draft statistics)
base_urlx1="https://www.basketball-reference.com/draft/NBA_2017.html"
request_x=requests.get(base_urlx1)
table_x=BeautifulSoup(request_x.text).find('table')
table_x1=table_x.find_all('thead')
for t in table_x1:
    print(t.get_text()) #prints out column headers 

#grab player stats
table_stats=BeautifulSoup(request_x.text).find('tbody')
#get player names, team, and school
table_stats1=table_stats.find_all('td',class_=re.compile('left'))
w1=[]
for w in table_stats1:
    print(w.get_text())
    w1.append(w.get_text())
#get player stats
table_stats2=table_stats.find_all('td',class_=re.compile('right'))
w2=[]
for w in table_stats2:
    print(w.get_text())
    w2.append(w.get_text())

#size of the list(60,18)
len(w2)       
x=np.reshape(w2,(60,18)) 
type(x)
#w1 list(60,3)
len(w1)
x1=np.reshape(w1,(60,3))
#combine arrays (player, college, nba team and NBA statistics)
final_array=np.concatenate((x1,x),axis=1)