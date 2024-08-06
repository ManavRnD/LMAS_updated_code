from datetime import datetime,timedelta
import mysql.connector

current_datetime = datetime.now()
# Format the datetime as a string in the MySQL DATETIME format
formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
interval_time = current_datetime - timedelta(minutes=5)
print(interval_time)


print("Current date and time in MySQL DATETIME format:", formatted_datetime)


def insert_datetime_to_db(formatted_datetime):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="Mepl",
            password="Mepl@123",
            database="manav_admin"
        )
        cursor = connection.cursor()

        # Example query to insert the datetime value into a table
        query = ("INSERT INTO lmas_data (Name,plant_name,DS,`AS`,WEATHER,Hoot,macid,date_time) VALUES (%s, %s, %s,%s,%s,"
                 "%s,%s,%s)")
        params = ('Test1', 'Test', 0, 1, 0, 0, '1234', formatted_datetime)  # Replace with your actual values
        cursor.execute(query, params)
        connection.commit()

        print("Datetime inserted successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


# Call the function to insert the datetime
insert_datetime_to_db(formatted_datetime)
