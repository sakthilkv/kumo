import sqlite3

conn = sqlite3.connect('kumo.db')
cursor = conn.cursor()

class User:
    def __init__(self):
        pass

    def create_user(self, user_data):
        try:
            cursor.execute('''
                INSERT INTO users (uid, username, name, pfp_url, email, bio, dob, waifu, join_date, location, account_status, social_links)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', user_data)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error inserting users into the users table: {e}")

    def edit_user(self, uid, new_user_data):
        try:
            cursor.execute('''
                UPDATE users
                SET username = ?, name = ?, pfp_url = ?, email = ?, bio = ?, dob = ?, waifu = ?, join_date = ?, location = ?, account_status = ?, social_links = ?
                WHERE uid = ?
            ''', (
                new_user_data['username'], new_user_data['name'], new_user_data['pfp_url'],
                new_user_data['email'], new_user_data['bio'], new_user_data['dob'],
                new_user_data['waifu'], new_user_data['join_date'], new_user_data['location'],
                new_user_data['account_status'], new_user_data['social_links'], uid
            ))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error updating user in the users table: {e}")

if __name__ == "__main__":
    user = User()

    # Example usage for creating a user


    # Example usage for editing a user
    new_user_data = {
        'username': 'satoru',
        'name': 'New Name',
        'pfp_url': 'https://example.com/new_profile.jpg',
        'email': 'new.email@example.com',
        'bio': 'Updated bio',
        'dob': '1990-01-01',
        'waifu': 'New Waifu',
        'join_date': '2024-06-25',
        'location': 'New Location',
        'account_status': 'active',
        'social_links': '{"twitter": "https://twitter.com/new_profile"}'
    }
    user.edit_user('7KwpHkNlGQYeXGUJbVhMpXWAiL22', new_user_data)
