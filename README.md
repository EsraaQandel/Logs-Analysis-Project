# Log-Analysis

### Project Overview
>In this project, you'll work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.

### How to Run?

#### PreRequisites:
  * [Python3](https://www.python.org/)
  * [Vagrant](https://www.vagrantup.com/)
  * [VirtualBox](https://www.virtualbox.org/)

#### Setup Project:
  1. Install Vagrant and VirtualBox
  2. Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
  3. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from here.
  4. Unzip this file after downloading it. The file inside is called newsdata.sql.
  5. Copy the newsdata.sql file and content of this current repository, by either downloading or cloning it from
  [Here](https://github.com/sagarchoudhary96/Log-Analysis)
  
#### Launching the Virtual Machine:
  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
  
  ```
    $ vagrant up
  ```
  2. Then Log into this using command:
  
  ```
    $ vagrant ssh
  ```
 
  
#### Setting up the database and Creating Views:

  1. Load the data in local database using the command:
  
  ```
    psql -d news -f newsdata.sql
  ```
  The database includes three tables:
  * The authors table includes information about the authors of articles.
  * The articles table includes the articles themselves.
  * The log table includes one entry for each time a user has accessed the site.
  
  2. Use `psql -d news` to connect to database.
  
  3. Create view articles_view using:
  ```
    create view articles_view as select title,author,count(*) as views from articles,
    log where log.path like concat('%',articles.slug,'%') and log.status like '%200%'
    group by articles.title,articles.author order by views DESC;
  ```
  
  4. Create vier error_lead_view using:
  ```
    create view error_lead_view as select date(time) ,count(*) as total,
    sum(case log.status when '200 OK' then 0 else 1 end) as error from log
    group by date(time) order by error DESC;
  ```

#### Run the reporting tool:
  1. From the vagrant directory inside the virtual machine,run logs.py using:
  ```
    $ python3 reporting_tool.py
  ```
  