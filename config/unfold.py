# config/settings/unfold_settings.py

from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.templatetags.static import static

UNFOLD = {
    "SITE_TITLE": "farbeshbot",
    "SITE_HEADER": "farbeshbot",
    "SITE_URL": "/",
    "SITE_ICON": {
        "light": lambda request: static("logo/logo.png"),  # Light mode logo
        "dark": lambda request: static("logo/logo.png"),   # Dark mode logo
    },
    "SITE_LOGO": {
        "light": lambda request: static("logo/logo.png"),  # Light mode logo
        "dark": lambda request: static("logo/logo.png"),   # Dark mode logo
    },
    "SITE_SYMBOL": "speed",  # Symbol from the icon set
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/png",  # Updated to PNG for better compatibility
            "href": lambda request: static("logo/favicon.png"),
        },
    ],
    "SHOW_HISTORY": True,  # Show/hide the "History" button
    "SHOW_VIEW_ON_SITE": True,  # Show/hide the "View on site" button
    "ENVIRONMENT": None,
    "DASHBOARD_CALLBACK": None,
    "STYLES": [
        lambda request: static("css/style.css"),  # Custom styles
    ],
    "SCRIPTS": [
        lambda request: static("js/script.js"),  # Custom scripts
    ],
    "COLORS": {
        "primary": {
            "50": "250 245 255",
            "100": "243 232 255",
            "200": "233 213 255",
            "300": "216 180 254",
            "400": "192 132 252",
            "500": "168 85 247",
            "600": "147 51 234",
            "700": "126 34 206",
            "800": "107 33 168",
            "900": "88 28 135",
            "950": "59 7 100",
        },
    },
    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "en": "🇬🇧",
                "fr": "🇫🇷",
                "nl": "🇧🇪",
            },
        },
    },
    "SIDEBAR": {
        "show_search": True, 
        "show_all_applications": True, 
        "navigation": [
            {
                "title": _("Asosiy Sahifa"),
                "separator": False,  # Top border
                "collapsible": True,
                "items": [
                    {
                        "title": _("Asosiy sahifa"),
                        "icon": "home",
                        "link": reverse_lazy("admin:index"),
                    },
                    {
                        "title": _("Foydalanuvchilar"),
                        "icon": "person",
                        "link": reverse_lazy("admin:category_users_changelist"),
                    },
                ],
            },
            {
                "title": _("Kategoryalar"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Kategoryalar"),
                        "icon": "category",  
                        "link": reverse_lazy("admin:category_category_changelist"),
                    },
                ],
            
            },
        ],
    },
}
