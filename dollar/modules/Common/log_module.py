import sqlite3
from persiantools.jdatetime import JalaliDateTime
import pytz


def log_user_event(user_id, user_first_name, user_full_name, event_name):
    with sqlite3.connect('/root/dollar/dollar_persistance/mydatabase.db') as conn:
        cur = conn.cursor()

        # Check if user already exists in the users table
        cur.execute('SELECT id FROM users WHERE id =' + str(user_id))
        existed_user = cur.fetchone()

        # Insert user if not exists in the users table
        if existed_user is None:
            cur.execute("INSERT INTO users (id, first_name, full_name) VALUES (?, ?, ?)",
                        (int(user_id), str(user_first_name), str(user_full_name)))

        # Insert user log
        cur.execute("INSERT INTO user_log (user_id, event_time, event_name) VALUES (?, ?, ?)",
                    (int(user_id), str(JalaliDateTime.now(pytz.utc)), str(event_name)))

        conn.commit()
    return ''