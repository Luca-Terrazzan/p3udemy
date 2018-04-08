from test_module import main as asa
from test_module.test_module_subpackage import main

def echo():
    print("Located at modules root!")

asa.echo()
