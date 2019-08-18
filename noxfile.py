import nox


@nox.session(reuse_venv=True)
def run(session):
    session.install('-r', 'requirements.txt', env={'FLASK_APP': 'app.py'})
    session.run('flask', 'run')
