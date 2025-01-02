from ...selializers.asset.usage_category_serializer import UsageCategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ...models.asset.usage_category import UsageCategory
from ...backends.user.cookie_authentication import CookieTokenBackend


class UsageCategoryView(APIView):
    authentication_classes = [CookieTokenBackend]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        req = request.data
        serializer = UsageCategorySerializer(data=req)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        categories = UsageCategory.objects.all()
        serializer = UsageCategorySerializer(categories, many=True)
        return Response(serializer.data)
