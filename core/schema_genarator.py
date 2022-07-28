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
        :param form: A model form object
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
            description="The request body should be a 'application/json' encoded object, containing the following "
                        "items.",

        )


class ListSchema:
    """
    This creates a schema for a list view
    """

    def __init__(self, parameters: list):
        """
        This method creates a list schema for a list view
        :param parameters: A list of dictionaries required parameters.
                                    Format - [{'name': 'parameter_name', 'help_text': 'string',
                                    'required': The required status}]
        """
        self.parameters = parameters

    def create_schema(self):
        """
        This method loops through all the passed parameters and creates a schema
        :return:
        """
        fields = []
        for parameter in self.parameters:
            fields.append(coreapi.Field(
                name=parameter.get('name'),
                required=parameter.get('required'),
                location='form',
                schema=coreschema.String(
                    title=str(parameter.get('name').replace('_', ' ').title()),
                    description=str(parameter.get('help_text')),
                ),
            ))
        return ManualSchema(
            fields=fields,
            encoding="application/json",
            description="The following parameters should be included in the URL path.",

        )
