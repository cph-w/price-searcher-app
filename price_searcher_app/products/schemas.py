from marshmallow import Schema, ValidationError, fields, validate


# Custom fields
class BooleanInStockField(fields.Boolean):
    def _deserialize(self, value, attr, data, **kwargs):
        # is True or is False is faster isinstance(x, bool)
        if value is True or value is False:
            return value
        if value.lower() in ('y', 'yes', 'true'):
            return True
        if value.lower() in ('n', 'no', 'false'):
            return False
        raise ValidationError('Unknown in_stock serialization field')


class StringWithEmptyAsNone(fields.String):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, allow_none=True, **kwargs)

    def _deserialize(self, value, attr, data, **kwargs):
        if value == '':
            return None
        return super()._deserialize(value, attr, data, **kwargs)


class FloatWithEmptyAsNone(fields.Float):
    def __init__(self, *args, allow_nan=False, as_string=False, **kwargs):
        super().__init__(
            *args,
            allow_nan=allow_nan,
            as_string=as_string,
            allow_none=True,
            **kwargs
        )

    def _deserialize(self, value, attr, data, **kwargs):
        if value == '':
            return None
        return super()._deserialize(value, attr, data, **kwargs)


# Schemas
class ProductSchema(Schema):
    """ Schema for products, mostly using fields with custom
    deserialization to support multiple data sources with unified logic.

    Dumped data will be returned in the format:
        - id as a string
        - name as a string
        - brand as a string
        - retailer as a string
        - price as a float
        - in_stock as a boolean
    As described in the requirements.
    """
    id = fields.String(required=True)
    name = StringWithEmptyAsNone(missing=None)
    brand = StringWithEmptyAsNone(missing=None)
    retailer = StringWithEmptyAsNone(missing=None)
    price = FloatWithEmptyAsNone(missing=None)
    in_stock = BooleanInStockField(missing=None)


class ProductsResponseSchema(Schema):
    """ Response schema that returns pagination information along with data
    """
    data = fields.List(fields.Nested(ProductSchema))
    page = fields.Integer()
    page_size = fields.Integer()
    total_records = fields.Integer()


class ProductsRequestSchema(Schema):
    """ Schema for URL arguments for the products endpoint, defaults the
    pagination to the first page of length 10.
    """
    page = fields.Integer(missing=1, validate=validate.Range(min=1))
    page_size = fields.Integer(missing=10, validate=validate.Range(min=1))
