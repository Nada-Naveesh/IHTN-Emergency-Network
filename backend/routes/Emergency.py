from flask import Blueprint, request, jsonify
from service.triage import predict_severity
from service.hospital import get_hospital

emergency_bp = Blueprint("emergency", __name__)

@emergency_bp.route("/emergency", methods=["POST"])
def emergency():
    data = request.get_json()
    symptoms = data.get("symptoms", "")

    severity = predict_severity(symptoms)
    hospital = get_hospital(severity)

    return jsonify({
        "symptoms": symptoms,
        "severity": severity,
        "hospital": hospital
    })
