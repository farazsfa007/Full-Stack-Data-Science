import os , sys
from os.path import dirname , join , abspath

sys.path.insert(0,abspath(join(dirname(__file__),'..')))

from payment import payment_details

def course():
    print("This is course details")

payment_details.payment()