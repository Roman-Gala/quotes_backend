from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import QuoteSerializer
from .models import Quote


@api_view(['GET'])
def get_routes(request):
    routes = [
        {
            'Endpoint': '/quotes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of quotes'
        },
        {
            'Endpoint': '/events/create/',
            'method': 'POST',
            'body': None,
            'description': 'Creates a new quote object with POST data'
        },
        {
            'Endpoint': '/events/id/update/',
            'method': 'PUT',
            'body': None,
            'description': 'Updates an existing event object with PUT data'
        },
        {
            'Endpoint': '/events/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing event object'
        }
    ]
    return Response(routes)


@api_view(['GET'])
def get_quotes(request):
    quotes = Quote.objects.all()
    serializer = QuoteSerializer(quotes, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_quote(request):
    data = request.data

    event = Quote.objects.create(
        text=data['text'],
        author=data['author'],
    )
    serializer = QuoteSerializer(event, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_quote(request, _id):
    event = Quote.objects.get(id=_id)
    event.delete()
    return Response('Event was deleted!')
