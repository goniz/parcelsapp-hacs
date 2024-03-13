from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

DOMAIN = "parcelsapp"

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    # Here you could set up API connection and fetch initial data
    hass.data.setdefault(DOMAIN, {})
    # Example: hass.data[DOMAIN]["api"] = YourApiClass(entry.data)
    return True
