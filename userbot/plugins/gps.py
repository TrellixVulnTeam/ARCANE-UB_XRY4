from geopy.geocoders import Nominatim
from telethon.tl import types

from userbot import CMD_HELP
from userbot.utils import lightning_cmd


@borg.on(lightning_cmd(pattern="gps ?(.*)"))
async def gps(event):
    if event.fwd_from:
        return
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    input_str = event.pattern_match.group(1)

    if not input_str:
        return await event.edit("what should i find give me location.")

    await event.edit("finding")

    geolocator = Nominatim(user_agent="Arcane")
    geoloc = geolocator.geocode(input_str)

    if geoloc:
        lon = geoloc.longitude
        lat = geoloc.latitude
        await reply_to_id.reply(
            input_str, file=types.InputMediaGeoPoint(types.InputGeoPoint(lat, lon))
        )
        await event.delete()
    else:
        await event.edit("i coudn't find it")


CMD_HELP.update(
    {
        "gps": "`.gps` <location name> :\
      \nUSAGE: sends you the given location name\
      "
    }
)
