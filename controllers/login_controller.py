from models.database_setup import create_session, User
import bcrypt

def authenticate(username, password):
    session = create_session()
    # Fetch user from the DB based on username
    user = session.query(User).filter_by(username=username).first()
    
    # Verify if the user exists and if the password is correct
    if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        return True
    else:
        return False