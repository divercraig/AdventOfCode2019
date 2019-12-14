import math


class Chemical:
    def __init__(self, name:str, quantity:int):
        self.name = name
        self.quantity = quantity

    def __eq__(self, other):
        return self.name == other.name and self.quantity == other.quantity

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return '{} {}'.format(self.quantity, self.name)

    def __add__(self, other):
        if other.name != self.name:
            raise ValueError("CANNOT ADD TWO DIFFERENT CHEMICALS")
        else:
            return Chemical(name=self.name, quantity=self.quantity + other.quantity)

    @classmethod
    def from_string(cls, chemical:str):
        quantity, name = chemical.strip().split(' ')
        return cls(name=name, quantity=int(quantity))


class Reaction:

    def __init__(self, formula:str):
        self.inputs = []
        input, output = formula.split('=>', maxsplit=1)
        self.product = Chemical.from_string(output)

        for string in input.strip().split(','):
            chemical = Chemical.from_string(string)
            self.inputs.append(chemical)

    def __repr__(self):
        return '{} -> {}'.format(self.inputs, self.product)


class NanoFactory:
    def __init__(self, file_name:str):
        self.reactions = {}

        for formula in open(file_name):
            reaction = Reaction(formula)
            self.reactions[reaction.product.name] = reaction

    def breakdown(self, chemical):
        required_chemicals = []
        if chemical.name == 'ORE' or chemical.quantity < 0:
            required_chemicals.append(chemical)
            return required_chemicals

        reaction = self.reactions[chemical.name]

        multiplier = math.ceil(chemical.quantity/reaction.product.quantity)
        waste_amount = (reaction.product.quantity * multiplier) - chemical.quantity
        if (waste_amount != 0):
            required_chemicals.append(Chemical(name=chemical.name, quantity=waste_amount * -1))

        for input in reaction.inputs:
            chemical = Chemical(name=input.name, quantity=input.quantity * multiplier)
            required_chemicals.append(chemical)

        return required_chemicals

    def breakdown_group(self, chemicals):
        chemicals_to_reduce = []
        for to_breakdown in chemicals:
            chemicals_to_reduce.extend(self.breakdown(to_breakdown))
        return chemicals_to_reduce

    def reduce_requirements(self, required_chemicals):
        reduced_chemicals_dict = {}
        for chemical in required_chemicals:
            if chemical.name in reduced_chemicals_dict.keys():
                reduced_chemicals_dict[chemical.name] = reduced_chemicals_dict[chemical.name] + chemical
            else:
                reduced_chemicals_dict[chemical.name] = chemical

        reduced_chemicals_list = []
        for chemical in reduced_chemicals_dict.values():
            reduced_chemicals_list.append(chemical)

        return reduced_chemicals_list

    def further_reduction_required(self, chemicals):
        any_reducable = False
        for chemical in chemicals:
            if chemical.name != 'ORE' and chemical.quantity > 0:
                any_reducable = True
                break
        return any_reducable

    def ore_to_produce_fuel(self, fuel:int = 1):
        required_chemicals = self.chemicals_required_to_make_fuel(fuel=fuel, available_chemicals=[])

        ore_required = 0
        for chemical in required_chemicals:
            if chemical.name == 'ORE':
                ore_required += chemical.quantity

        return ore_required

    def chemicals_required_to_make_fuel(self, available_chemicals=[], fuel:int = 1):
        further_reduction_required = True
        required_chemicals = available_chemicals
        required_chemicals.append(Chemical(name='FUEL', quantity=fuel))

        while further_reduction_required:
            chemicals_to_reduce = self.breakdown_group(required_chemicals)
            reduced_chemicals = self.reduce_requirements(chemicals_to_reduce)
            further_reduction_required = self.further_reduction_required(reduced_chemicals)
            required_chemicals = reduced_chemicals

        return required_chemicals