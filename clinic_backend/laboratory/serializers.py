from rest_framework import serializers
from .models import LabTestType, LabRequest, LabReport


class LabTestTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTestType
        fields = ["id", "test_name", "description", "price", "created_at"]
        read_only_fields = ["id", "created_at"]


class LabReportSerializer(serializers.ModelSerializer):
    technician_name = serializers.CharField(
        source="technician.full_name", read_only=True
    )

    class Meta:
        model = LabReport
        fields = [
            "id",
            "lab_request",
            "report_file",
            "notes",
            "technician",
            "technician_name",
            "uploaded_at",
        ]
        read_only_fields = ["id", "technician", "uploaded_at"]


class LabRequestSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(
        source="patient.user.full_name", read_only=True
    )
    patient_uhid = serializers.CharField(source="patient.uhid", read_only=True)
    doctor_name = serializers.CharField(
        source="doctor.user.full_name", read_only=True
    )
    test_name = serializers.CharField(source="test.test_name", read_only=True)
    test_price = serializers.DecimalField(
        source="test.price", max_digits=10, decimal_places=2, read_only=True
    )
    report = LabReportSerializer(read_only=True)

    class Meta:
        model = LabRequest
        fields = [
            "id",
            "patient",
            "patient_name",
            "patient_uhid",
            "doctor",
            "doctor_name",
            "appointment",
            "test",
            "test_name",
            "test_price",
            "status",
            "report",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]
