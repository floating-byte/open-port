# Basic Stuff:

1. **Create prox_master obj**
<br>
<code>
	import openport
	prox = openport.prox_master()
</code>
<br>
2. **find()**
<br>
- find(index)
<br> 
- visit the web pages and scrape data 
<br>
- https://www.sslproxies.org   -> find(1) 
<br>
- https://free-proxy-list.net -> find(2)
<br>
<code>
	data = prox.find(2)
</code>
<br>
- returned data is going to be is a json format
<br>

3. **save()**
<br>
- save(file_name,data)
<br>
- when you use save u dont have to care about repeated data
<br>
<code>
	prox.save("prox_test",data)
</code>

<br>

4. **load_data()**
<br>
- load_data(file_name)
<br>
- if you have a excel file with data load will just load the file and return a json 

<code>
	data = prox.load_data("prox_test")
</code>
<br>

5. **json formt**
<code>
{
	"ip":xxx.xx.xx.x,
	"port":xx,
	"http":True,
	"https":True
}	
</code>
<br>

## Notes 
1. **setup_file()**
- setup_file(file_name) 
<br>
- it is going to setup a excel file
<br>
| ip       | port | http | https |
|----------|------|------|-------|
| xx.xx.xx | xxxx | True | False |
<br>
<code>
	prox.setup_file("file_name")
</code>
<br>
2. **save()**
<br>
- save(file_name,data)
<br>
- when you use this its  just going to save data and wont check repeated data
<code>
	prox.save("prox_test")
</code>

