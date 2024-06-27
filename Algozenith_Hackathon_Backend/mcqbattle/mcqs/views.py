# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MCQ
from .serializers import MCQSerializer
from rest_framework.permissions import IsAuthenticated

class MCQListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        mcqs = MCQ.objects.all()
        serializer = MCQSerializer(mcqs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MCQSerializer(data=request.data)
        if serializer.is_valid():
            mcq = MCQ.objects.create(
                body=serializer.validated_data['body'],
                explanation=serializer.validated_data['explanation'],
                options=serializer.validated_data['options']
            )
            mcq.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MCQRetrieveUpdateDestroyView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return MCQ.objects.get(pk=pk)
        except MCQ.DoesNotExist:
            return None

    def get(self, request, pk):
        mcq = self.get_object(pk)
        if mcq is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MCQSerializer(mcq)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        mcq = self.get_object(pk)
        if mcq is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MCQSerializer(mcq, data=request.data)
        if serializer.is_valid():
            mcq.body = serializer.validated_data['body']
            mcq.explanation = serializer.validated_data['explanation']
            mcq.options = serializer.validated_data['options']
            mcq.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        mcq = self.get_object(pk)
        if mcq is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        mcq.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
