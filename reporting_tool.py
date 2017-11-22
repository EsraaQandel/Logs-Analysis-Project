#! /usr/bin/env python3

import psycopg2
DB_NAME = "news"

# 1. What are the most popular three articles of all time?
title1 = "\n The 3 most popular articles of all time are:\n"

query1 = "select title,views from articles_view limit 3"

# 2. Who are the most popular article authors of all time?
title2 = "\n The most popular article authors of all time are:\n"

query2 = """select authors.name,sum(articles_view.views) as views from
articles_view,authors where authors.id = articles_view.author
group by authors.name order by views desc"""

# 3. On which days did more than 1% of requests lead to errors?
title3 = "\n Days with more than 1% of request that lead to an error:\n "

query3 = """select date, round (CAST((error/total::float)*100 AS numeric) ,2) as percent
from error_lead_view where (error/total::float)*100 > 1"""

# to store results
result_1 = dict()
result_2 = dict()
result_3 = dict()

# returns query result

def get_result(query):
    """Connect to the PostgreSQL database"""
    try:
        db = psycopg2.connect(database=DB_NAME)
        c = db.cursor()
        c.execute(query)
        results = c.fetchall()
        db.close()
        return results
    except:
        print("Couldn't connect to database")


def print_results(title, query_result):
    print (title)
    for result in query_result['results']:
        print ('\t' + str(result[0]) + ' --->>> ' + str(result[1]) + ' views')


def print_error_percentage(title, query_result):
    print (title)
    for result in query_result['results']:
        print ('\t' + str(result[0]) + ' --->>> ' + str(result[1]) + ' %')

if __name__ == '__main__':
    # stores query result
    result_1['results'] = get_result(query1)
    result_2['results'] = get_result(query2)
    result_3['results'] = get_result(query3)

    # print formatted output
    print_results(title1, result_1)
    print_results(title2, result_2)
    print_error_percentage(title3, result_3)
