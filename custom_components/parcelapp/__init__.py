from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

from .const import DOMAIN

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the component from configuration.yaml (if any)."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up a parcel tracking from a config entry."""
    hass.data.setdefault(DOMAIN, {})

    # Perform your setup here, such as setting up API connections
    # and creating entities based on the entry data.
    
    # Example: Load a sensor platform
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    # Unload your platform.
    await hass.config_entries.async_forward_entry_unload(entry, "sensor")

    # Remove the config entry from hass.data if you need to
    # Example: hass.data[DOMAIN].pop(entry.entry_id)

    return True
