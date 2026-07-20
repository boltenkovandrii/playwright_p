PROFILES = {
    "desktop": {
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
    },

    "desktop_2560x1600": {
        "viewport": {
            "width": 2560,
            "height": 1600,
        },
    },

    "desktop_1920x1200": {
        "viewport": {
            "width": 1920,
            "height": 1200,
        },
    },

    "mobile_landscape": {
        "device": "iPhone 13 landscape",
    },
    "mobile": {
        "device": "iPhone 13",
    },
    "tablet_landscape": {
        "device": "iPad Mini landscape",
    },
    "tablet": {
        "device": "iPad Mini",
    },
}

def get_profile(playwright, profile):
    if profile.startswith("desktop"):
        return {
            **PROFILES[profile],
        }

    device = PROFILES[profile]["device"]

    return {
        **playwright.devices[device],
    }