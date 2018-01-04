from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_script import Manager, Server

from testflask import db, User, app

manager = Manager(app=app)
bootstrap = Bootstrap(app=app)
moment = Moment(app=app)

manager.add_command("server", Server())


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User)


if __name__ == '__main__':
    manager.run()
