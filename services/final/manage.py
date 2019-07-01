# services/users/manage.py

import unittest

import coverage # new

COV = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'project/tests/*',
        'project/config.py',
    ]
)
COV.start()


from flask.cli import FlaskGroup

from project import create_app, db # new
from project.api.models import P01, P02, T01, S01 # new

app = create_app() # new
cli = FlaskGroup(create_app=create_app) # new

@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command()
def test():
    """Ejecutar los tests sin covertura de codigo"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

# nueva era
@cli.command('seed_db')
def seed_db():
    """Sembrado en la base de datos"""
    db.session.add(P01(name='Guantes', stock=12, price=20))
    db.session.add(P01(name='Mouse Gamer', stock=25, price=50))
    db.session.add(P01(name='Router', stock=9, price=100))
    db.session.add(P02(name='Deltron', address='Lobaton 1020', ruc=83753689))
    db.session.add(P02(name='Savando in todias', address='Aprovemi 127', ruc=45673308))
    db.session.add(P02(name='Impacto', address='Alameda 301', ruc=23658938))
    db.session.add(T01(name='Daniel', position= 'Vendedor'))
    db.session.add(T01(name='Leandro', position= 'Contador'))
    db.session.add(T01(name='Cetaceo', position= 'servicio tecnico'))
    db.session.add(S01(country='Peru', city= 'Arequipa', floor=1))
    db.session.add(S01(country='Bolivia', city= 'La Paz', floor=1))
    db.session.add(S01(country='Peru', city= 'Lima', floor=2))
    db.session.commit()

# nuevo -> de covertura
@cli.command()
def cov():
    """Ejecuta las pruebas unitarias con coverage"""
    tests   = unittest.TestLoader().discover('project/tests')
    result  = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Resumen de cobertura')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    sys.exit(result)


if __name__ == '__main__':
    cli()
