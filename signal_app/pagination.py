from django.core.paginator import Paginator

class Pagination:

    def pagination(self, query, request):
        limit = request.GET.get('limit', 4) # get value from query params and assign default value
        page = request.GET.get('page', 10)

        paginator = Paginator(query, limit) # passing the query and limit into the paginator class
        filter_data = paginator.get_page(page) # passing page into the get_page function

        response_data = {
            "data": filter_data,
            "next": filter_data.next_page_number() if filter_data.has_next() else None,
            "previous": filter_data.previous_page_number() if filter_data.has_previous() else None,
            "no_of_pages": paginator.num_pages,
            "count": paginator.count
        }

        return response_data
