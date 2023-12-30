# pylint: disable=no-value-for-parameter

"""
Added for pylint
can go to .pylintrc to change stuff for linting
"""

import logging
import os
import sys
import psycopg2

try:
    user_name = os.environ['USER_NAME']
    password = os.environ['PASSWORD']
    rds_host = os.environ['RDS_HOST']
    rds_port = os.environ['RDS_PORT']
    db_name = os.environ['DB_NAME']

except psycopg2.Error as e:
    logging.Logger.error("ERROR: Unexpected error: Could not connect to Postgres instance.")
    logging.Logger.error(e)
    sys.exit()

def lambda_handler(event, context):
    """
    Added for pylint
    """
    print(event)
    print(context)
    conn = psycopg2.connect(host=rds_host, user=user_name, password=password, dbname=db_name, port=rds_port)
    with conn.cursor() as cur:
        cur.execute(
                """
                SELECT counter from counter
                ORDER BY id DESC
                LIMIT 1;
                """
            )
        data = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return data
