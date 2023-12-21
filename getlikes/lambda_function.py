import psycopg2
import logging
import sys
import os


try:    
    user_name = os.environ['USER_NAME']
    password = os.environ['PASSWORD']
    rds_host = os.environ['RDS_HOST']
    rds_port = os.environ['RDS_PORT']
    db_name = os.environ['DB_NAME']
    
    conn = psycopg2.connect(host=rds_host, user=user_name, password=password, dbname=db_name, port=rds_port)
except psycopg2.Error as e:
    logging.Logger.error("ERROR: Unexpected error: Could not connect to Postgres instance.")
    logging.Logger.error(e)
    sys.exit()
    
    
# logging.Logger.info("SUCCESS: Connection to the RDS Postgres instance succeeded")
    
# def lambda_handler(event, context):
#     with conn.cursor() as cur:
#         cur.execute(
#                 """
#                 SELECT counter from counter
#                 ORDER BY id DESC
#                 LIMIT 1;
#                 """
#             )
#         data = cur.fetchone()
#         # print(data)
        

        
#         conn.commit()
#         cur.close()
#         conn.close()
    
#         return data




def lambda_handler(event, context):
    with conn.cursor() as cur:
        cur.execute(
                """
                SELECT counter from counter
                ORDER BY id DESC
                LIMIT 1;
                """
            )
        data = cur.fetchone()
        # print(data)
        

        
        conn.commit()
        cur.close()
        conn.close()
    
        return data
    
        
        