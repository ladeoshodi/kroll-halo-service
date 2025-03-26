from .models import KrollHaloMapping
from .serializers import KrollHaloMappingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class KrollHaloMappingList(APIView):
    def get(self, request):
        kroll_halo_mapping = KrollHaloMapping.objects.all()
        serializer = KrollHaloMappingSerializer(kroll_halo_mapping, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = KrollHaloMappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KrollHaloMappingDetail(APIView):
    def get_object(self, kroll_ticket_id):
        try:
            return KrollHaloMapping.objects.get(kroll_ticket_id=kroll_ticket_id)
        except KrollHaloMapping.DoesNotExist:
            raise Http404

    def get(self, request, kroll_ticket_id):
        kroll_halo_mapping = self.get_object(kroll_ticket_id)
        serializer = KrollHaloMappingSerializer(kroll_halo_mapping)
        return Response(serializer.data)
