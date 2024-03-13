import logging
from homeassistant.helpers.entity import Entity
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, entry, async_add_entities):
    # Assuming your API client is set up in __init__.py and has a method to get parcels
    parcels = await hass.data[DOMAIN]["api"].get_parcels()
    sensors = [ParcelSensor(parcel) for parcel in parcels]
    async_add_entities(sensors, True)

class ParcelSensor(Entity):
    def __init__(self, parcel):
        self._parcel = parcel
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"Parcel {self._parcel['tracking_id']}"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    async def async_update(self):
        """Fetch new state data for the sensor."""
        try:
            status = await hass.data[DOMAIN]["api"].get_parcel_status(self._parcel["tracking_id"])
            self._state = status["state"]
        except Exception as e:
            _LOGGER.error("Error updating parcel sensor: %s", e)
