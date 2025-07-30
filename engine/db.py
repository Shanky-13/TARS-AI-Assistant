import csv
import sqlite3

con = sqlite3.connect("TARS.db")
cursor = con.cursor()

# cursor.execute("UPDATE SYSTEM_COMMANDS SET path = 'C:\\Users\\supriya\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe' WHERE name = 'zoom'")
# con.commit()


query = "CREATE TABLE IF NOT EXISTS WEB_COMMANDS(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'youtube', 'https://www.youtube.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'google', 'https://www.google.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'gmail', 'https://mail.google.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'facebook', 'https://www.facebook.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'instagram', 'https://www.instagram.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'whatsapp web', 'https://web.whatsapp.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'amazon', 'https://www.amazon.in/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'flipkart', 'https://www.flipkart.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'stackoverflow', 'https://stackoverflow.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'github', 'https://github.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'linkedin', 'https://www.linkedin.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'twitter', 'https://twitter.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'netflix', 'https://www.netflix.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'chatgpt', 'https://chat.openai.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'canva', 'https://www.canva.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'wikipedia', 'https://www.wikipedia.org/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'notion', 'https://www.notion.so/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'zoom', 'https://zoom.us/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'google drive', 'https://drive.google.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'google docs', 'https://docs.google.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'google meet', 'https://meet.google.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'one drive', 'https://onedrive.live.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'dropbox', 'https://www.dropbox.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'trello', 'https://trello.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'figma', 'https://www.figma.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'replit', 'https://replit.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'geeksforgeeks', 'https://www.geeksforgeeks.org/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'w3schools', 'https://www.w3schools.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'khan academy', 'https://www.khanacademy.org/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'coursera', 'https://www.coursera.org/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'udemy', 'https://www.udemy.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'edx', 'https://www.edx.org/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'openai', 'https://platform.openai.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'hugging face', 'https://huggingface.co/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'kaggle', 'https://www.kaggle.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'colab', 'https://colab.research.google.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'aws console', 'https://console.aws.amazon.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'azure portal', 'https://portal.azure.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'vercel', 'https://vercel.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'render', 'https://render.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'cloudflare', 'https://www.cloudflare.com/')"
# cursor.execute(query)

# query = "INSERT INTO WEB_COMMANDS VALUES (null,'figma community', 'https://www.figma.com/community')"
# cursor.execute(query)

# con.commit()


# testing module
# app_name = "android studio"
# cursor.execute('SELECT path FROM SYSTEM_COMMANDS WHERE name IN (?)', (app_name,))
# results = cursor.fetchall()
# print(results[0][0])

# Create a table with the desired columns
cursor.execute('''CREATE TABLE IF NOT EXISTS CONTACTS (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')


# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
# desired_columns_indices = [0, 20]

# # # Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     next(csvreader)  # Skip the header row
#     for row in csvreader:
#         if len(row) > max(desired_columns_indices):  # Avoid index errors
#             selected_data = [row[i] for i in desired_columns_indices]
#             cursor.execute('''INSERT INTO CONTACTS (id, name, mobile_no) VALUES (null, ?, ?);''', tuple(selected_data))

# # Commit changes and close connection
# con.commit()
# con.close()

# query = "INSERT INTO CONTACTS VALUES (null,'raghav', '1234567890', 'null')"
# cursor.execute(query)
# con.commit()

# query = 'S '
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM CONTACTS WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])
