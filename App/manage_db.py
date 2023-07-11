from flask import Manager, Migrate, MigrateCommand
from App import create_app, db

app = create_app()  
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()