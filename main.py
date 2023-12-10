import inspect
from animal_types import *


def print_info(instance, *methods):
    if not isinstance(instance, animal.Animal):
        raise TypeError(f'passed object is not an animal')
    print('-----------------')
    print(f'this is {instance.name}')
    print(f'he is {instance.kind}')
    if not methods:
        print("he can't do anything")
        return
    for method in methods:
        foo = getattr(instance, method)
        if len(inspect.signature(foo).parameters) == 0:
            foo()
        else:
            raise ValueError(f'the method {method} passed has more that one argument')

if __name__ == '__main__':

    pinguin1 = Pinguin('Bobby')
    eagle1 = Eagle('Johny')
    tuna1 = Tuna('Henry')
    flying_fish1 = Flying_Fish('Fishey') #shat ankap en anunnery ))))
    
    print_info( pinguin1, 'walk', 'eat', 'swim')
    print_info(eagle1, 'walk', 'eat', 'fly')
    print_info(tuna1, 'eat', 'swim')
    print_info(flying_fish1, 'swim', 'eat', 'fly')



