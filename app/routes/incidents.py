from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.models.incident import Incident
from app.schemas.incident import incident_schema, incidents_schema
from app.extensions import db

incidents_bp = Blueprint('incidents', __name__)

@incidents_bp.route("/incidents", methods=["POST"])
def create_incident():
    try:
        incident = incident_schema.load(request.get_json())
        db.session.add(incident)
        db.session.commit()
        return incident_schema.dump(incident), 201
    except ValidationError as err:
        return {"errors": err.messages}, 400

@incidents_bp.route("/incidents", methods=["GET"])
def list_incidents():
    incidents = Incident.query.all()
    return incidents_schema.dump(incidents)

@incidents_bp.route("/incidents/<int:incident_id>", methods=["PATCH"])
def update_incident_status(incident_id):
    incident = Incident.query.get(incident_id)
    if not incident:
        return {"error": "Incident not found"}, 404
    
    try:
        data = {"status": request.get_json().get("status")}
        incident = incident_schema.load(data, instance=incident, partial=True)
        db.session.commit()
        return incident_schema.dump(incident)
    except ValidationError as err:
        return {"errors": err.messages}, 400

@incidents_bp.route("/incidents/<int:incident_id>", methods=["DELETE"])
def delete_incident(incident_id):
    incident = Incident.query.get(incident_id)
    if not incident:
        return {"error": "Incident not found"}, 404
    
    db.session.delete(incident)
    db.session.commit()
    
    return "", 204