from rest_framework.decorators import api_view
from rest_framework.response  import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Create your views here.
#decorator
@api_view(['GET'] )
def getbook(request):
    book_objs = Book.objects.all()
    #data = request.POST['x']
    #data = request.POST.get('x')
    #print(student_objs[1].name)

    serializer = BookSerializer(book_objs, many=True)

    return Response({"message": serializer.data})

from rest_framework_simplejwt.tokens import RefreshToken

class Userregister(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"status":403,"error":serializer.errors, "msg":"somthings wrong"})
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        refresh = RefreshToken.for_user(user)

        return Response({"msg":"usercreated", "user":serializer.data, 'refresh': str(refresh),
        'access': str(refresh.access_token)})

    def get(self, request):
        user_objs = User.objects.all()
        serializer = UserSerializer(user_objs, many=True)
        return Response({"message": serializer.data})


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class StudentAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        import pdb; pdb.set_trace()
        student_objs = Student.objects.all()
        serializer = StudentSerializer(student_objs, many=True)
        return Response({"message": serializer.data})

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"status":403,"error":serializer.errors , "message": "somethings went worng"})
        serializer.save()
        return Response({"message": serializer.data})

    def put(self, request):
        try:
            student_obj = Student.objects.get(id=request.data['id'])
            serializer = StudentSerializer(student_obj, data=request.data)

            if not serializer.is_valid():
                return Response({"status":403,"error":serializer.errors , "message": "somethings went worng"})
            serializer.save()
            return Response({"message": serializer.data})
    
        except Exception as e:
            return Response({"status": 403 , "message":"id not mached"})

    def patch(self, request):
        try:
            student_obj = Student.objects.get(id=request.data['id'])
            serializer = StudentSerializer(student_obj, data=request.data, partial=True)
            print('abc')

            if not serializer.is_valid():
                return Response({"status":403,"error":serializer.errors , "message": "somethings went worng"})
            serializer.save()
            return Response({"message": serializer.data})
    
        except Exception as e:
            return Response({"status": 403 , "message":"id not mached"})

    def delete(self, request,id):
        #import pdb; pdb.set_trace()
        try:          
            #i = self.get('id')        
            #print(i)
            student_obj = Student.objects.get(id=id)
            student_obj.delete()
            return Response({"message": 'delete successful'})

        except Exception as e:
            return Response({"status": 403 , "message":"id not mached"})
#   




















# @api_view(['GET'] )
# def get(request):
#     student_objs = Student.objects.all()
#     #data = request.POST['x']
#     #data = request.POST.get('x')
#     #print(student_objs[1].name)

#     serializer = StudentSerializer(student_objs, many=True)

#     return Response({"message": serializer.data})


# @api_view(['POST'] )
# def post(request):

#     serializer = StudentSerializer(data=request.data)

#     if not serializer.is_valid():
#         return Response({"status":403,"error":serializer.errors , "message": "somethings went worng"})
#     serializer.save()


#     return Response({"message": serializer.data})


# @api_view(['PUT'] )
# def put(request, id):
#     try:
#         student_obj = Student.objects.get(id=id)
#         serializer = StudentSerializer(student_obj, data=request.data)

#         if not serializer.is_valid():
#             return Response({"status":403,"error":serializer.errors , "message": "somethings went worng"})
#         serializer.save()
#         return Response({"message": serializer.data})
    
#     except Exception as e:
#         return Response({"status": 403 , "message":"id not mached"})


# @api_view(['PATCH' ] )
# def patch(request, id):
#     try:
#         student_obj = Student.objects.get(id=id)
#         serializer = StudentSerializer(student_obj, data=request.data, partial=True)

#         if not serializer.is_valid():
#             return Response({"status":403,"error":serializer.errors , "message": "somethings went worng"})
#         serializer.save()
#         return Response({"message": serializer.data})
    
#     except Exception as e:
#         return Response({"status": 403 , "message":"id not mached"})


# @api_view(['DELETE' ] )
# def delete(request):
#     try:
#         #  http://127.0.0.1:8000/delete/?id=8
#         # but this why to get the id is not working here dontknow why?
#         id = request.Get.get('id')
#         student_obj = Student.objects.get(id=id)
#         student_obj.delete()
#         return Response({"message": 'delete successful'})

#     except Exception as e:
#         return Response({"status": 403 , "message":"id not mached"})