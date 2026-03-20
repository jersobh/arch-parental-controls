"""Shared constants used across the application."""

import os as _os

APP_ID = "org.archparentalcontrols.ParentalControls"
APP_NAME = "Arch Parental Controls"
APP_VERSION = "1.0.0"
APP_DEVELOPER = "Arch Linux Community"
APP_WEBSITE = "https://github.com/jersobh/arch-parental-controls"
APP_ISSUE_URL = "https://github.com/jersobh/arch-parental-controls/issues"

SUPERVISED_GROUP = "supervised"
MIN_HUMAN_UID = 1000

GROUP_HELPER = "/usr/lib/arch-parental-controls/group-helper"
GETTEXT_DOMAIN = "arch-parental-controls"

# Resolve locale dir — prefer local compiled .mo files during development
_INSTALLED_LOCALE = "/usr/share/locale"
_LOCAL_LOCALE = _os.path.normpath(
    _os.path.join(_os.path.dirname(__file__), "..", "..", "..",
                  "data-files", "usr", "share", "locale")
)
LOCALE_DIR = (
    _LOCAL_LOCALE
    if _os.path.isdir(_LOCAL_LOCALE)
    else _INSTALLED_LOCALE
)

# Data paths — root-owned, not user-writable
DATA_DIR = "/var/lib/arch-parental-controls"
ACTIVITY_DIR = f"{DATA_DIR}/activity"
TIME_LIMITS_FILE = f"{DATA_DIR}/time-limits.json"
ACL_STATE_FILE = f"{DATA_DIR}/acl-blocks.json"
DNS_CONFIG_DIR = "/etc/arch-parental-controls/dns"

# Polkit
POLKIT_RULES_DIR = "/etc/polkit-1/rules.d"
POLKIT_RULES_FILE = f"{POLKIT_RULES_DIR}/50-arch-parental-controls.rules"

# UI — resolve to local data/ dir during development, installed path otherwise
_INSTALLED_RESOURCE = "/usr/share/arch-parental-controls"
_LOCAL_RESOURCE = _os.path.join(_os.path.dirname(__file__), "..", "data")
RESOURCE_BASE = (
    _LOCAL_RESOURCE
    if _os.path.isdir(_LOCAL_RESOURCE)
    else _INSTALLED_RESOURCE
)

# Age groups with labels — used in user creation
AGE_GROUPS: dict[str, tuple[str, int]] = {
    "child": ("child", 7),
    "preteen": ("preteen", 10),
    "teen": ("teen", 13),
    "young-adult": ("young-adult", 16),
}

# DNS providers
DNS_PROVIDERS: dict[str, dict[str, str]] = {
    "cleanbrowsing": {
        "name": "CleanBrowsing Family Filter",
        "dns1": "185.228.168.168",
        "dns2": "185.228.169.168",
    },
    "opendns": {
        "name": "OpenDNS FamilyShield",
        "dns1": "208.67.222.123",
        "dns2": "208.67.220.123",
    },
    "cloudflare": {
        "name": "Cloudflare for Families",
        "dns1": "1.1.1.3",
        "dns2": "1.0.0.3",
    },
}

# Default supervised blocks (package managers, network tools)
DEFAULT_SUPERVISED_BLOCKS: list[str] = [
    "/usr/bin/pamac-manager",
    "/usr/bin/pamac-installer",
    "/usr/bin/pamac-daemon",
    "/usr/bin/yay",
    "/usr/bin/paru",
    "/usr/bin/flatpak",
    "/usr/bin/snap",
    "/usr/bin/docker",
    "/usr/bin/podman",
    "/usr/bin/curl",
    "/usr/bin/wget",
    "/usr/bin/ssh",
]
