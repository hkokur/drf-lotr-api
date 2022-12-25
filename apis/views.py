from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
import csv

from .models import Character
from .serializers import CharacterSerializer, CharacterListSerializer


class ListCharacter(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterListSerializer

    def get_queryset(self):
        name = self.kwargs.get("name", None)
        if name is not None:
            self.queryset = self.queryset.filter(name=name)
            self.serializer_class = CharacterSerializer
        return super().get_queryset()


class DetailCharacter(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


def data_transportation(csv_path):
    # The function read the csv file from given path and create or update the features of the characters.
    # RUN ON THE SHELL
    with open(csv_path, "r") as f:
        data = csv.DictReader(f)
        data = [row for row in data]

    # data format will be :
    # (birth, death, gender, hair, height, name, race, realm, spouse)
    for row in data:
        if row["race"] != "" and row["name"] is not None and row["name"] != "":
            obj, created = Character.objects.update_or_create(
                name=row["name"],
                race=row["race"],
                birth=row["birth"],
                gender=row["gender"],
                death=row["death"],
                hair=row["hair"],
                height=row["height"],
                realm=row["realm"],
                spouse=row["spouse"],
            )
