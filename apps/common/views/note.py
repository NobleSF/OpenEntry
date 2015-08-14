
from rest_framework import viewsets
from apps.common.models import Note
from apps.common.serializers.note import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides
    `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
