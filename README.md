# Recommender-System
This repo holds the source code of the Recommender, I coded for my project: KitabGhar


### Steps to have `ratings.csv` from Database

Step 1: Added R/W Permissions to Base Folder using `chmod 777 -R Recommender-System/`

Step 2: Modified `/etc/mysql/my.cnf` by adding 
> [mysqld]
> `secure-file-priv=""`

Step 3: Open MySQL Client using `mysql -u root -p`

Step 4: Selecting Database using `use kitabghar;`

Step 5: Generating .CSV file using `SELECT reviewid,bookid,userid,ratings INTO OUTFILE 'ratings.csv' FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n' FROM reviews;`

Step 6: `sudo su`

Step 7: `cd var/lib/mysql/kitabghar`

Step 8: `cp ratings.csv /home/jaykay12/Documents/Github/Recommender-System`