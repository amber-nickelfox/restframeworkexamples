from .serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, views, parsers, mixins, generics
from .models import Company
from rest_framework.permissions import IsAuthenticated


@api_view(['POST', 'GET'])
def company_view(request):
    if request.method == "GET":
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "success"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', 'GET', 'PATCH'])
def company_details(request, pk):
    """
    Update using id
    """
    if request.method == "GET":
        try:
            company = Company.objects.get(id=pk)
            serializer = CompanySerializer(company)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Company.DoesNotExist:
            return Response({"message": "Data not exist"}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        try:
            Company.objects.get(id=pk).delete()
            return Response({"message": "delete successfully"}, status=status.HTTP_200_OK)
        except Company.DoesNotExist:
            return Response({"message": "Data not exist"}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PATCH":
        company = Company.objects.get(id=pk)
        serializer = CompanySerializer(company, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "update success"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyAPIView(views.APIView):
    """
    Company API View
    """

    serializer_class = CompanySerializer
    parser_classes = (parsers.JSONParser,)
    model = Company
    permission_classes = ()

    def get(self, request, *args, **kwargs):
        company = Company.objects.all()
        serializer = self.serializer_class(company, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyDetailAPIView(views.APIView):
    """
    Company API View
    """

    serializer_class = CompanySerializer
    parser_classes = (parsers.JSONParser,)
    model = Company
    permission_classes = ()

    def get(self, request, pk, *args, **kwargs):
        company = Company.objects.get(id=pk)
        serializer = self.serializer_class(company)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        company = self.model.objects.get(id=pk).delete()
        return Response({"message": "data deleted"}, status=status.HTTP_200_OK)

    def patch(self, request, pk, *args, **kwargs):
        company = Company.objects.get(id=pk)
        serializer = self.serializer_class(company, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeAPIView(views.APIView):
    serializer_class = EmployeeSerializer
    parser_classes = (parsers.JSONParser,)
    model = Company
    permission_classes = ()

    def post(self, request, company_id, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"company": company_id})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "success"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyMixinsAPIView(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           mixins.DestroyModelMixin,
                           generics.GenericAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
