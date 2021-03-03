# Basic Stuff:

1. Create prox_master obj
'import openport'
'prox = openport.prox_master()'
<\br>

2. **find()**
-find(index) 
-visit the web pages and scrape data 
-https://www.sslproxies.org   -> find(1) 
- https://free-proxy-list.net -> find(2)

'data = prox.find(2)'

-returned data is going to be is a json format
<br>

3. **save()**
-save(file_name,data)
-when you use save u dont have to care about repeated data

'prox.save("prox_test",data)'
<br>

4. **load_data()**
-load_data(file_name)
-if you have a excel file with data load will just load the file and return a json 

'data = prox.load_data("prox_test")'
<br>

5. **json formt**
'{
	"ip":xxx.xx.xx.x,
	"port":xx,
	"http":True,
	"https":True
}'
<br>

## Notes 
1. **setup_file()**
-setup_file(file_name) 
-it is going to setup a excel file
| ip       | port | http | https |
|----------|------|------|-------|
| xx.xx.xx | xxxx | True | False |

'prox.setup_file("file_name")'
<\br>

2. **save()**
-save(file_name,data)
-when you use this its  just going to save data and wont check repeated data

'prox.save("prox_test")'
<br>

