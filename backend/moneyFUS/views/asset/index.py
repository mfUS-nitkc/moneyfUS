from django.shortcuts import get_object_or_404
from django.forms import ValidationError
from ...selializers.asset.asset_log_serializer import AssetLogSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ...models.asset.asset_log import AssetLog
from ...models.asset.usage_category import UsageCategory
from ...backends.user.cookie_authentication import CookieTokenBackend
from ...utils.Response import create_response, create_error_response

class AssetView(APIView):
    authentication_classes = [CookieTokenBackend]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        req = request.data
        user = request.user
        req["user"] = user.user_id
        usage_category_id = request.data.get("usage_category_id")
        usage_category_code = request.data.get("usage_category_code")
        
        if not usage_category_id and usage_category_code:
            usage_category = UsageCategory.objects.get(usage_category_code = usage_category_code)
            if not usage_category:
                error_res = create_error_response("Invalid category_code", status=status.HTTP_400_BAD_REQUEST)
                return error_res
            usage_category_id = usage_category.usage_category_id
            
        if not usage_category_id:
            error_res = create_error_response("usage_category_id or usage_category_code is required.", status=status.HTTP_400_BAD_REQUEST)
            return error_res
        
        req["usage_category"] = usage_category_id

        serializer = AssetLogSerializer(data=req)
        
        if serializer.is_valid():
            create_data = serializer.save()
            response = create_response({'asset_id': create_data.asset_id}, status=status.HTTP_201_CREATED)
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        pk = request.data.get("asset_id")
        if pk:
            asset = get_object_or_404(AssetLog, pk=pk)
            serializer = AssetLogSerializer(asset)
        else:
            queryset = AssetLog.objects.all().filter(user_id=request.user.user_id)
            serializer = AssetLogSerializer(queryset, many=True)
        return Response(serializer.data)

    def delete(self, request):
        pk = request.data.get("asset_id")
        if pk:
            asset = get_object_or_404(AssetLog, pk=pk)
        else:
            res = Response(
                {"success": False, "reason": "asset_id is needed."},
                status=status.HTTP_400_BAD_REQUEST,
            )
            return res
        try:
            asset.delete()
            res = Response({"success": True}, status=status.HTTP_204_NO_CONTENT)
        except ValidationError:
            res = Response(
                {"success": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        return res

    def patch(self, request):
        pk = request.data.get("asset_id")
        if pk:
            asset = get_object_or_404(AssetLog, pk=pk)
        else:
            res = Response(
                {"success": False, "reason": "asset_id is needed."},
                status=status.HTTP_400_BAD_REQUEST,
            )
            return res
        asset.amount = request.data.get("amount")
        asset.issued_at = request.data.get("issued_at")
        usage_category_id = request.data.get("usage_category")
        new_usage_category = get_object_or_404(UsageCategory, pk=usage_category_id)
        asset.usage_category = new_usage_category
        asset.save()
        res = Response({"success": True})
        return res
