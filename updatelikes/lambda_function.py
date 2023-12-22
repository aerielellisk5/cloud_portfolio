import psycopg2
import logging
import sys
import os
import json


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
    try: 
        conn = psycopg2.connect(host=rds_host, user=user_name, password=password, dbname=db_name, port=rds_port)
        with conn.cursor() as cur:
            # grabbing value from database
            cur.execute(
                """
                SELECT counter from counter
                WHERE id = 1
                """
            )
            data = cur.fetchone()
            count = data[0] + 1

            update_query = "UPDATE counter SET counter = %s WHERE id = 1;"

            cur.execute(update_query, [count])

            conn.commit()
            cur.close()
            conn.close()
            
            # return count
        
            response = {
                "statusCode": 200,  # HTTP status code indicating success (e.g., 200 for OK)
                "body": count,
                "headers": {
                    "content-type": "application/json"
                }
                
            }
            
            return response
            
            
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
        
        
