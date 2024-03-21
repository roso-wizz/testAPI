from rest_framework import serializers
from AnAPI.models import Story


class StorySerializerz(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    author = serializers.StringRelatedField()
    class Meta:
        lookup_field = "slug"
        model = Story
        fields = "__all__"





"""
class StorySerializerz(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    slug = serializers.SlugField(read_only=True)
    showed = serializers.DateTimeField(read_only=True)

    def make(self, validated_data):
        return Story.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.slug = validated_data.get("slug", instance.slug)
        instance.showed = validated_data.get("showed", instance.showed)
        instance.save()
        return instance
"""