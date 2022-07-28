import coreapi
import coreschema
from rest_framework.schemas import ManualSchema


class CreateSchema:
    """
    This class creates a schema from a form object
    """

    def __init__(self, form):
        """
        This method initializes the class
        :param form:
        """
        self.form = form
        self.schema = None

    def create_schema(self):
        fields = []
        for key, value in self.form.fields.items():
            fields.append(coreapi.Field(
                name=key,
                required=value.required,
                location='form',
                schema=coreschema.String(
                    title=str(value.label),
                    description=str(value.help_text),
                ),
            ))
        return ManualSchema(
            fields=fields,
            encoding="application/json",
        )
