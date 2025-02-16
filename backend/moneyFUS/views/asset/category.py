from ...serializers.asset.usage_category_serializer import UsageCategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ...models.asset.usage_category import UsageCategory
from ...backends.user.cookie_authentication import CookieTokenBackend

from ...utils.Response import create_error_response, create_response


class UsageCategoryView(APIView):
    authentication_classes = [CookieTokenBackend]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        req = request.data
        serializer = UsageCategorySerializer(data=req)
        if serializer.is_valid():
            serializer.save()
            return create_response({'item': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        categories = UsageCategory.objects.all()
        serializer = UsageCategorySerializer(categories, many=True)
        response = create_response({'items': serializer.data}, status=status.HTTP_200_OK)
        return response
    