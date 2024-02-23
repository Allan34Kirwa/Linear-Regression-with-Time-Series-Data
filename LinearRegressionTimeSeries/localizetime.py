# DatetimeIndex for df is localized to the correct timezone, "Africa/Nairobi
from myFunction import df
import pytz
df = df.index.tz_localize("UTC").tz_convert("Africa/Nairobi")