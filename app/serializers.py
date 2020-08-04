from rest_framework import serializers
from .models import Company, Employee


class CompanySerializer(serializers.ModelSerializer):
    """This is company serializer"""

    class Meta:
        model = Company
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    """This is employee serializer"""

    class Meta:
        model = Employee
        fields = ("name", )

    def create(self, validated_data):
        company = self.context.get("company")
        company_instance = Company.objects.get(id=company)
        instance = Employee.objects.create(company=company_instance, name=validated_data.get("name"))
        return instance
