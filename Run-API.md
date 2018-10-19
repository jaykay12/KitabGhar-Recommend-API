**Step 1:** Prior Running this API, Build the Project [KitabGhar](https://github.com/jaykay12/KitabGhar)

> (*If Step 1 is Skipped (Not Recommended)*)

> **Step 1.1:**  Create a DB in MySQL named *kitabghar* 

> **Step 1.2:**  Populate the DB Schema into the *kitabghar* using
> ```bash
> mysql -u <MYSQL_USERNAME> -p kitabghar < KitabGhar.sql
> ```

**Step 2:** Create Virtual Environment using `virtualenv venv`

**Step 3:** Activate the Virtual Environment using `source venv/bin/activate`

**Step 4:** Install the dependencies using `pip install -r requirements.txt`

**Step 5:** Create a file `development.env` for environment variables(mainly Database Connections):
```bash
export LOCALHOST="localhost"
export USERNAME="<MYSQL_USERNAME>"
export PASSWORD="<MYSQL_PASSWORD>"
export DATABASE="kitabghar"
```

**Step 6:** Set the environment variables using `source ./development.env`

**Step 7:** Check if API Service is running normally using `pytest` and check if all 3 test passes.

**Step 8:** Run the API Service using `cd api` and `python3 app.py`
