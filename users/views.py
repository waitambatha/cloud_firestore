from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import UserSerializer
import firebase_admin
from firebase_admin import firestore


@api_view(['GET'])
def base_view(request):
    """Show available links at the base URL."""
    links = {
        "Users API": "http://127.0.0.1:8000/api/users/",
        "Swagger Documentation": "http://127.0.0.1:8000/swagger/"
    }
    return Response(links, status=status.HTTP_200_OK)


class UserView(APIView):
    def get(self, request):
        """Fetch all user records."""
        db = firestore.client()
        users_ref = db.collection('users')
        users = [doc.to_dict() for doc in users_ref.stream()]
        return Response(users, status=status.HTTP_200_OK)

    def post(self, request):
        """Create a new user record."""
        # Updated to handle new fields
        data = request.data
        required_fields = ['name', 'address', 'phone_number', 'next_of_kin', 'next_of_kin_phone', 'dnr_status',
                           'nfc_tag']

        # Ensure all required fields are provided
        if not all(field in data for field in required_fields):
            return Response({"error": "Missing required fields."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            db = firestore.client()
            db.collection('users').add(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        """Delete user record."""
        user_id = request.query_params.get('id')
        if user_id:
            db = firestore.client()
            user_ref = db.collection('users').document(user_id)
            user_ref.delete()
            return Response({"message": "User deleted successfully"}, status=status.HTTP_200_OK)
        return Response({"error": "User ID is required"}, status=status.HTTP_400_BAD_REQUEST)
