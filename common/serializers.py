from common.i18n import (
    DEFAULT_LANGUAGE_CODE,
    get_request_language,
)


class LocalizedFieldsMixin:
    """
    Return translated name and description fields.

    Fallback order:

    1. Requested language
    2. Default language, currently English
    3. Original model field
    """

    def get_translations_by_language(self, obj):
        """
        Build and cache the object's translations.

        When translations are prefetched, this does not
        create an additional database query.
        """

        cache_attribute = (
            "_ginkova_translations_by_language"
        )

        cached_translations = getattr(
            obj,
            cache_attribute,
            None,
        )

        if cached_translations is not None:
            return cached_translations

        translations_by_language = {
            translation.language: translation
            for translation in obj.translations.all()
        }

        setattr(
            obj,
            cache_attribute,
            translations_by_language,
        )

        return translations_by_language

    def get_translation(self, obj):
        request = self.context.get("request")

        requested_language = get_request_language(
            request
        )

        translations_by_language = (
            self.get_translations_by_language(obj)
        )

        return (
            translations_by_language.get(
                requested_language
            )
            or translations_by_language.get(
                DEFAULT_LANGUAGE_CODE
            )
        )

    def get_name(self, obj):
        translation = self.get_translation(obj)

        if translation is not None:
            return translation.name

        return obj.name

    def get_description(self, obj):
        translation = self.get_translation(obj)

        if translation is not None:
            return translation.description

        return obj.description