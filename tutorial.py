import openport

''' u create a obj like that '''
prox = openport.prox_master()

'''setup_file() just going to create empty file'''
''' u dont need to use it '''
prox.setup_file("data_test")

''' there is 2 web pages i can scrape for data '''
''' https://www.sslproxies.org  -> find(1) '''
''' https://free-proxy-list.net -> find(2) '''

''' find() going to visit the web pages '''
data = prox.find(2)
'''
return a json like 
{
	"ip":xxx.xx.xx.x,
	"port":xx,
	"http":True,
	"https":True
}
'''

''' save() just take the data and save it in a xlsx file'''
''' save() wont save the same proxy so your data is not repeated'''
prox.save("data_test",data)

'''if u dont care about repeated data well use '''
#prox.save_data("data_test",data)

''' so u can load it using load_data() '''
print(prox.load_data("data_test"))
'''
return a json like 
{
	"ip":xxx.xx.xx.x,
	"port":xx,
	"http":True,
	"https":True
}
'''