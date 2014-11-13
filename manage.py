import pytest
from flask.ext.script import Manager, Shell, Server
from plant_api.app import create_app, mongo

app = create_app({'TESTING': True})

manager = Manager(app)

def _make_context():
    return {'app': app, 'db': mongo.db}

@manager.command
def test():
    import pytest
    exit_code = pytest.main(['tests/test_main.py', '--verbose'])
    return exit_code

manager.add_command('server', Server(host='0.0.0.0', port=5000))
manager.add_command('shell', Shell(make_context=_make_context))

if __name__ == '__main__':
    manager.run()