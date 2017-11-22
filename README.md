# Log-Analysis Project

## Introduction 

In this project you will build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.
You will get practice interacting with a live database both from the command line and from your code.

> You will be working with a database that includes three tables:
> * The authors table includes information about the authors of articles.
> * The articles table includes the articles themselves.
> * The log table includes one entry for each time a user has accessed the site.


## How to Run?

### PreRequisites:
  1. [Python3](https://www.python.org/) 
  2. [VirtualBox](https://www.virtualbox.org/)
  3. [Vagrant](https://www.vagrantup.com/)
   

### Setup Project:
  1. Install Vagrant and VirtualBox
  2. Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
  3. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from here.
  4. Copy the newsdata.sql file -from the zip file you just downloaded - and content of this current repository

### Launching the Virtual Machine:
  1. Navigate to the sub directory in the downloaded folder -fullstack-nanodegree-vm- to install all the dependencies by running:
  
  ```
    $ vagrant up
  ```
  2. Then Log into this using command:
  
  ```
    $ vagrant ssh
  ```
 
  
### loading the data and Creating Views:

  1. Load the data in local database using the command:
  
  ```
    psql -d news -f newsdata.sql
  ```
 
  
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

### Run the reporting tool:

  ```
    $ python3 reporting_tool.py
  ```
  