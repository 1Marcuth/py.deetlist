from pydantic import validate_arguments
from datetime import datetime

from ..settings import SECONDS_PER_DAY, SECONDS_PER_HOUR, SECONDS_PER_MINUTE, MINUTES_PER_HOUR

@validate_arguments
def parse_attack_training_time(raw_time: str) -> int:
    if "hours" in raw_time:
        if raw_time == "24 hours":
            return 24 * SECONDS_PER_HOUR

        hours = datetime.strptime(raw_time, "%H hours").hour

        return hours * SECONDS_PER_HOUR
        
    elif "days" in raw_time:
        days = datetime.strptime(raw_time, "%d days").day

        return days * SECONDS_PER_DAY

    else:
        raise Exception("Valor inesperado em TimeParser > training_time")

@validate_arguments
def parse_summon_time(raw_time: str) -> int:
    time = raw_time.split("(")[1].strip().removesuffix(")")

    if "Hours" in raw_time:
        hours = int(time.removesuffix(" Hours"))
        return hours * SECONDS_PER_HOUR

    elif "hr" in raw_time and "min" in raw_time:

        try:
            times = datetime.strptime(time, "%Hhr %Mmin")
        except:
            times = datetime.strptime(time.split(".")[0], "%Hhr %M")

        hours = times.hour
        minutes = times.minute

        return (minutes * SECONDS_PER_MINUTE) + (hours * SECONDS_PER_HOUR)

    else:
        raise Exception("Valor inesperado em TimeParser > summon_time")

@validate_arguments
def parse_breed_time(raw_time: str) -> int:
    time = raw_time.split("(")[1].strip().removesuffix(")")

    if "Hours" in raw_time:
        hours = int(time.removesuffix(" Hours"))
        return hours * SECONDS_PER_HOUR

    elif "hr" in raw_time and "min" in raw_time:

        try:
            times = datetime.strptime(time, "%Hhr %Mmin")
        except:
            times = datetime.strptime(time.split(".")[0], "%Hhr %M")

        hours = times.hour
        minutes = times.minute

        return (minutes * SECONDS_PER_MINUTE) + (hours * SECONDS_PER_HOUR)

    else:
        raise Exception("Valor inesperado em TimeParser > breed_time")

@validate_arguments
def parse_hatch_time(raw_time: str) -> int:
    time = raw_time.split("(")[1].strip().removesuffix(")")

    if "Hours" in raw_time:
        hours = int(time.removesuffix(" Hours"))
        return hours * SECONDS_PER_HOUR

    elif "hr" in raw_time and "min" in raw_time:

        try:
            times = datetime.strptime(time, "%Hhr %Mmin")
        except:
            times = datetime.strptime(time.split(".")[0], "%Hhr %M")
        
        hours = times.hour
        minutes = times.minute

        return (minutes * SECONDS_PER_MINUTE) + (hours * SECONDS_PER_HOUR)

    else:
        raise Exception("Valor inesperado em TimeParser > hatch_time")

@validate_arguments
def parse_spawn_time(pool_time: str) -> int:
        pool_time = pool_time.lower()

        if pool_time == "instant" or pool_time == "no minimum":
            return 0
        
        if "minutes" in pool_time:
            if "60" in pool_time:
                return 60 * SECONDS_PER_MINUTE
                
            minutes = datetime.strptime(pool_time, "%M minutes").minute
            return minutes * SECONDS_PER_MINUTE

        elif "hours" in pool_time:
            hours = datetime.strptime(pool_time, "%H hours").hour
            return hours * SECONDS_PER_HOUR

        elif "hr" in pool_time and "min" in pool_time:
            hours_and_minutes = datetime.strptime(pool_time, "%Hhr %Mmin")
            hours = hours_and_minutes.hour
            minutes = hours_and_minutes.minute

            return (hours * SECONDS_PER_HOUR) + (minutes * SECONDS_PER_MINUTE)

        elif "day" in pool_time:
            days_and_hours = datetime.strptime(pool_time, "%d day %H hrs")
            days = days_and_hours.day
            hours = days_and_hours.hour
            return (days * SECONDS_PER_DAY) + (hours * MINUTES_PER_HOUR)

__all__ = [
   "parse_attack_training_time",
    "parse_summon_time",
    "parse_breed_time",
    "parse_hatch_time",
    "parse_spawn_time"
]