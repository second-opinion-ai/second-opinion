from flask import g

def some_function():
    if hasattr(g, 'make'):
        make = g.make
        model = g.model
        year = g.year
        car_issue = g.car_issue
    retrn [make, model, year, car_issue]