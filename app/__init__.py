import db
from db_models import *
def run():
    pass
if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    run()