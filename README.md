# Flask &harr; MySQL Connection



## Some info

Just as we used *Phpmyadmin* for our past projects, we're gonna do the same here.

The important thing to remember when  discussing connecting our flask app to the MySQL database is that flask isn't really doing anything special here.  Just like we used php to connect to the database in the previous modules, we're using python.

I wrote a python file that should make things easier. This will be explained later.


## Installation of mysql flask module
1. ssh into your instance and cd into your project directory
2. run `sudo yum install mariadb-devel`
3. run `sudo yum install python3-devel`
4. run `pip3 install flask_mysqldb`

## Then, see the example for use