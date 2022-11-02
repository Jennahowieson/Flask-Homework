from models.order import *
from datetime import datetime



order1 = Order("Tony Stark", datetime.now().strftime('%d-%m-%Y'), 3, "Suit")
order2 = Order("Hulk", datetime.now().strftime('%d-%m-%Y'), 40, "XXXL Shirts")
order3 = Order("Captain Marvel", datetime.now().strftime('%d-%m-%Y'), 1, "Airplane")
order4 = Order("Captain America", datetime.now().strftime('%d-%m-%Y'), 1, "Sheild")
orders = [order1, order2, order3, order4]