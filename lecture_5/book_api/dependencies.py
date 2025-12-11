from database import SessionLocal

# Dependency: create DB session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
