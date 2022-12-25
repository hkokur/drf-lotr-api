from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from .models import Character


class CharacterTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.character = Character.objects.create(
            name="Isildur",
            race="Men",
            birth="SA 3209",
            gender="Male",
            death="TA 2",
            hair="Black",
            height="Very tall almost 7'1",
            realm="Arnor,Gondor",
            spouse="Unnamed wife",
        )

    def test_character_model(self):
        self.assertEqual(self.character.name, "Isildur")
        self.assertEqual(self.character.race, "Men")
        self.assertEqual(self.character.birth, "SA 3209")
        self.assertEqual(self.character.gender, "Male")
        self.assertEqual(self.character.death, "TA 2")
        self.assertEqual(self.character.hair, "Black")
        self.assertEqual(self.character.height, "Very tall almost 7'1")
        self.assertEqual(self.character.realm, "Arnor,Gondor")
        self.assertEqual(self.character.spouse, "Unnamed wife")


class ListCharacterTest(APITestCase):
    def test_create_character(self):
        sample = {
            "name": "Aragorn II Elessar",
            "race": "Men",
            "birth": "March 1 ,2931",
            "gender": "Male",
            "death": "FO 120",
            "hair": "Dark",
            "height": "198cm (6'6)",
            "realm": "Reunited Kingdom,Arnor,Gondor",
            "spouse": "Arwen",
        }
        Character.objects.create(**sample)

        response = self.client.post(reverse("api-list"), sample)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        res = self.client.post(
            reverse("api-name-detail", kwargs={"name": "Aragorn II Elessar"}), sample
        )
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_character(self):
        sample = {
            "name": "Aragorn II Elessar",
            "race": "Men",
            "birth": "March 1 ,2931",
            "gender": "Male",
            "death": "FO 120",
            "hair": "Dark",
            "height": "198cm (6'6)",
            "realm": "Reunited Kingdom,Arnor,Gondor",
            "spouse": "Arwen",
        }
        Character.objects.create(**sample)
        sample["name"] = "Aragorn Elessar"
        Character.objects.create(**sample)

        response_list = self.client.get(reverse("api-list"))
        self.assertEqual(response_list.status_code, status.HTTP_200_OK)
        self.assertEqual(response_list.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_list.data["results"], list)
        self.assertEqual(response_list.data["count"], 2)

        response_detail = self.client.get(
            reverse("api-name-detail", kwargs={"name": "Aragorn II Elessar"})
        )
        self.assertEqual(response_detail.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_detail.data["results"], list)
        self.assertEqual(response_detail.data["count"], 1)


class DetailCharacterTest(APITestCase):
    def create_one_item(self):
        sample = {
            "name": "Aragorn II Elessar",
            "race": "Men",
            "birth": "March 1 ,2931",
            "gender": "Male",
            "death": "FO 120",
            "hair": "Dark",
            "height": "198cm (6'6)",
            "realm": "Reunited Kingdom,Arnor,Gondor",
            "spouse": "Arwen",
        }
        obj, created = Character.objects.get_or_create(**sample)
        return obj

    def test_retrieves_one_item(self):
        character = self.create_one_item()
        res = self.client.get(reverse("api-detail", kwargs={"pk": character.id}))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["name"], character.name)
        self.assertEqual(res.data["race"], character.race)
        self.assertEqual(res.data["birth"], character.birth)
        self.assertEqual(res.data["gender"], character.gender)
        self.assertEqual(res.data["death"], character.death)
        self.assertEqual(res.data["hair"], character.hair)
        self.assertEqual(res.data["height"], character.height)
        self.assertEqual(res.data["name"], character.name)
        self.assertEqual(res.data["realm"], character.realm)
        self.assertEqual(res.data["spouse"], character.spouse)

    def test_updates_one_item(self):
        character = self.create_one_item()
        res = self.client.patch(
            reverse("api-detail", kwargs={"pk": character.id}), {"name": "Rachel"}
        )
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_deletes_one_item(self):
        character = self.create_one_item()
        res = self.client.delete(reverse("api-detail", kwargs={"pk": character.id}))
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
