# Name convention: profile name should start from "desktop_", "tablet_", "mobile_"

from __future__ import annotations

from typing import TypeAlias, cast

from playwright.sync_api import Playwright

BrowserContextConfig: TypeAlias = dict[str, object]
ProfileConfig: TypeAlias = dict[str, object]

PROFILES: dict[str, ProfileConfig] = {
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


def get_profile(playwright: Playwright, profile: str) -> BrowserContextConfig:
    if is_desktop(profile):
        return cast(BrowserContextConfig, dict(PROFILES[profile]))

    device = cast(str, PROFILES[profile]["device"])

    return cast(BrowserContextConfig, dict(playwright.devices[device]))


def is_desktop(profile: str) -> bool:
    return profile.startswith("desktop")
