"""
Egg, Inc. MCP Server

An MCP (Model Context Protocol) server that exposes Egg, Inc. game data
as tools, inspired by wasmegg-carpet.netlify.app companion tools.

Tools:
  - get_player_overview: Player profile, earning bonus, farmer role
  - get_contracts: Active contracts with coop status and progress
  - get_coop_status: Detailed coop status for a specific contract/coop
  - get_artifact_inventory: Full artifact inventory
  - get_equipped_artifacts: Currently equipped artifact loadouts
  - get_rocket_missions: Active/historical rocket missions
  - get_epic_research: Epic research levels
  - get_earnings_bonus: Detailed earning bonus breakdown
  - get_game_stats: Egg totals, prestiges, drone takedowns, etc.
"""

import base64
import math
import re
import sys
import os

import requests
from mcp.server.fastmcp import FastMCP

# Add the ei-api directory to path for proto imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from proto.gen import ei_pb2

# ── Constants ──────────────────────────────────────────────────────────

EI_ID_PATTERN = re.compile(r"^EI[0-9]{16}$")

MAP_OOM_FARMER_ROLE = {
    0: "Farmer", 1: "Farmer II", 2: "Farmer III",
    3: "Kilofarmer", 4: "Kilofarmer II", 5: "Kilofarmer III",
    6: "Megafarmer", 7: "Megafarmer II", 8: "Megafarmer III",
    9: "Gigafarmer", 10: "Gigafarmer II", 11: "Gigafarmer III",
    12: "Terafarmer", 13: "Terafarmer II", 14: "Terafarmer III",
    15: "Petafarmer", 16: "Petafarmer II", 17: "Petafarmer III",
    18: "Exafarmer", 19: "Exafarmer II", 20: "Exafarmer III",
    21: "Zettafarmer", 22: "Zettafarmer II", 23: "Zettafarmer III",
    24: "Yottafarmer", 25: "Yottafarmer II", 26: "Yottafarmer III",
    27: "Xennafarmer", 28: "Xennafarmer II", 29: "Xennafarmer III",
    30: "Weccafarmer", 31: "Weccafarmer II", 32: "Weccafarmer III",
    33: "Vendafarmer", 34: "Vendafarmer II", 35: "Vendafarmer III",
    36: "Uadafarmer", 37: "Uadafarmer II", 38: "Uadafarmer III",
    39: "Treidafarmer", 40: "Treidafarmer II", 41: "Treidafarmer III",
    42: "Quadafarmer", 43: "Quadafarmer II", 44: "Quadafarmer III",
    45: "Pendafarmer", 46: "Pendafarmer II", 47: "Pendafarmer III",
    48: "Exedafarmer", 49: "Exedafarmer II", 50: "Exedafarmer III",
    51: "Infinifarmer",
}

SPACESHIP_NAMES = {
    0: "Chicken One", 1: "Chicken Nine", 2: "Chicken Heavy",
    3: "BCR", 4: "Millennium Chicken", 5: "Corellihen Corvette",
    6: "Galeggtica", 7: "Chickfiant", 8: "Voyegger",
    9: "Henerprise", 10: "Atreggies",
}

MISSION_STATUS_NAMES = {
    0: "Fueling", 5: "Preparing to Launch", 10: "Exploring",
    15: "Returned", 16: "Analyzing", 20: "Complete",
    25: "Archived", 30: "Aborted",
}

MISSION_DURATION_NAMES = {
    0: "Short", 1: "Long", 2: "Epic", 3: "Tutorial",
}

ARTIFACT_NAMES = {
    0: "Lunar Totem", 3: "Neodymium Medallion", 4: "Beak of Midas",
    5: "Light of Eggendil", 6: "Demeter's Necklace", 7: "Vial of Martian Dust",
    8: "Ornate Gusset", 9: "The Chalice", 10: "Book of Basan",
    11: "Phoenix Feather", 12: "Tungsten Ankh", 21: "Aurelian Brooch",
    22: "Carved Rainstick", 23: "Puzzle Cube", 24: "Quantum Metronome",
    25: "Ship in a Bottle", 26: "Tachyon Deflector", 27: "Interstellar Compass",
    28: "Dilithium Monocle", 29: "Titanium Actuator", 30: "Mercury's Lens",
    1: "Tachyon Stone", 31: "Dilithium Stone", 32: "Shell Stone",
    33: "Lunar Stone", 34: "Soul Stone", 39: "Prophecy Stone",
    36: "Quantum Stone", 37: "Terra Stone", 38: "Life Stone",
    40: "Clarity Stone",
    13: "Extraterrestrial Aluminum", 14: "Ancient Tungsten",
    15: "Space Rocks", 16: "Alien Wood", 17: "Gold Meteorite",
    18: "Tau Ceti Geode", 19: "Centaurian Steel", 20: "Eridani Feather",
    35: "Drone Parts", 41: "Celestial Bronze", 42: "Lalande Hide",
    43: "Solar Titanium",
    2: "Tachyon Stone Fragment", 44: "Dilithium Stone Fragment",
    45: "Shell Stone Fragment", 46: "Lunar Stone Fragment",
    47: "Soul Stone Fragment", 48: "Prophecy Stone Fragment",
    49: "Quantum Stone Fragment", 50: "Terra Stone Fragment",
    51: "Life Stone Fragment", 52: "Clarity Stone Fragment",
}

ARTIFACT_LEVEL_NAMES = {0: "Inferior", 1: "Lesser", 2: "Normal", 3: "Greater", 4: "Superior"}
ARTIFACT_RARITY_NAMES = {0: "Common", 1: "Rare", 2: "Epic", 3: "Legendary"}

EGG_NAMES = {
    1: "Edible", 2: "Superfood", 3: "Medical", 4: "Rocket Fuel",
    5: "Super Material", 6: "Fusion", 7: "Quantum", 8: "Immortality",
    9: "Tachyon", 10: "Graviton", 11: "Dilithium", 12: "Prodigy",
    13: "Terraform", 14: "Antimatter", 15: "Dark Matter", 16: "AI",
    17: "Nebula", 18: "Universe", 19: "Enlightenment",
    50: "Curiosity", 51: "Integrity", 52: "Humility", 53: "Resilience", 54: "Kindness",
    100: "Chocolate", 101: "Easter", 102: "Waterballoon", 103: "Firework", 104: "Pumpkin",
    200: "Custom Egg", 1000: "Unknown",
}

GRADE_NAMES = {0: "Unset", 1: "C", 2: "B", 3: "A", 4: "AA", 5: "AAA"}

# ── API Client ─────────────────────────────────────────────────────────

def _validate_ei_id(ei_id: str) -> str:
    ei_id = ei_id.strip()
    if not EI_ID_PATTERN.match(ei_id):
        raise ValueError(
            f"Invalid Egg Inc ID format: '{ei_id}'. "
            "Must match pattern EI followed by 16 digits (e.g. EI1234567890123456)."
        )
    return ei_id


def _fetch_backup(ei_id: str) -> ei_pb2.Backup:
    ei_id = _validate_ei_id(ei_id)
    req = ei_pb2.EggIncFirstContactRequest()
    req.ei_user_id = ei_id
    req.client_version = 45

    resp = requests.post(
        "https://www.auxbrain.com/ei/bot_first_contact",
        data={"data": base64.b64encode(req.SerializeToString()).decode("utf-8")},
        timeout=15,
    )
    resp.raise_for_status()

    fc_resp = ei_pb2.EggIncFirstContactResponse()
    fc_resp.ParseFromString(base64.b64decode(resp.text))
    if fc_resp.error_message:
        raise ValueError(f"Egg Inc API error: {fc_resp.error_message}")
    return fc_resp.backup



# ── Helpers ────────────────────────────────────────────────────────────

def _format_number(n: float) -> str:
    """Format large numbers with SI suffixes."""
    if n < 1000:
        return f"{n:.2f}" if isinstance(n, float) and n != int(n) else str(int(n))
    suffixes = [
        "", "K", "M", "B", "T", "q", "Q", "s", "S", "o", "N", "d",
        "U", "D", "Td", "qd", "Qd", "sd", "Sd", "Od", "Nd", "V",
        "uV", "dV", "tV", "qV", "QV", "sV", "SV", "OV", "NV",
    ]
    magnitude = int(math.floor(math.log10(abs(n)) / 3))
    magnitude = min(magnitude, len(suffixes) - 1)
    scaled = n / (10 ** (magnitude * 3))
    return f"{scaled:.3f}{suffixes[magnitude]}"


def _get_farmer_role(soul_power: float) -> str:
    oom = int(math.floor(max(soul_power, 0)))
    max_key = max(MAP_OOM_FARMER_ROLE.keys())
    return MAP_OOM_FARMER_ROLE.get(min(oom, max_key), "Unknown")


def _soul_power_from_backup(backup: ei_pb2.Backup) -> float:
    """Calculate soul power (log10 of earning bonus) from backup data."""
    soul_eggs = backup.game.soul_eggs_d or float(backup.game.soul_eggs or 0)
    prophecy_eggs = backup.game.eggs_of_prophecy or 0

    # Find epic research levels
    soul_food_level = 0
    prophecy_bonus_level = 0
    for r in backup.game.epic_research:
        if r.id == "soul_eggs":
            soul_food_level = r.level
        elif r.id == "prophecy_bonus":
            prophecy_bonus_level = r.level

    # Soul Food: each level adds 1% to soul egg bonus (base 10%)
    soul_egg_bonus = 0.10 + 0.01 * soul_food_level

    # Prophecy Bonus: each level adds 0.05% (base 5%)
    prophecy_multiplier = 1.05 + 0.01 * prophecy_bonus_level

    if soul_eggs <= 0:
        return 0.0

    # EB = soul_eggs * soul_egg_bonus * prophecy_multiplier^prophecy_eggs
    eb = soul_eggs * soul_egg_bonus * (prophecy_multiplier ** prophecy_eggs)
    return math.log10(eb) if eb > 0 else 0.0


def _format_artifact_spec(spec) -> dict:
    name_val = spec.name if spec.HasField("name") else 0
    level_val = spec.level if spec.HasField("level") else 0
    rarity_val = spec.rarity if spec.HasField("rarity") else 0
    return {
        "name": ARTIFACT_NAMES.get(name_val, f"Unknown ({name_val})"),
        "level": ARTIFACT_LEVEL_NAMES.get(level_val, f"Unknown ({level_val})"),
        "rarity": ARTIFACT_RARITY_NAMES.get(rarity_val, f"Unknown ({rarity_val})"),
    }


def _format_complete_artifact(complete_artifact) -> dict:
    result = _format_artifact_spec(complete_artifact.spec)
    stones = []
    for stone in complete_artifact.stones:
        stones.append(_format_artifact_spec(stone))
    if stones:
        result["stones"] = stones
    return result


# ── MCP Server ─────────────────────────────────────────────────────────

mcp = FastMCP(
    "Egg Inc.",
    instructions=(
        "This MCP server provides read-only access to Egg, Inc. game data. "
        "All tools require an Egg Inc user ID (format: EI followed by 16 digits, "
        "e.g. EI1234567890123456). Data is fetched live from the Auxbrain game servers."
    ),
)


@mcp.tool()
def get_player_overview(ei_id: str) -> dict:
    """Get a player's overall profile: username, soul eggs, eggs of prophecy,
    earning bonus, farmer role, golden eggs, permit level, and more.
    This is the best starting point for understanding a player's progress."""
    backup = _fetch_backup(ei_id)
    game = backup.game

    soul_eggs = game.soul_eggs_d or float(game.soul_eggs or 0)
    prophecy_eggs = game.eggs_of_prophecy or 0
    soul_power = _soul_power_from_backup(backup)
    oom = int(math.floor(max(soul_power, 0)))

    # Calculate actual earning bonus
    soul_food_level = 0
    prophecy_bonus_level = 0
    for r in game.epic_research:
        if r.id == "soul_eggs":
            soul_food_level = r.level
        elif r.id == "prophecy_bonus":
            prophecy_bonus_level = r.level

    soul_egg_bonus = 0.10 + 0.01 * soul_food_level
    prophecy_multiplier = 1.05 + 0.01 * prophecy_bonus_level
    earning_bonus = soul_eggs * soul_egg_bonus * (prophecy_multiplier ** prophecy_eggs)

    permit_names = {0: "Standard", 1: "Pro", 2: "Ultra"}

    return {
        "username": backup.user_name,
        "ei_id": backup.ei_user_id,
        "soul_eggs": _format_number(soul_eggs),
        "soul_eggs_raw": soul_eggs,
        "eggs_of_prophecy": prophecy_eggs,
        "earning_bonus": _format_number(earning_bonus) + "%",
        "earning_bonus_raw": earning_bonus,
        "farmer_role": _get_farmer_role(soul_power),
        "earning_bonus_oom": oom,
        "golden_eggs": (game.golden_eggs_earned or 0) - (game.golden_eggs_spent or 0),
        "golden_eggs_earned": game.golden_eggs_earned or 0,
        "golden_eggs_spent": game.golden_eggs_spent or 0,
        "shell_scripts": (game.shell_scripts_earned or 0) - (game.shell_scripts_spent or 0),
        "permit_level": permit_names.get(game.permit_level, f"Unknown ({game.permit_level})"),
        "hyperloop_station": game.hyperloop_station,
        "piggy_bank": game.piggy_bank or 0,
        "prestiges": backup.stats.num_prestiges or 0,
        "drone_takedowns": backup.stats.drone_takedowns or 0,
        "drone_takedowns_elite": backup.stats.drone_takedowns_elite or 0,
        "current_egg": EGG_NAMES.get(backup.sim.egg_type, "Unknown"),
        "max_egg_reached": EGG_NAMES.get(game.max_egg_reached, "Unknown"),
        "fuel_tank_level": backup.artifacts.tank_level or 0,
        "crafting_xp": backup.artifacts.crafting_xp or 0,
    }


@mcp.tool()
def get_contracts(ei_id: str) -> dict:
    """Get a player's active contracts with coop status, goals, and progress.
    Shows contract details, contributor lists, eggs laid, time remaining, and grade."""
    backup = _fetch_backup(ei_id)

    coop_lookup = {
        coop.coop_identifier: coop
        for coop in backup.contracts.current_coop_statuses
    }

    contracts = []
    for lc in backup.contracts.contracts:
        contract = lc.contract
        coop_id = lc.coop_identifier or None

        # Get goals for the player's grade
        grade = lc.grade if lc.HasField("grade") else 0
        goals = []
        if contract.grade_specs:
            for gs in contract.grade_specs:
                if gs.grade == grade:
                    for g in gs.goals:
                        goals.append({
                            "target": _format_number(g.target_amount),
                            "target_raw": g.target_amount,
                            "reward_type": ei_pb2.RewardType.Name(g.reward_type) if g.HasField("reward_type") else "Unknown",
                            "reward_amount": g.reward_amount,
                        })
                    break
        if not goals:
            for g in contract.goals:
                goals.append({
                    "target": _format_number(g.target_amount),
                    "target_raw": g.target_amount,
                    "reward_type": ei_pb2.RewardType.Name(g.reward_type) if g.HasField("reward_type") else "Unknown",
                    "reward_amount": g.reward_amount,
                })

        # Coop info
        contributors = []
        coop_total = None
        coop_grade = None
        seconds_remaining = None
        all_goals_achieved = False

        if coop_id and coop_id in coop_lookup:
            coop = coop_lookup[coop_id]
            coop_total = coop.total_amount
            coop_grade = GRADE_NAMES.get(coop.grade, None)
            seconds_remaining = coop.seconds_remaining
            all_goals_achieved = coop.all_goals_achieved

            for c in coop.contributors:
                sp = c.soul_power if c.HasField("soul_power") else 0
                contributors.append({
                    "name": c.user_name,
                    "eggs_laid": _format_number(c.contribution_amount),
                    "eggs_laid_raw": c.contribution_amount,
                    "eggs_per_hour": _format_number(c.contribution_rate * 3600),
                    "eggs_per_hour_raw": c.contribution_rate * 3600,
                    "farmer_role": _get_farmer_role(sp),
                    "earning_bonus_oom": int(math.floor(max(sp, 0))),
                    "boost_tokens": c.boost_tokens,
                    "boost_tokens_spent": c.boost_tokens_spent,
                    "active": c.active,
                    "time_cheat_detected": c.time_cheat_detected,
                    "leech": c.leech,
                })

        custom_egg_id = contract.custom_egg_id if contract.HasField("custom_egg_id") else ""
        leggacy = contract.leggacy or contract.name.startswith("LEGGACY")

        contracts.append({
            "contract_id": contract.identifier,
            "contract_name": contract.name,
            "description": contract.description,
            "egg_type": EGG_NAMES.get(contract.egg, "Unknown"),
            "custom_egg_id": custom_egg_id or None,
            "leggacy": leggacy,
            "coop_allowed": contract.coop_allowed,
            "max_coop_size": contract.max_coop_size,
            "coop_id": coop_id,
            "grade": GRADE_NAMES.get(grade, "Unset"),
            "coop_grade": coop_grade,
            "goals": goals,
            "total_eggs_laid": _format_number(coop_total) if coop_total else None,
            "total_eggs_laid_raw": coop_total,
            "all_goals_achieved": all_goals_achieved,
            "seconds_remaining": seconds_remaining,
            "hours_remaining": round(seconds_remaining / 3600, 1) if seconds_remaining else None,
            "num_contributors": len(contributors),
            "contributors": contributors,
            "contract_length_seconds": contract.length_seconds,
            "boost_token_timer_minutes": contract.minutes_per_token,
        })

    # Contract grade info
    cpi = backup.contracts.last_cpi
    grade_info = None
    if cpi and cpi.HasField("grade"):
        grade_info = {
            "grade": GRADE_NAMES.get(cpi.grade, "Unknown"),
            "total_cxp": cpi.total_cxp,
            "season_cxp": cpi.season_cxp,
            "grade_score": cpi.grade_score,
            "target_grade_score": cpi.target_grade_score,
            "grade_progress": cpi.grade_progress,
        }

    return {
        "ei_id": ei_id,
        "contract_count": len(contracts),
        "player_grade_info": grade_info,
        "contracts": contracts,
    }


@mcp.tool()
def get_coop_status(ei_id: str, contract_id: str) -> dict:
    """Get detailed coop status for a specific contract the player is in.
    Shows contributors, eggs laid, time remaining, goals achieved, gifts, and chicken runs.
    The contract_id should match one of the player's active contracts (use get_contracts to find them)."""
    backup = _fetch_backup(ei_id)

    # Find the matching coop status from the player's backup
    coop = None
    for status in backup.contracts.current_coop_statuses:
        if status.contract_identifier == contract_id:
            coop = status
            break

    if coop is None:
        # Also check if the contract exists at all in their active contracts
        active_ids = [lc.contract.identifier for lc in backup.contracts.contracts if lc.contract]
        return {
            "error": f"No coop found for contract '{contract_id}'. "
                     f"Player's active contracts: {active_ids}",
        }

    contributors = []
    for c in coop.contributors:
        sp = c.soul_power if c.HasField("soul_power") else 0
        contributors.append({
            "name": c.user_name,
            "eggs_laid": _format_number(c.contribution_amount),
            "eggs_laid_raw": c.contribution_amount,
            "eggs_per_hour": _format_number(c.contribution_rate * 3600),
            "eggs_per_hour_raw": c.contribution_rate * 3600,
            "farmer_role": _get_farmer_role(sp),
            "earning_bonus_oom": int(math.floor(max(sp, 0))),
            "boost_tokens": c.boost_tokens,
            "boost_tokens_spent": c.boost_tokens_spent,
            "active": c.active,
            "recently_active": c.recently_active,
            "leech": c.leech,
            "time_cheat_detected": c.time_cheat_detected,
            "platform": "iOS" if c.platform == 1 else "Android" if c.platform == 2 else "Unknown",
        })

    gifts = []
    for g in coop.gifts:
        gifts.append({
            "from": g.user_name,
            "tokens": g.amount,
        })

    chicken_runs = []
    for cr in coop.chicken_runs:
        chicken_runs.append({
            "from": cr.user_name,
            "chickens": cr.amount,
        })

    return {
        "ei_id": ei_id,
        "contract_id": coop.contract_identifier,
        "coop_id": coop.coop_identifier,
        "grade": GRADE_NAMES.get(coop.grade, "Unset"),
        "total_eggs_laid": _format_number(coop.total_amount),
        "total_eggs_laid_raw": coop.total_amount,
        "all_goals_achieved": coop.all_goals_achieved,
        "seconds_remaining": coop.seconds_remaining,
        "hours_remaining": round(coop.seconds_remaining / 3600, 1) if coop.seconds_remaining else None,
        "public": coop.public,
        "auto_generated": coop.auto_generated,
        "all_members_reporting": coop.all_members_reporting,
        "num_contributors": len(contributors),
        "contributors": contributors,
        "gifts": gifts,
        "chicken_runs": chicken_runs,
    }


@mcp.tool()
def get_artifact_inventory(ei_id: str) -> dict:
    """Get a player's full artifact inventory - every artifact, stone, ingredient,
    and stone fragment they own, with quantities and details.
    Similar to the wasmegg Inventory Visualizer."""
    backup = _fetch_backup(ei_id)
    db = backup.artifacts_db

    inventory = []
    for item in db.inventory_items:
        artifact = _format_complete_artifact(item.artifact)
        artifact["item_id"] = item.item_id
        artifact["quantity"] = item.quantity or 1
        inventory.append(artifact)

    # Discovered/craftable status
    artifact_status = []
    for s in db.artifact_status:
        spec = _format_artifact_spec(s.spec)
        spec["discovered"] = s.discovered
        spec["craftable"] = s.craftable
        spec["recipe_discovered"] = s.recipe_discovered
        spec["count"] = s.count
        artifact_status.append(spec)

    return {
        "ei_id": ei_id,
        "inventory_count": len(inventory),
        "inventory": inventory,
        "crafting_xp": backup.artifacts.crafting_xp or 0,
        "artifact_discovery_status": artifact_status,
    }


@mcp.tool()
def get_equipped_artifacts(ei_id: str) -> dict:
    """Get a player's currently equipped artifact loadouts.
    Shows which artifacts are active in each artifact set slot."""
    backup = _fetch_backup(ei_id)
    db = backup.artifacts_db

    # Build item lookup
    item_lookup = {item.item_id: item for item in db.inventory_items}

    artifact_sets = []
    for i, artifact_set in enumerate(db.active_artifact_sets):
        slots = []
        for slot in artifact_set.slots:
            if slot.occupied and slot.item_id in item_lookup:
                item = item_lookup[slot.item_id]
                slots.append(_format_complete_artifact(item.artifact))
            else:
                slots.append(None)
        artifact_sets.append({
            "set_index": i,
            "slots": slots,
        })

    # Saved sets
    saved_sets = []
    for i, saved_set in enumerate(db.saved_artifact_sets):
        slots = []
        for slot in saved_set.slots:
            if slot.occupied and slot.item_id in item_lookup:
                item = item_lookup[slot.item_id]
                slots.append(_format_complete_artifact(item.artifact))
            else:
                slots.append(None)
        saved_sets.append({
            "set_index": i,
            "slots": slots,
        })

    return {
        "ei_id": ei_id,
        "active_sets": artifact_sets,
        "saved_sets": saved_sets,
    }


@mcp.tool()
def get_rocket_missions(ei_id: str) -> dict:
    """Get a player's rocket mission data: currently active missions being fueled
    or exploring, plus historical mission archive with launch counts.
    Similar to the wasmegg Rockets Tracker."""
    backup = _fetch_backup(ei_id)
    db = backup.artifacts_db

    def _format_mission(m):
        ship = m.ship if m.HasField("ship") else 0
        status = m.status if m.HasField("status") else 0
        dur = m.duration_type if m.HasField("duration_type") else 0

        fuel_info = []
        for f in m.fuel:
            fuel_info.append({
                "egg": EGG_NAMES.get(f.egg, "Unknown"),
                "amount": _format_number(f.amount),
                "amount_raw": f.amount,
            })

        target = None
        if m.HasField("target_artifact"):
            target = ARTIFACT_NAMES.get(m.target_artifact, f"Unknown ({m.target_artifact})")

        return {
            "ship": SPACESHIP_NAMES.get(ship, f"Unknown ({ship})"),
            "status": MISSION_STATUS_NAMES.get(status, f"Unknown ({status})"),
            "duration_type": MISSION_DURATION_NAMES.get(dur, f"Unknown ({dur})"),
            "duration_seconds": m.duration_seconds,
            "capacity": m.capacity,
            "level": m.level,
            "seconds_remaining": m.seconds_remaining if m.HasField("seconds_remaining") else None,
            "target_artifact": target,
            "fuel": fuel_info,
            "identifier": m.identifier,
        }

    # Currently fueling mission
    fueling = None
    if db.HasField("fueling_mission"):
        fueling = _format_mission(db.fueling_mission)

    # Active missions (exploring/returned)
    active = [_format_mission(m) for m in db.mission_infos]

    # Archive stats
    archive_count = len(db.mission_archive)
    ship_counts = {}
    for m in db.mission_archive:
        ship = m.ship if m.HasField("ship") else 0
        ship_name = SPACESHIP_NAMES.get(ship, f"Unknown ({ship})")
        ship_counts[ship_name] = ship_counts.get(ship_name, 0) + 1

    # Launch counts from client info in artifacts
    fuel_tank_level = backup.artifacts.tank_level or 0
    tank_fuels = list(backup.artifacts.tank_fuels)
    tank_limits = list(backup.artifacts.tank_limits)

    fuel_tank = []
    for i, (fuel, limit) in enumerate(zip(tank_fuels, tank_limits)):
        egg_id = i + 1  # egg IDs start at 1
        fuel_tank.append({
            "egg": EGG_NAMES.get(egg_id, f"Egg {egg_id}"),
            "stored": _format_number(fuel),
            "stored_raw": fuel,
            "capacity": _format_number(limit),
            "capacity_raw": limit,
            "percent_full": round(fuel / limit * 100, 1) if limit > 0 else 0,
        })

    return {
        "ei_id": ei_id,
        "fueling_mission": fueling,
        "active_missions": active,
        "active_mission_count": len(active),
        "total_missions_completed": archive_count,
        "missions_by_ship": ship_counts,
        "fuel_tank_level": fuel_tank_level,
        "fuel_tank": fuel_tank,
    }


@mcp.tool()
def get_epic_research(ei_id: str) -> dict:
    """Get a player's epic research levels - every epic research item and its
    current level. Useful for understanding a player's permanent upgrades."""
    backup = _fetch_backup(ei_id)

    EPIC_RESEARCH_NAMES = {
        "hold_to_hatch": "Hold to Hatch",
        "epic_hatchery": "Epic Hatchery",
        "epic_internal_incubators": "Epic Int. Hatcheries",
        "video_doubler_time": "Video Doubler Time",
        "epic_clucking": "Epic Clucking",
        "epic_multiplier": "Epic Multiplier",
        "cheaper_contractors": "Cheaper Contractors",
        "bust_unions": "Bust Unions",
        "cheaper_research": "Lab Upgrade",
        "silo_capacity": "Silo Capacity",
        "int_hatch_sharing": "Internal Hatchery Sharing",
        "int_hatch_calm": "Internal Hatchery Calm",
        "accounting_tricks": "Accounting Tricks",
        "hold_to_research": "Hold to Research",
        "soul_eggs": "Soul Food",
        "prestige_bonus": "Prestige Bonus",
        "drone_rewards": "Drone Rewards",
        "epic_egg_laying": "Epic Comfy Nests",
        "transportation_lobbyist": "Transportation Lobbyists",
        "prophecy_bonus": "Prophecy Bonus",
        "afx_mission_time": "FTL Drive Upgrades",
        "afx_mission_capacity": "Zero-g Quantum Containment",
    }

    EPIC_RESEARCH_MAX = {
        "hold_to_hatch": 15, "epic_hatchery": 20, "epic_internal_incubators": 20,
        "video_doubler_time": 10, "epic_clucking": 5, "epic_multiplier": 100,
        "cheaper_contractors": 10, "bust_unions": 20, "cheaper_research": 20,
        "silo_capacity": 20, "int_hatch_sharing": 10, "int_hatch_calm": 20,
        "accounting_tricks": 10, "hold_to_research": 10, "soul_eggs": 140,
        "prestige_bonus": 20, "drone_rewards": 25, "epic_egg_laying": 20,
        "transportation_lobbyist": 30, "prophecy_bonus": 5,
        "afx_mission_time": 60, "afx_mission_capacity": 25,
    }

    research = {}
    for r in backup.game.epic_research:
        max_level = EPIC_RESEARCH_MAX.get(r.id, "?")
        research[r.id] = {
            "name": EPIC_RESEARCH_NAMES.get(r.id, r.id),
            "level": r.level,
            "max_level": max_level,
            "maxed": r.level >= max_level if isinstance(max_level, int) else False,
        }

    return {
        "ei_id": ei_id,
        "research": research,
    }


@mcp.tool()
def get_earnings_bonus(ei_id: str) -> dict:
    """Get a detailed breakdown of a player's Earning Bonus calculation.
    Shows soul eggs, eggs of prophecy, Soul Food level, Prophecy Bonus level,
    and the step-by-step EB calculation. Essential for understanding player power."""
    backup = _fetch_backup(ei_id)
    game = backup.game

    soul_eggs = game.soul_eggs_d or float(game.soul_eggs or 0)
    prophecy_eggs = game.eggs_of_prophecy or 0

    soul_food_level = 0
    prophecy_bonus_level = 0
    for r in game.epic_research:
        if r.id == "soul_eggs":
            soul_food_level = r.level
        elif r.id == "prophecy_bonus":
            prophecy_bonus_level = r.level

    # Soul Food: base 10% + 1% per level
    soul_egg_bonus_per_se = 0.10 + 0.01 * soul_food_level

    # Prophecy Bonus: base 1.05 + 0.01 per level
    prophecy_multiplier = 1.05 + 0.01 * prophecy_bonus_level

    # Prophecy effect
    prophecy_effect = prophecy_multiplier ** prophecy_eggs

    # Total EB
    earning_bonus = soul_eggs * soul_egg_bonus_per_se * prophecy_effect

    return {
        "ei_id": ei_id,
        "soul_eggs": _format_number(soul_eggs),
        "soul_eggs_raw": soul_eggs,
        "eggs_of_prophecy": prophecy_eggs,
        "soul_food_level": soul_food_level,
        "soul_food_max": 140,
        "soul_egg_bonus_per_se": f"{soul_egg_bonus_per_se * 100:.0f}%",
        "prophecy_bonus_level": prophecy_bonus_level,
        "prophecy_bonus_max": 5,
        "prophecy_multiplier_per_pe": f"{prophecy_multiplier:.2f}x",
        "prophecy_total_multiplier": f"{_format_number(prophecy_effect)}x",
        "earning_bonus": _format_number(earning_bonus) + "%",
        "earning_bonus_raw": earning_bonus,
        "farmer_role": _get_farmer_role(math.log10(earning_bonus) if earning_bonus > 0 else 0),
        "earning_bonus_oom": int(math.floor(math.log10(earning_bonus))) if earning_bonus > 0 else 0,
        "formula": (
            f"EB = {_format_number(soul_eggs)} SE "
            f"x {soul_egg_bonus_per_se * 100:.0f}% per SE "
            f"x {prophecy_multiplier:.2f}^{prophecy_eggs} PE "
            f"= {_format_number(earning_bonus)}%"
        ),
    }


@mcp.tool()
def get_game_stats(ei_id: str) -> dict:
    """Get a player's game statistics: total eggs laid by type, prestige count,
    drone takedowns, boosts used, piggy bank data, and more."""
    backup = _fetch_backup(ei_id)
    stats = backup.stats

    egg_totals_list = list(stats.egg_totals)
    egg_totals_len = len(egg_totals_list)

    egg_counts = []

    # Standard Eggs (indices 0-18 -> IDs 1-19)
    for i in range(min(19, egg_totals_len)):
        egg_id = i + 1
        egg_counts.append({
            "egg_type": EGG_NAMES.get(egg_id, f"Unknown ({egg_id})"),
            "egg_id": egg_id,
            "count": _format_number(egg_totals_list[i]),
            "count_raw": egg_totals_list[i],
        })

    # Special Eggs (indices 20-24 -> IDs 50-54)
    for i in range(20, min(25, egg_totals_len)):
        egg_id = i + 30
        egg_counts.append({
            "egg_type": EGG_NAMES.get(egg_id, f"Unknown ({egg_id})"),
            "egg_id": egg_id,
            "count": _format_number(egg_totals_list[i]),
            "count_raw": egg_totals_list[i],
        })

    # Contract/Holiday eggs from contract data
    all_contracts = list(backup.contracts.contracts or []) + list(backup.contracts.archive or [])
    contract_only_eggs = [100, 101, 102, 103, 104]  # Chocolate, Easter, Waterballoon, Firework, Pumpkin

    for egg_id in contract_only_eggs:
        total = 0.0
        for c in all_contracts:
            if c.contract and c.contract.egg == egg_id and not c.contract.HasField("custom_egg_id"):
                total += (
                    getattr(c, "coop_last_uploaded_contribution", None) or
                    getattr(c, "last_amount_when_reward_given", None) or
                    0.0
                )
        egg_counts.append({
            "egg_type": EGG_NAMES.get(egg_id, f"Unknown ({egg_id})"),
            "egg_id": egg_id,
            "count": _format_number(total),
            "count_raw": total,
        })

    # Custom eggs
    custom_totals = {}
    for lc in all_contracts:
        if not lc.contract:
            continue
        if lc.contract.HasField("custom_egg_id") and lc.contract.custom_egg_id:
            custom_id = lc.contract.custom_egg_id.strip()
            if custom_id:
                contribution = (
                    getattr(lc, "coop_last_uploaded_contribution", None) or
                    getattr(lc, "last_amount_when_reward_given", None) or
                    0.0
                )
                custom_totals[custom_id] = custom_totals.get(custom_id, 0.0) + contribution

    for custom_id, total in custom_totals.items():
        egg_counts.append({
            "egg_type": f"Custom: {custom_id}",
            "egg_id": "custom",
            "count": _format_number(total),
            "count_raw": total,
        })

    # Trophies / medals
    medal_names = {0: "None", 1: "Bronze", 2: "Silver", 3: "Gold", 4: "Platinum", 5: "Diamond"}
    trophies = []
    for i, level in enumerate(backup.game.egg_medal_level):
        egg_id = i + 1
        if level > 0:
            trophies.append({
                "egg": EGG_NAMES.get(egg_id, f"Unknown ({egg_id})"),
                "medal": medal_names.get(level, f"Level {level}"),
            })

    return {
        "ei_id": ei_id,
        "egg_counts": egg_counts,
        "trophies": trophies,
        "prestiges": stats.num_prestiges or 0,
        "boosts_used": stats.boosts_used or 0,
        "video_doubler_uses": stats.video_doubler_uses or 0,
        "drone_takedowns": stats.drone_takedowns or 0,
        "drone_takedowns_elite": stats.drone_takedowns_elite or 0,
        "piggy_bank_breaks": stats.num_piggy_breaks or 0,
        "iap_packs_purchased": stats.iap_packs_purchased or 0,
    }


def main():
    mcp.run()


if __name__ == "__main__":
    main()
