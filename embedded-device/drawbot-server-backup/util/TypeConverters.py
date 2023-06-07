from werkzeug.routing import BaseConverter, ValidationError
from model.Command import Command


class CommandTypeConverter(BaseConverter):

    def to_python(self, value):
        try:
            request_type = Command(value)
            return request_type
        except ValueError as err:
            raise ValidationError()

    def to_url(self, obj):
        return obj.value
