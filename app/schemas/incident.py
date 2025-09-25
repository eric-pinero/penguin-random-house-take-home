from marshmallow import validate
from app.extensions import ma
from app.models.incident import Incident

from marshmallow import fields

class IncidentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Incident
        load_instance = True
        include_fk = True
    
    title = ma.auto_field(validate=validate.Length(min=1, max=100))
    description = ma.auto_field(validate=validate.Length(min=1))
    status = fields.String(
        validate=validate.OneOf(["Open", "In Progress", "Resolved"]),
        dump_default="Open",
        load_default="Open"
    )

incident_schema = IncidentSchema()
incidents_schema = IncidentSchema(many=True)