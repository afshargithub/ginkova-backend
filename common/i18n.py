from typing import Final

from django.conf import settings


SUPPORTED_LANGUAGE_CODES: Final[frozenset[str]] = frozenset(
    language_code
    for language_code, _language_name in settings.LANGUAGES
)

DEFAULT_LANGUAGE_CODE: Final[str] = settings.LANGUAGE_CODE

RTL_LANGUAGE_CODES: Final[frozenset[str]] = frozenset({
    "fa",
})


def normalize_language_code(
    language_code: str | None,
) -> str:
    """
    Normalize a language code such as `fa-IR` to `fa`.

    Unsupported or empty language codes fall back to
    settings.LANGUAGE_CODE.
    """

    if not language_code:
        return DEFAULT_LANGUAGE_CODE

    normalized_code = (
        language_code
        .strip()
        .lower()
        .split("-")[0]
    )

    if normalized_code in SUPPORTED_LANGUAGE_CODES:
        return normalized_code

    return DEFAULT_LANGUAGE_CODE


def get_request_language(request) -> str:
    """
    Return the active supported language for a request.

    LocaleMiddleware stores the selected language in
    request.LANGUAGE_CODE.
    """

    language_code = getattr(
        request,
        "LANGUAGE_CODE",
        DEFAULT_LANGUAGE_CODE,
    )

    return normalize_language_code(language_code)


def get_language_direction(
    language_code: str | None,
) -> str:
    """
    Return `rtl` for Persian and `ltr` for other
    supported languages.
    """

    normalized_code = normalize_language_code(
        language_code
    )

    if normalized_code in RTL_LANGUAGE_CODES:
        return "rtl"

    return "ltr"