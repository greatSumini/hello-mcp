"""Server state management for ChillMCP."""

import time
from dataclasses import dataclass


@dataclass
class ServerState:
    """Manages the state of the ChillMCP server."""

    stress_level: int
    boss_alert_level: int
    last_stress_update_time: float
    last_boss_cooldown_time: float
    boss_alertness: int  # CLI parameter: probability (0-100) of boss alert increasing
    boss_alertness_cooldown: int  # CLI parameter: cooldown period in seconds

    @classmethod
    def create(
        cls, boss_alertness: int = 50, boss_alertness_cooldown: int = 300
    ) -> "ServerState":
        """Create a new ServerState with default initial values."""
        current_time = time.time()
        return cls(
            stress_level=0,
            boss_alert_level=0,
            last_stress_update_time=current_time,
            last_boss_cooldown_time=current_time,
            boss_alertness=boss_alertness,
            boss_alertness_cooldown=boss_alertness_cooldown,
        )
