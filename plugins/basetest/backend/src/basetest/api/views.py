from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from baserow.contrib.database.models import Database
from baserow.contrib.database.table.models import Table
from baserow.contrib.database.fields.models import Field

class StartingView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response({"title": "Starting title", "content": "Starting text"})


class CoursesView(APIView):
    permission_classes = (AllowAny,)
    
    def get_model_and_table(self):
        """Helper method to get the model and table"""
        database = Database.objects.get(name="Hublms")
        table = Table.objects.get(database=database, name="Courses")
        model = table.get_model()
        return model, table
    
    def get_course_data(self, course):
        """Helper method to format course data"""
        import logging
        logger = logging.getLogger(__name__)
        
        try:
            # Get all field objects from the model
            field_objects = course.get_field_objects()
            
            # Prepare the course data with actual field values
            course_data = {
                'id': course.id,
                'order': str(course.order)  # Convert Decimal to string for JSON serialization
            }
            
            # Add all custom fields from the table
            for field_object in field_objects:
                field_name = field_object['field'].name
                field_type = field_object['type'].type
                
                try:
                    field_value = getattr(course, f'field_{field_object["field"].id}')
                    
                    # Convert field value based on its type
                    if field_value is not None:
                        if field_type == 'number':
                            field_value = float(field_value) if field_value is not None else None
                        elif field_type == 'boolean':
                            field_value = bool(field_value)
                        elif field_type in ['date', 'last_modified', 'created_on']:
                            field_value = field_value.isoformat() if field_value else None
                    
                    course_data[field_name] = field_value
                except Exception as e:
                    logger.warning(f"Could not get field {field_name}: {str(e)}")
                    course_data[field_name] = None
            
            # Add timestamps
            course_data.update({
                'created_on': course.created_on.isoformat() if course.created_on else None,
                'updated_on': course.updated_on.isoformat() if course.updated_on else None
            })
            
            return course_data
            
        except Exception as e:
            logger.error(f"Error getting course data: {str(e)}")
            raise

    def get(self, request, course_id=None):
        """
        GET /api/basetest/courses/ - List all courses
        GET /api/basetest/courses/{id}/ - Get single course
        """
        try:
            model, _ = self.get_model_and_table()
            
            # Get single course
            if course_id:
                course = model.objects.get(id=course_id)
                return Response({
                    "status": "success",
                    "course": self.get_course_data(course)
                })
            
            # Get all courses
            courses = model.objects.all()
            courses_data = [self.get_course_data(course) for course in courses]
            
            return Response({
                "status": "success",
                "count": len(courses_data),
                "courses": courses_data
            })
            
        except model.DoesNotExist:
            return Response({"error": "Course not found"}, status=404)
        except Database.DoesNotExist:
            return Response({"error": "Database 'Hublms' not found"}, status=404)
        except Table.DoesNotExist:
            return Response({"error": "Table 'Courses' not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
    
    def post(self, request):
        """
        POST /api/basetest/courses/ - Create a new course
        """
        try:
            model, table = self.get_model_and_table()
            data = request.data
            
            # Get field mappings
            field_objects = {}
            for field_obj in model.get_field_objects():
                field_name = field_obj['field'].name
                field_objects[field_name] = field_obj
            
            # Prepare course data with field mappings
            course_data = {}
            for field_name, value in data.items():
                if field_name in field_objects:
                    field_obj = field_objects[field_name]
                    field_id = field_obj['field'].id
                    field_type = field_obj['type'].type
                    
                    # Convert value based on field type
                    if value is not None:
                        if field_type == 'number':
                            value = float(value) if value != '' else None
                        elif field_type == 'boolean':
                            value = bool(value)
                    
                    course_data[f'field_{field_id}'] = value
            
            # Create the course
            course = model.objects.create(**course_data)
            
            return Response({
                "status": "success",
                "message": "Course created successfully",
                "course": self.get_course_data(course)
            }, status=201)
            
        except Exception as e:
            import traceback
            logger.error(f"Error creating course: {str(e)}\n{traceback.format_exc()}")
            return Response({"error": str(e)}, status=400)
    
    def put(self, request, course_id):
        """
        PUT /api/basetest/courses/{id}/ - Update a course
        """
        try:
            model, table = self.get_model_and_table()
            
            # Get the course to update
            course = model.objects.get(id=course_id)
            data = request.data
            
            # Get field mappings
            field_objects = {}
            for field_obj in model.get_field_objects():
                field_name = field_obj['field'].name
                field_objects[field_name] = field_obj
            
            # Update fields
            for field_name, value in data.items():
                if field_name in field_objects:
                    field_obj = field_objects[field_name]
                    field_id = field_obj['field'].id
                    field_type = field_obj['type'].type
                    
                    # Convert value based on field type
                    if value is not None:
                        if field_type == 'number':
                            value = float(value) if value != '' else None
                        elif field_type == 'boolean':
                            value = bool(value)
                    
                    setattr(course, f'field_{field_id}', value)
            
            # Save changes
            course.save()
            
            return Response({
                "status": "success",
                "message": "Course updated successfully",
                "course": self.get_course_data(course)
            })
            
        except model.DoesNotExist:
            return Response({"error": "Course not found"}, status=404)
        except Exception as e:
            import traceback
            logger.error(f"Error updating course: {str(e)}\n{traceback.format_exc()}")
            return Response({"error": str(e)}, status=400)


