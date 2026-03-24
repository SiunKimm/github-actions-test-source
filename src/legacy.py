"""Legacy utilities - scheduled for removal."""


def old_handler():
    """Handle legacy requests."""
    return {"status": "ok", "version": "legacy"}


def deprecated_parser(data):
    """Parse data using old format."""
    return data.split(",")
