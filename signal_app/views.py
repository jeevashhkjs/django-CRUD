from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import serializer_user
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import HttpResponse
from .models import Users
from .pagination import Pagination

class user_methods(viewsets.ModelViewSet, Pagination) :

    def get_data(self, request) :

        all_data = Users.objects.filter(description__icontains="ne", id=1)
        get_data = super().pagination(query=all_data, request=request)
        get_data["data"] = serializer_user(get_data["data"], many=True).data
        return JsonResponse(get_data)

        # paginator = Paginator(all_data, limit)
        # filter_data = paginator.get_page(page)
        # serialize_data = serializer_user(filter_data, many=True)
        # response_data = {
        #     "data": serialize_data.data,
        #     "message": "Movies Listed successfully",
        #     # "next": filter_data.has_next() if filter_data.next_page_number() else None,
        #     "pages": "pages",
        #     "prev": filter_data.previous_page_number() if filter_data.has_previous()  else None,
        #     "status": 200,
        #     "success": True,
        #     "total_no_pages": paginator.num_pages,
        #     "total_records": paginator.count
        #     }
        #
        # return JsonResponse(response_data, safe=False)

    def post_data(self, request) :
        get_data = request.data
        serializer_data = serializer_user(data=get_data)

        if serializer_data.is_valid() :
            serializer_data.save()
            return HttpResponse("Added")
        else :
            return HttpResponse("not added")

        # You need to move the JsonResponse outside of the if-else block
        return JsonResponse(serializer_data.data, safe=False)

    def delete_data(self, request, target_id) :
        model_object = Users.objects.get(id=target_id)
        model_object.delete()
        return HttpResponse("deleted successfully")

    def update_data(self, request, target_id) :
        model_object = Users.objects.get(id=target_id)
        get_data = request.data
        serializered_data = serializer_user(model_object, data=get_data)
        if serializered_data.is_valid() :
            serializered_data.save()
            return HttpResponse("Update successfully")
        else :
            return HttpResponse("not work")

    def login(self, request) :
        try :
            # Retrieve a specific user by some criteria (e.g., first user in the queryset)
            user = Users.objects.first()  # You can adjust the criteria as needed

            if user is not None :
                # Create a refresh token for the user
                refresh = RefreshToken.for_user(user)
                return HttpResponse(str(refresh))
            else :
                return HttpResponse('No users found', status=404)
        except Users.DoesNotExist :
            return HttpResponse('User not found', status=404)

    def logout(self, request) :
        refresh_token = request.data.get("refresh_token")
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"message" : "User logged out successfully"})
