#Question 1 Task 1: Add a Member 
import sqlite3
def add_member(id, name, age):
    conn = sqlite3.connect('gym_db')
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO Members (id, name, age)
            VALUES (?,?,?)
        ''',(id, name, age))
        conn.commit()
        print("Members added sucessfully.")
    except sqlite3.IntegrityError as e:
        if 'UNIQUE constriant failed' in str(e):
            print(f"Error: A member with ID {id}already exists.")
        else:
            print(f"Integrity Error: {e}")

    except Exception as e:
        print(f"An error occured: {e}")
    finally:
        conn.close()

# Example Useage
add_member(1, 'Alice Jhon', 23)

#Question 1 Task 2: Add a Workout Session
def add_workout_session(member_id, date, duration_minutes, calories_burned):
    conn = sqlite3.connect('gym_db')
    cursor = conn.cursor()
    try:
       conn = sqlite3.connect('gym_db')
       cursor = conn.cursor()
    
       query = """ 
       INSERT INTO Workoutsessions (member_id, date, duration_minutes, calories_burnned)
       VALUES (?,?,?)
       """

       cursor.execute(query, (member_id, date, duration_minutes, calories_burned))
       conn.commit()

       print("Workout session added sucessfully.")
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()
# Example Useage
add_workout_session(1, '2024-3-5', 34, 787)

#Question 1 Task 3: Updating Member Information
def update_member_age(member_id, new_age):
    conn = sqlite3.connect('gym_db')
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT COUNT(*) FROM members WHERE id = ?", (member_id,))
        count = cursor.fetchone()[0]

        if count == 0:
            print(f"Member with ID {member_id} does not exist")
            return
        
        cursor.execute("UPDATE members SET age = ?", (new_age, member_id))
        conn.commit()
        print(f"Member with ID {member_id} has been updated to age {new_age}.")
    except sqlite3.Error as e:
        print(f"An error occured: {e}")
    finally:
        conn.close()
    
# Example Useage
update_member_age(1,32)

#Question 1 Task 3: Delete a Workout Session
def delete_workout_session(session_id):
    conn = sqlite3.connect('gym_db')
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM workout_sessions WHERE session_id = ?", (session_id,))
        session = cursor.fetchone()
        if session is None:
            raise ValueError(f"Session ID {session_id} does not exist.")
        cursor.execute("DELETE FROM workout_sessions WHERE session_id =?", (session_id,))
        conn.commit()
        print(f"Sessions ID {session_id} has been sucessfully deleted.")
    except sqlite3.Error as e:
        print(f"An error occured: {e}")
    except ValueError as ve
        print(ve)
    finally:
        conn.close()

# Example Useage
delete_workout_session(1)

#Question 2 Task 1: SQL BETWEEN Usage
import sqlite3
def get_members_in_age_range(start_age, end_age):
    conn = sqlite3.connect('gym_db')
    cursor = conn.cursor()
    
    query = """
    SELECT * FROM Members
    WHERE age BETWEEN ? AND ?
    """
    cursor.execute(query, (start_age, end_age ))
    results = cursor.fetchall()
    conn.close()
    return results

# Example Useage
members_in_age_range = get_members_in_age_range(32,42)
for member in members_in_age_range:
    print(member)








