from day14.reactions import NanoFactory

factory = NanoFactory(file_name='input.txt')
ore_required = factory.ore_to_produce_fuel(fuel=2)

print('1 FUEL required {} ORE'.format(ore_required))