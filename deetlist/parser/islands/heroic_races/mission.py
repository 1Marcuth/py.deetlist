from pydantic import validate_arguments
from parsel import Selector

from ....utils.time_parser import parse_spawn_time

class MissionParser:
    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    def __init__(self, selector: Selector) -> None:
        self.__selector = selector

    @property
    def goal_points(self) -> int:
        goal_points = int(self.__selector.css(".mz:nth-child(1) .m2::text").get())
        return goal_points

    @property
    def pool_size(self) -> int:
        pool_size = int(self.__selector.css(".mz:nth-child(2) .m2::text").get())
        return pool_size

    @property
    def spawn_time(self) -> int:
        spawn_time_for_one = parse_spawn_time(self.__selector.css(".mz:nth-child(3) .m2::text").get())
        spawn_time_for_all = parse_spawn_time(self.__selector.css(".mz:nth-child(5) .m2::text").get())

        return dict(
            one = spawn_time_for_one,
            all = spawn_time_for_all
        )

    @property
    def spawn_chance(self) -> float:
        spawn_chance = int(self.__selector.css(".mz:nth-child(4) .m2::text").get().removesuffix("%")) / 100
        return spawn_chance

    def get(self) -> dict:
        return dict(
            goal_points = self.goal_points,
            pool_size = self.pool_size,
            spawn_time = self.spawn_time,
            spawn_chance = self.spawn_chance
        )

__all__ = [ "MissionParser" ]