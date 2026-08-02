from common.i18n import (
    DEFAULT_LANGUAGE_CODE,
    normalize_language_code,
)


def get_translations_by_language(obj):
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

    if not hasattr(obj, "translations"):
        return {}

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


def get_localized_translation(
    obj,
    language_code,
):
    requested_language = normalize_language_code(
        language_code
    )

    translations_by_language = (
        get_translations_by_language(obj)
    )

    return (
        translations_by_language.get(
            requested_language
        )
        or translations_by_language.get(
            DEFAULT_LANGUAGE_CODE
        )
    )


def get_localized_field(
    obj,
    field_name,
    language_code,
):
    translation = get_localized_translation(
        obj,
        language_code,
    )

    if translation is not None:
        translated_value = getattr(
            translation,
            field_name,
            None,
        )

        if translated_value not in (
            None,
            "",
        ):
            return translated_value

    return getattr(
        obj,
        field_name,
        "",
    )


def get_localized_name(
    obj,
    language_code,
):
    return get_localized_field(
        obj,
        "name",
        language_code,
    )


def get_localized_description(
    obj,
    language_code,
):
    return get_localized_field(
        obj,
        "description",
        language_code,
    )