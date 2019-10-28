import factory
import factory.fuzzy


class ProductFactory(factory.DictFactory):
    id = factory.fuzzy.FuzzyText()
    name = factory.fuzzy.FuzzyText()
    brand = factory.fuzzy.FuzzyText()
    retailer = factory.fuzzy.FuzzyText()
    price = factory.fuzzy.FuzzyFloat(low=0.01, high=10000.0, precision=10)
    in_stock = factory.fuzzy.FuzzyChoice((True, False))


class RawProductFactory(factory.DictFactory):
    id = factory.fuzzy.FuzzyText()
    name = factory.fuzzy.FuzzyText()
    brand = factory.fuzzy.FuzzyText()
    retailer = factory.fuzzy.FuzzyText()
    price = factory.fuzzy.FuzzyFloat(low=0.01)
    in_stock = factory.fuzzy.FuzzyChoice(
        ('y', 'yes', 'n', 'no', True, False, 'true', 'false')
    )
