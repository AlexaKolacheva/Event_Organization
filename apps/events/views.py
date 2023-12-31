from datetime import timedelta

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .filters import EventFilter
from .models import CustomUser, Category, Event,  Participation
from .permissions import IsEventOwnerOrReadOnly, IsEventCreatorOrReadOnly, IsOwnerOrReadOnly
from .serializers import CustomUserSerializer, CategorySerializer, EventSerializer,  ParticipationSerializer
from .tasks import send_event_reminder_notification, process_image


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_token_pair(user):
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        return access_token, refresh_token


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = EventFilter
    search_fields = ['category', 'date_start' ]
    permission_classes = [IsEventCreatorOrReadOnly]

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        event = serializer.save()
        send_event_reminder_notification.apply_async((event.id,), eta=event.date_start - timedelta(days=1))
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_update(self, serializer):
        event = serializer.save()
        send_event_reminder_notification.apply_async((event.id,), eta=event.date_start - timedelta(days=1))
        return Response(serializer.data, status=status.HTTP_200_OK)





class ParticipationViewSet(viewsets.ModelViewSet):
    queryset = Participation.objects.all()
    serializer_class = ParticipationSerializer
    permission_classes = [IsEventOwnerOrReadOnly]
