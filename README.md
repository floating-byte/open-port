# Basic Stuff:
0. **requirement**
	<br>
	<code>
		pip install -r requirements.txt
	</code>
1. **prox_master()**
	* import openport and create obj 
	<code>
		import openport
	</code>
	<br>
	<code>
		prox = openport.prox_master()
	</code>


2. **find()**
	<br>
	<code>
		data = prox.find(2)
	</code>
	* find(index)
	* visit the web pages and scrape data 
	* https://www.sslproxies.org   -> find(1) 
	* https://free-proxy-list.net  -> find(2)


	* returned data is going to be is a json format

3. **save()**
	<br>
	<code>
		prox.save("prox_test",data)
	</code>
	* save(file_name,data)
	* when you use save u dont have to care about repeated data



4. **load_data()**
	<br>
	<code>
		data = prox.load_data("prox_test")
	</code>
	* load_data(file_name)
	* if you have a excel file with data load will just load the file and return a json 



5. **json**
	```json
	{
	  "ip": "123.123.21.2",
	  "port": 80,
	  "http": "False",
	  "https": "True",
	}
	```

## Notes 
1. **setup_file()**
	<br>
	<code>
		prox.setup_file("file_name")
	</code>
	* setup_file(file_name) 
	* its going to setup a excel file
2. **save()**
	<br>
	<code>
		prox.save("prox_test")
	</code>
	* save(file_name,data)
	* its going to save data and wont check repeated proxies


