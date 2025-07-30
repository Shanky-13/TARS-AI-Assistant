import subprocess
import sqlite3
import re

def get_start_apps():
    try:
        # Run PowerShell command to get all start menu apps
        output = subprocess.check_output(
            ["powershell", "-Command", "Get-StartApps | Format-Table -AutoSize"],
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            shell=True
        )
        return output
    except subprocess.CalledProcessError as e:
        print(f"[PowerShell ERROR] {e.output}")
        return ""

def parse_apps(output):
    apps = []
    lines = output.strip().split('\n')

    # Skip headers (first 3 lines typically)
    for line in lines[3:]:
        parts = re.split(r'\s{2,}', line.strip())
        if len(parts) == 2:
            name, app_id = parts
            apps.append((name.strip().lower(), app_id.strip()))
    return apps

def insert_or_update_db(apps):
    conn = sqlite3.connect("TARS.db")
    cursor = conn.cursor()

    insert_count = 0
    update_count = 0

    for name, app_id in apps:
        try:
            cursor.execute("SELECT path FROM SYSTEM_COMMANDS WHERE name = ?", (name,))
            result = cursor.fetchone()

            if result is None:
                cursor.execute("INSERT INTO SYSTEM_COMMANDS (name, path) VALUES (?, ?)", (name, app_id))
                insert_count += 1
            elif result[0] != app_id:
                cursor.execute("UPDATE SYSTEM_COMMANDS SET path = ? WHERE name = ?", (app_id, name))
                update_count += 1
        except Exception as e:
            print(f"[DB ERROR] {e}")
    
    conn.commit()
    conn.close()
    print(f"Inserted {insert_count} new records.")
    print(f"Updated {update_count} existing records.")

# Run the process
output = get_start_apps()
apps = parse_apps(output)
insert_or_update_db(apps)
