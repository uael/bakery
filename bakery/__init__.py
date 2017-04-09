from bakery.impl import *
from pulp import *


def script_main():
  bakery = Bakery(
    {
      'farine': {'stock': 250, 'cost': 0.5},
      'sel': {'stock': 10, 'cost': 0.5},
      'beurre': {'stock': 20, 'cost': 7},
      'leuvure': {'stock': 1, 'cost': 50},
      'sucre': {'stock': 50, 'cost': 1},
      'oeuf': {'stock': 5, 'cost': 3},
      'chocolat': {'stock': 20, 'cost': 10}
    },
    {
      'pain': {
        'time': 0.02, 'price': 3.6, 'ingredients': {
          'farine': 0.991, 'sel': 0.01, 'beurre': 0, 'leuvure': 0.008, 'sucre': 0, 'oeuf': 0, 'chocolat': 0
        }
      },
      'croissant': {
        'time': 0.1, 'price': 12.5, 'ingredients': {
          'farine': 0.6, 'sel': 0.01, 'beurre': 0.3, 'leuvure': 0.015, 'sucre': 0.05, 'oeuf': 0.03, 'chocolat': 0
        }
      },
      'pain au chocolat': {
        'time': 0.11, 'price': 13, 'ingredients': {
          'farine': 0.55, 'sel': 0.01, 'beurre': 0.2, 'leuvure': 0.015, 'sucre': 0.05, 'oeuf': 0.03, 'chocolat': 0.05
        }
      },
      'gateau': {
        'time': 0.01, 'price': 16, 'ingredients': {
          'farine': 0.15, 'sel': 0, 'beurre': 0.3, 'leuvure': 0, 'sucre': 0.6, 'oeuf': 0.1, 'chocolat': 1.2
        }
      }
    }
  )
  bakery.prepare(4)

if __name__ == '__main__':
  sys.exit(script_main())
