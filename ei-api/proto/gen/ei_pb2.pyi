from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

AD_COLONY: AdNetwork
AI: Egg
ALL_TIME: LeaderboardScope
ALL_USERS: UserType
ANTIMATTER: Egg
APPLOVIN: AdNetwork
ARTIFACT: RewardType
ARTIFACTS_ACTIVE: UserType
ARTIFACTS_INACTIVE: UserType
ARTIFACTS_UNLOCKED: UserType
ARTIFACT_CASE: RewardType
BOOST: RewardType
BOOST_SHOP: UILocation
BOOST_TOKEN: RewardType
CASH: RewardType
CHARTBOOST: AdNetwork
CHICKEN: RewardType
CHICKENS: UILocation
CHICKEN_HATS: UILocation
CHOCOLATE: Egg
CONTRACT: FarmType
CONTRACTS_ACTIVE: UserType
CONTRACTS_INACTIVE: UserType
CONTRACTS_UNLOCKED: UserType
CURIOSITY: Egg
CURRENT_SEASON: LeaderboardScope
CUSTOM_EGG: Egg
DARK_MATTER: Egg
DESCRIPTOR: _descriptor.FileDescriptor
DILITHIUM: Egg
DROID: Platform
EASTER: Egg
EDIBLE: Egg
EGGED_UP: UserType
EGGS_LAID: GoalType
EGGS_OF_PROPHECY: RewardType
EMPTY: FarmType
ENLIGHTENMENT: Egg
EPIC_RESEARCH: UILocation
EPIC_RESEARCH_ITEM: RewardType
FACEBOOK: AdNetwork
FIREWORK: Egg
FUEL_TANK_UNLOCKED: UserType
FUSION: Egg
GOLD: RewardType
GRAVITON: Egg
HELP: UILocation
HOME: FarmType
HUMILITY: Egg
HYPER_MX: AdNetwork
IMMORTALITY: Egg
INTEGRITY: Egg
IOS: Platform
KINDNESS: Egg
MEDICAL: Egg
NEBULA: Egg
NONE: UILocation
NO_PRO_PERMIT: UserType
NO_ULTRA: UserType
PHONE: DeviceFormFactor
PIGGY: UILocation
PIGGY_FILL: RewardType
PIGGY_HESITANT: UserType
PIGGY_LEVEL_BUMP: RewardType
PIGGY_MULTIPLIER: RewardType
PLAYING_CONTRACT: UserType
PRESTIGE_READY: UserType
PRODIGY: Egg
PRO_PERMIT: UILocation
PRO_PERMIT_ACTIVE: UserType
PUMPKIN: Egg
QUANTUM: Egg
RESILIENCE: Egg
ROCKET_FUEL: Egg
SETTINGS: UILocation
SHELLS: UILocation
SHELLS_SHOWCASE: UILocation
SHELL_SCRIPT: RewardType
SHELL_SETS: UILocation
SHOP: UILocation
SOUL_EGGS: RewardType
SUPERFOOD: Egg
SUPER_MATERIAL: Egg
TABLET: DeviceFormFactor
TACHYON: Egg
TERRAFORM: Egg
ULTRA_ACTIVE: UserType
ULTRA_SHOP: UILocation
UNITY: AdNetwork
UNIVERSE: Egg
UNIVERSITY: UILocation
UNKNOWN: Egg
UNKNOWN_DEVICE: DeviceFormFactor
UNKNOWN_GOAL: GoalType
UNKNOWN_PLATFORM: Platform
UNKNOWN_REWARD: RewardType
VIRTUE_GEM: RewardType
VUNGLE: AdNetwork
WATERBALLOON: Egg

class AccountTransferPayload(_message.Message):
    __slots__ = ["from_id", "to_ei_user_id"]
    FROM_ID_FIELD_NUMBER: _ClassVar[int]
    TO_EI_USER_ID_FIELD_NUMBER: _ClassVar[int]
    from_id: str
    to_ei_user_id: str
    def __init__(self, from_id: _Optional[str] = ..., to_ei_user_id: _Optional[str] = ...) -> None: ...

class ActionKeyValuePair(_message.Message):
    __slots__ = ["key", "value"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class ActiveArtifactSlot(_message.Message):
    __slots__ = ["item_id", "occupied"]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    OCCUPIED_FIELD_NUMBER: _ClassVar[int]
    item_id: int
    occupied: bool
    def __init__(self, occupied: bool = ..., item_id: _Optional[int] = ...) -> None: ...

class AdAttributionInfo(_message.Message):
    __slots__ = ["adgroup_id", "adgroup_name", "attribution", "campaign_id", "campaign_name", "click_date", "conversion_date", "conversion_type", "creativeset_id", "creativeset_name", "device_ad_id", "geo", "keyword", "keyword_extra", "keyword_id", "network_name", "org_id", "org_name"]
    ADGROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ADGROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_NAME_FIELD_NUMBER: _ClassVar[int]
    CLICK_DATE_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_DATE_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATIVESET_ID_FIELD_NUMBER: _ClassVar[int]
    CREATIVESET_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_AD_ID_FIELD_NUMBER: _ClassVar[int]
    GEO_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_EXTRA_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_NAME_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_NAME_FIELD_NUMBER: _ClassVar[int]
    adgroup_id: str
    adgroup_name: str
    attribution: bool
    campaign_id: str
    campaign_name: str
    click_date: str
    conversion_date: str
    conversion_type: str
    creativeset_id: str
    creativeset_name: str
    device_ad_id: str
    geo: str
    keyword: str
    keyword_extra: str
    keyword_id: str
    network_name: str
    org_id: str
    org_name: str
    def __init__(self, device_ad_id: _Optional[str] = ..., network_name: _Optional[str] = ..., attribution: bool = ..., org_name: _Optional[str] = ..., org_id: _Optional[str] = ..., campaign_name: _Optional[str] = ..., campaign_id: _Optional[str] = ..., click_date: _Optional[str] = ..., conversion_date: _Optional[str] = ..., conversion_type: _Optional[str] = ..., geo: _Optional[str] = ..., adgroup_name: _Optional[str] = ..., adgroup_id: _Optional[str] = ..., keyword: _Optional[str] = ..., keyword_id: _Optional[str] = ..., keyword_extra: _Optional[str] = ..., creativeset_name: _Optional[str] = ..., creativeset_id: _Optional[str] = ...) -> None: ...

class AdAttributionRawData(_message.Message):
    __slots__ = ["ad_network", "device_ad_id", "json_data", "user_id"]
    AD_NETWORK_FIELD_NUMBER: _ClassVar[int]
    DEVICE_AD_ID_FIELD_NUMBER: _ClassVar[int]
    JSON_DATA_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ad_network: str
    device_ad_id: str
    json_data: str
    user_id: str
    def __init__(self, device_ad_id: _Optional[str] = ..., user_id: _Optional[str] = ..., ad_network: _Optional[str] = ..., json_data: _Optional[str] = ...) -> None: ...

class AdAttributionRow(_message.Message):
    __slots__ = ["ad_id", "ad_network", "approx_time", "campaign", "click_date", "download_date", "extra", "keyword", "user_id"]
    AD_ID_FIELD_NUMBER: _ClassVar[int]
    AD_NETWORK_FIELD_NUMBER: _ClassVar[int]
    APPROX_TIME_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    CLICK_DATE_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_DATE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ad_id: str
    ad_network: str
    approx_time: float
    campaign: str
    click_date: float
    download_date: float
    extra: str
    keyword: str
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., ad_id: _Optional[str] = ..., ad_network: _Optional[str] = ..., campaign: _Optional[str] = ..., keyword: _Optional[str] = ..., extra: _Optional[str] = ..., click_date: _Optional[float] = ..., download_date: _Optional[float] = ..., approx_time: _Optional[float] = ...) -> None: ...

class AppInfo(_message.Message):
    __slots__ = ["current_egg", "current_mission", "drone_takedowns", "drone_takedowns_elite", "egg_level", "gold_earned", "gold_spent", "iap_packs_purchased", "long_warp_uses", "lost_piggy_increments", "num_piggy_breaks", "num_prestiges", "permit_level", "piggy_found_full", "piggy_full", "piggy_size", "refill_uses", "sale_id", "sessions", "short_warp_uses", "soul_eggs", "struggle_factor", "time_piggy_full_gametime", "time_piggy_full_realtime", "trophies_unlocked", "unlimited_chickens_uses", "verified_piggy_breaks", "version_str", "video_doubler_uses"]
    CURRENT_EGG_FIELD_NUMBER: _ClassVar[int]
    CURRENT_MISSION_FIELD_NUMBER: _ClassVar[int]
    DRONE_TAKEDOWNS_ELITE_FIELD_NUMBER: _ClassVar[int]
    DRONE_TAKEDOWNS_FIELD_NUMBER: _ClassVar[int]
    EGG_LEVEL_FIELD_NUMBER: _ClassVar[int]
    GOLD_EARNED_FIELD_NUMBER: _ClassVar[int]
    GOLD_SPENT_FIELD_NUMBER: _ClassVar[int]
    IAP_PACKS_PURCHASED_FIELD_NUMBER: _ClassVar[int]
    LONG_WARP_USES_FIELD_NUMBER: _ClassVar[int]
    LOST_PIGGY_INCREMENTS_FIELD_NUMBER: _ClassVar[int]
    NUM_PIGGY_BREAKS_FIELD_NUMBER: _ClassVar[int]
    NUM_PRESTIGES_FIELD_NUMBER: _ClassVar[int]
    PERMIT_LEVEL_FIELD_NUMBER: _ClassVar[int]
    PIGGY_FOUND_FULL_FIELD_NUMBER: _ClassVar[int]
    PIGGY_FULL_FIELD_NUMBER: _ClassVar[int]
    PIGGY_SIZE_FIELD_NUMBER: _ClassVar[int]
    REFILL_USES_FIELD_NUMBER: _ClassVar[int]
    SALE_ID_FIELD_NUMBER: _ClassVar[int]
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    SHORT_WARP_USES_FIELD_NUMBER: _ClassVar[int]
    SOUL_EGGS_FIELD_NUMBER: _ClassVar[int]
    STRUGGLE_FACTOR_FIELD_NUMBER: _ClassVar[int]
    TIME_PIGGY_FULL_GAMETIME_FIELD_NUMBER: _ClassVar[int]
    TIME_PIGGY_FULL_REALTIME_FIELD_NUMBER: _ClassVar[int]
    TROPHIES_UNLOCKED_FIELD_NUMBER: _ClassVar[int]
    UNLIMITED_CHICKENS_USES_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_PIGGY_BREAKS_FIELD_NUMBER: _ClassVar[int]
    VERSION_STR_FIELD_NUMBER: _ClassVar[int]
    VIDEO_DOUBLER_USES_FIELD_NUMBER: _ClassVar[int]
    current_egg: int
    current_mission: int
    drone_takedowns: int
    drone_takedowns_elite: int
    egg_level: float
    gold_earned: int
    gold_spent: int
    iap_packs_purchased: int
    long_warp_uses: int
    lost_piggy_increments: int
    num_piggy_breaks: int
    num_prestiges: int
    permit_level: int
    piggy_found_full: bool
    piggy_full: bool
    piggy_size: int
    refill_uses: int
    sale_id: str
    sessions: int
    short_warp_uses: int
    soul_eggs: int
    struggle_factor: float
    time_piggy_full_gametime: float
    time_piggy_full_realtime: float
    trophies_unlocked: bool
    unlimited_chickens_uses: int
    verified_piggy_breaks: int
    version_str: str
    video_doubler_uses: int
    def __init__(self, version_str: _Optional[str] = ..., sessions: _Optional[int] = ..., num_prestiges: _Optional[int] = ..., soul_eggs: _Optional[int] = ..., current_egg: _Optional[int] = ..., gold_earned: _Optional[int] = ..., gold_spent: _Optional[int] = ..., current_mission: _Optional[int] = ..., piggy_size: _Optional[int] = ..., num_piggy_breaks: _Optional[int] = ..., verified_piggy_breaks: _Optional[int] = ..., iap_packs_purchased: _Optional[int] = ..., permit_level: _Optional[int] = ..., video_doubler_uses: _Optional[int] = ..., drone_takedowns: _Optional[int] = ..., drone_takedowns_elite: _Optional[int] = ..., trophies_unlocked: bool = ..., egg_level: _Optional[float] = ..., struggle_factor: _Optional[float] = ..., piggy_full: bool = ..., piggy_found_full: bool = ..., time_piggy_full_realtime: _Optional[float] = ..., time_piggy_full_gametime: _Optional[float] = ..., lost_piggy_increments: _Optional[int] = ..., sale_id: _Optional[str] = ..., unlimited_chickens_uses: _Optional[int] = ..., refill_uses: _Optional[int] = ..., short_warp_uses: _Optional[int] = ..., long_warp_uses: _Optional[int] = ...) -> None: ...

class ArtifactInventoryItem(_message.Message):
    __slots__ = ["artifact", "item_id", "quantity", "server_id"]
    ARTIFACT_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    artifact: CompleteArtifact
    item_id: int
    quantity: float
    server_id: str
    def __init__(self, item_id: _Optional[int] = ..., artifact: _Optional[_Union[CompleteArtifact, _Mapping]] = ..., quantity: _Optional[float] = ..., server_id: _Optional[str] = ...) -> None: ...

class ArtifactSpec(_message.Message):
    __slots__ = ["egg", "level", "name", "rarity"]
    class Level(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Name(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Rarity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALIEN_WOOD: ArtifactSpec.Name
    ANCIENT_TUNGSTEN: ArtifactSpec.Name
    ARTIFACT: ArtifactSpec.Type
    AURELIAN_BROOCH: ArtifactSpec.Name
    BEAK_OF_MIDAS: ArtifactSpec.Name
    BOOK_OF_BASAN: ArtifactSpec.Name
    CARVED_RAINSTICK: ArtifactSpec.Name
    CELESTIAL_BRONZE: ArtifactSpec.Name
    CENTAURIAN_STEEL: ArtifactSpec.Name
    CLARITY_STONE: ArtifactSpec.Name
    CLARITY_STONE_FRAGMENT: ArtifactSpec.Name
    COMMON: ArtifactSpec.Rarity
    DEMETERS_NECKLACE: ArtifactSpec.Name
    DILITHIUM_MONOCLE: ArtifactSpec.Name
    DILITHIUM_STONE: ArtifactSpec.Name
    DILITHIUM_STONE_FRAGMENT: ArtifactSpec.Name
    DRONE_PARTS: ArtifactSpec.Name
    EGG_FIELD_NUMBER: _ClassVar[int]
    EPIC: ArtifactSpec.Rarity
    ERIDANI_FEATHER: ArtifactSpec.Name
    EXTRATERRESTRIAL_ALUMINUM: ArtifactSpec.Name
    GOLD_METEORITE: ArtifactSpec.Name
    GREATER: ArtifactSpec.Level
    INFERIOR: ArtifactSpec.Level
    INGREDIENT: ArtifactSpec.Type
    INTERSTELLAR_COMPASS: ArtifactSpec.Name
    LALANDE_HIDE: ArtifactSpec.Name
    LEGENDARY: ArtifactSpec.Rarity
    LESSER: ArtifactSpec.Level
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    LIFE_STONE: ArtifactSpec.Name
    LIFE_STONE_FRAGMENT: ArtifactSpec.Name
    LIGHT_OF_EGGENDIL: ArtifactSpec.Name
    LUNAR_STONE: ArtifactSpec.Name
    LUNAR_STONE_FRAGMENT: ArtifactSpec.Name
    LUNAR_TOTEM: ArtifactSpec.Name
    MERCURYS_LENS: ArtifactSpec.Name
    NAME_FIELD_NUMBER: _ClassVar[int]
    NEODYMIUM_MEDALLION: ArtifactSpec.Name
    NORMAL: ArtifactSpec.Level
    ORNATE_GUSSET: ArtifactSpec.Name
    PHOENIX_FEATHER: ArtifactSpec.Name
    PROPHECY_STONE: ArtifactSpec.Name
    PROPHECY_STONE_FRAGMENT: ArtifactSpec.Name
    PUZZLE_CUBE: ArtifactSpec.Name
    QUANTUM_METRONOME: ArtifactSpec.Name
    QUANTUM_STONE: ArtifactSpec.Name
    QUANTUM_STONE_FRAGMENT: ArtifactSpec.Name
    RARE: ArtifactSpec.Rarity
    RARITY_FIELD_NUMBER: _ClassVar[int]
    SHELL_STONE: ArtifactSpec.Name
    SHELL_STONE_FRAGMENT: ArtifactSpec.Name
    SHIP_IN_A_BOTTLE: ArtifactSpec.Name
    SOLAR_TITANIUM: ArtifactSpec.Name
    SOUL_STONE: ArtifactSpec.Name
    SOUL_STONE_FRAGMENT: ArtifactSpec.Name
    SPACE_ROCKS: ArtifactSpec.Name
    STONE: ArtifactSpec.Type
    STONE_INGREDIENT: ArtifactSpec.Type
    SUPERIOR: ArtifactSpec.Level
    TACHYON_DEFLECTOR: ArtifactSpec.Name
    TACHYON_STONE: ArtifactSpec.Name
    TACHYON_STONE_FRAGMENT: ArtifactSpec.Name
    TAU_CETI_GEODE: ArtifactSpec.Name
    TERRA_STONE: ArtifactSpec.Name
    TERRA_STONE_FRAGMENT: ArtifactSpec.Name
    THE_CHALICE: ArtifactSpec.Name
    TITANIUM_ACTUATOR: ArtifactSpec.Name
    TUNGSTEN_ANKH: ArtifactSpec.Name
    UNKNOWN: ArtifactSpec.Name
    VIAL_MARTIAN_DUST: ArtifactSpec.Name
    egg: Egg
    level: ArtifactSpec.Level
    name: ArtifactSpec.Name
    rarity: ArtifactSpec.Rarity
    def __init__(self, name: _Optional[_Union[ArtifactSpec.Name, str]] = ..., level: _Optional[_Union[ArtifactSpec.Level, str]] = ..., rarity: _Optional[_Union[ArtifactSpec.Rarity, str]] = ..., egg: _Optional[_Union[Egg, str]] = ...) -> None: ...

class ArtifactsClientInfo(_message.Message):
    __slots__ = ["last_server_launch_count_sum_time", "launch_counts", "mission_capacity_mult", "mission_capacity_research_mult", "mission_duration_mult", "mission_ftl_duration_research_mult"]
    class LaunchCount(_message.Message):
        __slots__ = ["launch_points", "num_launches", "ship"]
        LAUNCH_POINTS_FIELD_NUMBER: _ClassVar[int]
        NUM_LAUNCHES_FIELD_NUMBER: _ClassVar[int]
        SHIP_FIELD_NUMBER: _ClassVar[int]
        launch_points: float
        num_launches: int
        ship: MissionInfo.Spaceship
        def __init__(self, ship: _Optional[_Union[MissionInfo.Spaceship, str]] = ..., num_launches: _Optional[int] = ..., launch_points: _Optional[float] = ...) -> None: ...
    LAST_SERVER_LAUNCH_COUNT_SUM_TIME_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_COUNTS_FIELD_NUMBER: _ClassVar[int]
    MISSION_CAPACITY_MULT_FIELD_NUMBER: _ClassVar[int]
    MISSION_CAPACITY_RESEARCH_MULT_FIELD_NUMBER: _ClassVar[int]
    MISSION_DURATION_MULT_FIELD_NUMBER: _ClassVar[int]
    MISSION_FTL_DURATION_RESEARCH_MULT_FIELD_NUMBER: _ClassVar[int]
    last_server_launch_count_sum_time: float
    launch_counts: _containers.RepeatedCompositeFieldContainer[ArtifactsClientInfo.LaunchCount]
    mission_capacity_mult: float
    mission_capacity_research_mult: float
    mission_duration_mult: float
    mission_ftl_duration_research_mult: float
    def __init__(self, mission_capacity_mult: _Optional[float] = ..., mission_duration_mult: _Optional[float] = ..., mission_ftl_duration_research_mult: _Optional[float] = ..., mission_capacity_research_mult: _Optional[float] = ..., launch_counts: _Optional[_Iterable[_Union[ArtifactsClientInfo.LaunchCount, _Mapping]]] = ..., last_server_launch_count_sum_time: _Optional[float] = ...) -> None: ...

class ArtifactsConfigurationRequest(_message.Message):
    __slots__ = ["client_version", "rinfo"]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    client_version: int
    rinfo: BasicRequestInfo
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., client_version: _Optional[int] = ...) -> None: ...

class ArtifactsConfigurationResponse(_message.Message):
    __slots__ = ["artifact_parameters", "crafting_level_infos", "mission_parameters"]
    class ArtifactParameters(_message.Message):
        __slots__ = ["base_quality", "crafting_price", "crafting_price_curve", "crafting_price_domain", "crafting_price_low", "crafting_xp", "odds_multiplier", "spec", "value"]
        BASE_QUALITY_FIELD_NUMBER: _ClassVar[int]
        CRAFTING_PRICE_CURVE_FIELD_NUMBER: _ClassVar[int]
        CRAFTING_PRICE_DOMAIN_FIELD_NUMBER: _ClassVar[int]
        CRAFTING_PRICE_FIELD_NUMBER: _ClassVar[int]
        CRAFTING_PRICE_LOW_FIELD_NUMBER: _ClassVar[int]
        CRAFTING_XP_FIELD_NUMBER: _ClassVar[int]
        ODDS_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
        SPEC_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        base_quality: float
        crafting_price: float
        crafting_price_curve: float
        crafting_price_domain: int
        crafting_price_low: float
        crafting_xp: int
        odds_multiplier: float
        spec: ArtifactSpec
        value: float
        def __init__(self, spec: _Optional[_Union[ArtifactSpec, _Mapping]] = ..., base_quality: _Optional[float] = ..., odds_multiplier: _Optional[float] = ..., value: _Optional[float] = ..., crafting_price: _Optional[float] = ..., crafting_price_low: _Optional[float] = ..., crafting_price_domain: _Optional[int] = ..., crafting_price_curve: _Optional[float] = ..., crafting_xp: _Optional[int] = ...) -> None: ...
    class CraftingLevelInfo(_message.Message):
        __slots__ = ["rarity_mult", "xp_required"]
        RARITY_MULT_FIELD_NUMBER: _ClassVar[int]
        XP_REQUIRED_FIELD_NUMBER: _ClassVar[int]
        rarity_mult: float
        xp_required: float
        def __init__(self, xp_required: _Optional[float] = ..., rarity_mult: _Optional[float] = ...) -> None: ...
    class MissionParameters(_message.Message):
        __slots__ = ["capacity_DEPRECATED", "durations", "level_mission_requirements", "ship"]
        class Duration(_message.Message):
            __slots__ = ["capacity", "duration_type", "level_capacity_bump", "level_quality_bump", "max_quality", "min_quality", "quality", "seconds"]
            CAPACITY_FIELD_NUMBER: _ClassVar[int]
            DURATION_TYPE_FIELD_NUMBER: _ClassVar[int]
            LEVEL_CAPACITY_BUMP_FIELD_NUMBER: _ClassVar[int]
            LEVEL_QUALITY_BUMP_FIELD_NUMBER: _ClassVar[int]
            MAX_QUALITY_FIELD_NUMBER: _ClassVar[int]
            MIN_QUALITY_FIELD_NUMBER: _ClassVar[int]
            QUALITY_FIELD_NUMBER: _ClassVar[int]
            SECONDS_FIELD_NUMBER: _ClassVar[int]
            capacity: int
            duration_type: MissionInfo.DurationType
            level_capacity_bump: int
            level_quality_bump: float
            max_quality: float
            min_quality: float
            quality: float
            seconds: float
            def __init__(self, duration_type: _Optional[_Union[MissionInfo.DurationType, str]] = ..., seconds: _Optional[float] = ..., quality: _Optional[float] = ..., min_quality: _Optional[float] = ..., max_quality: _Optional[float] = ..., capacity: _Optional[int] = ..., level_capacity_bump: _Optional[int] = ..., level_quality_bump: _Optional[float] = ...) -> None: ...
        CAPACITY_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
        DURATIONS_FIELD_NUMBER: _ClassVar[int]
        LEVEL_MISSION_REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
        SHIP_FIELD_NUMBER: _ClassVar[int]
        capacity_DEPRECATED: int
        durations: _containers.RepeatedCompositeFieldContainer[ArtifactsConfigurationResponse.MissionParameters.Duration]
        level_mission_requirements: _containers.RepeatedScalarFieldContainer[int]
        ship: MissionInfo.Spaceship
        def __init__(self, ship: _Optional[_Union[MissionInfo.Spaceship, str]] = ..., durations: _Optional[_Iterable[_Union[ArtifactsConfigurationResponse.MissionParameters.Duration, _Mapping]]] = ..., level_mission_requirements: _Optional[_Iterable[int]] = ..., capacity_DEPRECATED: _Optional[int] = ...) -> None: ...
    ARTIFACT_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    CRAFTING_LEVEL_INFOS_FIELD_NUMBER: _ClassVar[int]
    MISSION_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    artifact_parameters: _containers.RepeatedCompositeFieldContainer[ArtifactsConfigurationResponse.ArtifactParameters]
    crafting_level_infos: _containers.RepeatedCompositeFieldContainer[ArtifactsConfigurationResponse.CraftingLevelInfo]
    mission_parameters: _containers.RepeatedCompositeFieldContainer[ArtifactsConfigurationResponse.MissionParameters]
    def __init__(self, mission_parameters: _Optional[_Iterable[_Union[ArtifactsConfigurationResponse.MissionParameters, _Mapping]]] = ..., artifact_parameters: _Optional[_Iterable[_Union[ArtifactsConfigurationResponse.ArtifactParameters, _Mapping]]] = ..., crafting_level_infos: _Optional[_Iterable[_Union[ArtifactsConfigurationResponse.CraftingLevelInfo, _Mapping]]] = ...) -> None: ...

class ArtifactsDB(_message.Message):
    __slots__ = ["active_artifact_sets", "active_artifacts_DEPRECATED", "artifact_status", "craftable_artifacts_DEPRECATED", "crafting_counts_DEPRECATED", "discovered_artifacts_DEPRECATED", "fueling_mission", "inventory_items", "inventory_slots_NOT_USED", "item_sequence", "mission_archive", "mission_infos", "saved_artifact_sets", "virtue_afx_db"]
    class ActiveArtifactSet(_message.Message):
        __slots__ = ["slots", "uid"]
        SLOTS_FIELD_NUMBER: _ClassVar[int]
        UID_FIELD_NUMBER: _ClassVar[int]
        slots: _containers.RepeatedCompositeFieldContainer[ActiveArtifactSlot]
        uid: int
        def __init__(self, slots: _Optional[_Iterable[_Union[ActiveArtifactSlot, _Mapping]]] = ..., uid: _Optional[int] = ...) -> None: ...
    class CraftableArtifact(_message.Message):
        __slots__ = ["count", "craftable", "discovered", "recipe_discovered", "seen", "spec"]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        CRAFTABLE_FIELD_NUMBER: _ClassVar[int]
        DISCOVERED_FIELD_NUMBER: _ClassVar[int]
        RECIPE_DISCOVERED_FIELD_NUMBER: _ClassVar[int]
        SEEN_FIELD_NUMBER: _ClassVar[int]
        SPEC_FIELD_NUMBER: _ClassVar[int]
        count: int
        craftable: bool
        discovered: bool
        recipe_discovered: bool
        seen: bool
        spec: ArtifactSpec
        def __init__(self, spec: _Optional[_Union[ArtifactSpec, _Mapping]] = ..., discovered: bool = ..., craftable: bool = ..., recipe_discovered: bool = ..., seen: bool = ..., count: _Optional[int] = ...) -> None: ...
    class VirtueDB(_message.Message):
        __slots__ = ["active_artifacts", "artifact_status", "fueling_mission", "inventory_items"]
        ACTIVE_ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
        ARTIFACT_STATUS_FIELD_NUMBER: _ClassVar[int]
        FUELING_MISSION_FIELD_NUMBER: _ClassVar[int]
        INVENTORY_ITEMS_FIELD_NUMBER: _ClassVar[int]
        active_artifacts: ArtifactsDB.ActiveArtifactSet
        artifact_status: _containers.RepeatedCompositeFieldContainer[ArtifactsDB.CraftableArtifact]
        fueling_mission: MissionInfo
        inventory_items: _containers.RepeatedCompositeFieldContainer[ArtifactInventoryItem]
        def __init__(self, inventory_items: _Optional[_Iterable[_Union[ArtifactInventoryItem, _Mapping]]] = ..., artifact_status: _Optional[_Iterable[_Union[ArtifactsDB.CraftableArtifact, _Mapping]]] = ..., fueling_mission: _Optional[_Union[MissionInfo, _Mapping]] = ..., active_artifacts: _Optional[_Union[ArtifactsDB.ActiveArtifactSet, _Mapping]] = ...) -> None: ...
    ACTIVE_ARTIFACTS_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_ARTIFACT_SETS_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_STATUS_FIELD_NUMBER: _ClassVar[int]
    CRAFTABLE_ARTIFACTS_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    CRAFTING_COUNTS_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    DISCOVERED_ARTIFACTS_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    FUELING_MISSION_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_ITEMS_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_SLOTS_NOT_USED_FIELD_NUMBER: _ClassVar[int]
    ITEM_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    MISSION_ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    MISSION_INFOS_FIELD_NUMBER: _ClassVar[int]
    SAVED_ARTIFACT_SETS_FIELD_NUMBER: _ClassVar[int]
    VIRTUE_AFX_DB_FIELD_NUMBER: _ClassVar[int]
    active_artifact_sets: _containers.RepeatedCompositeFieldContainer[ArtifactsDB.ActiveArtifactSet]
    active_artifacts_DEPRECATED: _containers.RepeatedCompositeFieldContainer[ActiveArtifactSlot]
    artifact_status: _containers.RepeatedCompositeFieldContainer[ArtifactsDB.CraftableArtifact]
    craftable_artifacts_DEPRECATED: _containers.RepeatedCompositeFieldContainer[ArtifactsDB.CraftableArtifact]
    crafting_counts_DEPRECATED: _containers.RepeatedCompositeFieldContainer[ArtifactsDB.CraftableArtifact]
    discovered_artifacts_DEPRECATED: _containers.RepeatedCompositeFieldContainer[ArtifactSpec]
    fueling_mission: MissionInfo
    inventory_items: _containers.RepeatedCompositeFieldContainer[ArtifactInventoryItem]
    inventory_slots_NOT_USED: _containers.RepeatedCompositeFieldContainer[InventorySlot]
    item_sequence: int
    mission_archive: _containers.RepeatedCompositeFieldContainer[MissionInfo]
    mission_infos: _containers.RepeatedCompositeFieldContainer[MissionInfo]
    saved_artifact_sets: _containers.RepeatedCompositeFieldContainer[ArtifactsDB.ActiveArtifactSet]
    virtue_afx_db: ArtifactsDB.VirtueDB
    def __init__(self, inventory_items: _Optional[_Iterable[_Union[ArtifactInventoryItem, _Mapping]]] = ..., item_sequence: _Optional[int] = ..., inventory_slots_NOT_USED: _Optional[_Iterable[_Union[InventorySlot, _Mapping]]] = ..., active_artifacts_DEPRECATED: _Optional[_Iterable[_Union[ActiveArtifactSlot, _Mapping]]] = ..., active_artifact_sets: _Optional[_Iterable[_Union[ArtifactsDB.ActiveArtifactSet, _Mapping]]] = ..., saved_artifact_sets: _Optional[_Iterable[_Union[ArtifactsDB.ActiveArtifactSet, _Mapping]]] = ..., artifact_status: _Optional[_Iterable[_Union[ArtifactsDB.CraftableArtifact, _Mapping]]] = ..., fueling_mission: _Optional[_Union[MissionInfo, _Mapping]] = ..., mission_infos: _Optional[_Iterable[_Union[MissionInfo, _Mapping]]] = ..., mission_archive: _Optional[_Iterable[_Union[MissionInfo, _Mapping]]] = ..., virtue_afx_db: _Optional[_Union[ArtifactsDB.VirtueDB, _Mapping]] = ..., discovered_artifacts_DEPRECATED: _Optional[_Iterable[_Union[ArtifactSpec, _Mapping]]] = ..., craftable_artifacts_DEPRECATED: _Optional[_Iterable[_Union[ArtifactsDB.CraftableArtifact, _Mapping]]] = ..., crafting_counts_DEPRECATED: _Optional[_Iterable[_Union[ArtifactsDB.CraftableArtifact, _Mapping]]] = ...) -> None: ...

class AuthenticateArtifactResponse(_message.Message):
    __slots__ = ["delete", "demote", "ei_user_id", "original_item_id", "success"]
    DELETE_FIELD_NUMBER: _ClassVar[int]
    DEMOTE_FIELD_NUMBER: _ClassVar[int]
    EI_USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    delete: bool
    demote: bool
    ei_user_id: str
    original_item_id: int
    success: bool
    def __init__(self, success: bool = ..., original_item_id: _Optional[int] = ..., demote: bool = ..., delete: bool = ..., ei_user_id: _Optional[str] = ...) -> None: ...

class AuthenticatedMessage(_message.Message):
    __slots__ = ["code", "compressed", "message", "original_size", "user_id", "version"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    code: str
    compressed: bool
    message: bytes
    original_size: int
    user_id: str
    version: int
    def __init__(self, message: _Optional[bytes] = ..., version: _Optional[int] = ..., code: _Optional[str] = ..., compressed: bool = ..., original_size: _Optional[int] = ..., user_id: _Optional[str] = ...) -> None: ...

class AutoJoinCoopRequest(_message.Message):
    __slots__ = ["client_version", "contract_identifier", "eop", "grade", "league", "platform", "points_replay", "rinfo", "seconds_remaining", "soul_power", "user_id", "user_name"]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    EOP_FIELD_NUMBER: _ClassVar[int]
    GRADE_FIELD_NUMBER: _ClassVar[int]
    LEAGUE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    POINTS_REPLAY_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    SECONDS_REMAINING_FIELD_NUMBER: _ClassVar[int]
    SOUL_POWER_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    client_version: int
    contract_identifier: str
    eop: float
    grade: Contract.PlayerGrade
    league: int
    platform: Platform
    points_replay: bool
    rinfo: BasicRequestInfo
    seconds_remaining: float
    soul_power: float
    user_id: str
    user_name: str
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., contract_identifier: _Optional[str] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., soul_power: _Optional[float] = ..., eop: _Optional[float] = ..., league: _Optional[int] = ..., grade: _Optional[_Union[Contract.PlayerGrade, str]] = ..., points_replay: bool = ..., seconds_remaining: _Optional[float] = ..., platform: _Optional[_Union[Platform, str]] = ..., client_version: _Optional[int] = ...) -> None: ...

class Backup(_message.Message):
    __slots__ = ["approx_time", "artifacts", "artifacts_db", "checksum", "contracts", "device_id", "ei_user_id", "farms", "force_backup", "force_offer_backup", "game", "game_services_id", "mail_state", "misc", "mission", "push_user_id", "read_mail_ids", "settings", "shell_db", "shells", "signature", "sim", "stats", "tutorial", "user_id", "user_name", "version", "virtue"]
    class AchievementInfo(_message.Message):
        __slots__ = ["achieved", "id"]
        ACHIEVED_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        achieved: bool
        id: str
        def __init__(self, id: _Optional[str] = ..., achieved: bool = ...) -> None: ...
    class ActiveBoost(_message.Message):
        __slots__ = ["boost_id", "reference_value", "time_remaining"]
        BOOST_ID_FIELD_NUMBER: _ClassVar[int]
        REFERENCE_VALUE_FIELD_NUMBER: _ClassVar[int]
        TIME_REMAINING_FIELD_NUMBER: _ClassVar[int]
        boost_id: str
        reference_value: float
        time_remaining: float
        def __init__(self, boost_id: _Optional[str] = ..., time_remaining: _Optional[float] = ..., reference_value: _Optional[float] = ...) -> None: ...
    class Artifacts(_message.Message):
        __slots__ = ["crafting_xp", "egg_type_infusing", "eggs_infused", "enabled", "flow_percentage_artifacts", "fueling_enabled", "infusing", "infusing_eggs_required", "infusing_enabled_DEPRECATED", "intro_shown", "inventory_score", "item_being_infused", "last_fueled_ship", "spec_being_infused", "tank_filling_enabled", "tank_fuels", "tank_level", "tank_limits"]
        CRAFTING_XP_FIELD_NUMBER: _ClassVar[int]
        EGGS_INFUSED_FIELD_NUMBER: _ClassVar[int]
        EGG_TYPE_INFUSING_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        FLOW_PERCENTAGE_ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
        FUELING_ENABLED_FIELD_NUMBER: _ClassVar[int]
        INFUSING_EGGS_REQUIRED_FIELD_NUMBER: _ClassVar[int]
        INFUSING_ENABLED_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
        INFUSING_FIELD_NUMBER: _ClassVar[int]
        INTRO_SHOWN_FIELD_NUMBER: _ClassVar[int]
        INVENTORY_SCORE_FIELD_NUMBER: _ClassVar[int]
        ITEM_BEING_INFUSED_FIELD_NUMBER: _ClassVar[int]
        LAST_FUELED_SHIP_FIELD_NUMBER: _ClassVar[int]
        SPEC_BEING_INFUSED_FIELD_NUMBER: _ClassVar[int]
        TANK_FILLING_ENABLED_FIELD_NUMBER: _ClassVar[int]
        TANK_FUELS_FIELD_NUMBER: _ClassVar[int]
        TANK_LEVEL_FIELD_NUMBER: _ClassVar[int]
        TANK_LIMITS_FIELD_NUMBER: _ClassVar[int]
        crafting_xp: float
        egg_type_infusing: Egg
        eggs_infused: float
        enabled: bool
        flow_percentage_artifacts: float
        fueling_enabled: bool
        infusing: bool
        infusing_eggs_required: float
        infusing_enabled_DEPRECATED: bool
        intro_shown: bool
        inventory_score: float
        item_being_infused: ArtifactInventoryItem
        last_fueled_ship: MissionInfo.Spaceship
        spec_being_infused: ArtifactSpec
        tank_filling_enabled: bool
        tank_fuels: _containers.RepeatedScalarFieldContainer[float]
        tank_level: int
        tank_limits: _containers.RepeatedScalarFieldContainer[float]
        def __init__(self, infusing: bool = ..., item_being_infused: _Optional[_Union[ArtifactInventoryItem, _Mapping]] = ..., spec_being_infused: _Optional[_Union[ArtifactSpec, _Mapping]] = ..., egg_type_infusing: _Optional[_Union[Egg, str]] = ..., infusing_eggs_required: _Optional[float] = ..., eggs_infused: _Optional[float] = ..., flow_percentage_artifacts: _Optional[float] = ..., fueling_enabled: bool = ..., tank_filling_enabled: bool = ..., tank_level: _Optional[int] = ..., tank_fuels: _Optional[_Iterable[float]] = ..., tank_limits: _Optional[_Iterable[float]] = ..., last_fueled_ship: _Optional[_Union[MissionInfo.Spaceship, str]] = ..., inventory_score: _Optional[float] = ..., crafting_xp: _Optional[float] = ..., enabled: bool = ..., intro_shown: bool = ..., infusing_enabled_DEPRECATED: bool = ...) -> None: ...
    class Game(_message.Message):
        __slots__ = ["achievements", "boosts", "current_farm", "current_multiplier", "current_multiplier_expiration", "egg_medal_level", "eggs_of_prophecy", "epic_research", "force_elite_contracts", "golden_eggs_earned", "golden_eggs_spent", "hyperloop_station", "last_daily_gift_collected_day", "last_news_time", "lifetime_cash_earned", "long_idle_notification_set", "long_idle_notification_threshold", "long_idle_reward", "max_egg_reached", "max_farm_size_reached", "new_player_event_end_time", "news", "next_daily_gift_time", "num_daily_gifts_collected", "permit_level", "piggy_bank", "piggy_full_alert_shown", "prestige_cash_earned", "prestige_soul_boost_cash", "shell_scripts_earned", "shell_scripts_spent", "soul_eggs", "soul_eggs_d", "time_cheat_debt", "total_time_cheats_detected", "unclaimed_eggs_of_prophecy", "unclaimed_shell_scripts", "unclaimed_soul_eggs", "unclaimed_soul_eggs_d", "uncliamed_golden_eggs"]
        ACHIEVEMENTS_FIELD_NUMBER: _ClassVar[int]
        BOOSTS_FIELD_NUMBER: _ClassVar[int]
        CURRENT_FARM_FIELD_NUMBER: _ClassVar[int]
        CURRENT_MULTIPLIER_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
        CURRENT_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
        EGGS_OF_PROPHECY_FIELD_NUMBER: _ClassVar[int]
        EGG_MEDAL_LEVEL_FIELD_NUMBER: _ClassVar[int]
        EPIC_RESEARCH_FIELD_NUMBER: _ClassVar[int]
        FORCE_ELITE_CONTRACTS_FIELD_NUMBER: _ClassVar[int]
        GOLDEN_EGGS_EARNED_FIELD_NUMBER: _ClassVar[int]
        GOLDEN_EGGS_SPENT_FIELD_NUMBER: _ClassVar[int]
        HYPERLOOP_STATION_FIELD_NUMBER: _ClassVar[int]
        LAST_DAILY_GIFT_COLLECTED_DAY_FIELD_NUMBER: _ClassVar[int]
        LAST_NEWS_TIME_FIELD_NUMBER: _ClassVar[int]
        LIFETIME_CASH_EARNED_FIELD_NUMBER: _ClassVar[int]
        LONG_IDLE_NOTIFICATION_SET_FIELD_NUMBER: _ClassVar[int]
        LONG_IDLE_NOTIFICATION_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        LONG_IDLE_REWARD_FIELD_NUMBER: _ClassVar[int]
        MAX_EGG_REACHED_FIELD_NUMBER: _ClassVar[int]
        MAX_FARM_SIZE_REACHED_FIELD_NUMBER: _ClassVar[int]
        NEWS_FIELD_NUMBER: _ClassVar[int]
        NEW_PLAYER_EVENT_END_TIME_FIELD_NUMBER: _ClassVar[int]
        NEXT_DAILY_GIFT_TIME_FIELD_NUMBER: _ClassVar[int]
        NUM_DAILY_GIFTS_COLLECTED_FIELD_NUMBER: _ClassVar[int]
        PERMIT_LEVEL_FIELD_NUMBER: _ClassVar[int]
        PIGGY_BANK_FIELD_NUMBER: _ClassVar[int]
        PIGGY_FULL_ALERT_SHOWN_FIELD_NUMBER: _ClassVar[int]
        PRESTIGE_CASH_EARNED_FIELD_NUMBER: _ClassVar[int]
        PRESTIGE_SOUL_BOOST_CASH_FIELD_NUMBER: _ClassVar[int]
        SHELL_SCRIPTS_EARNED_FIELD_NUMBER: _ClassVar[int]
        SHELL_SCRIPTS_SPENT_FIELD_NUMBER: _ClassVar[int]
        SOUL_EGGS_D_FIELD_NUMBER: _ClassVar[int]
        SOUL_EGGS_FIELD_NUMBER: _ClassVar[int]
        TIME_CHEAT_DEBT_FIELD_NUMBER: _ClassVar[int]
        TOTAL_TIME_CHEATS_DETECTED_FIELD_NUMBER: _ClassVar[int]
        UNCLAIMED_EGGS_OF_PROPHECY_FIELD_NUMBER: _ClassVar[int]
        UNCLAIMED_SHELL_SCRIPTS_FIELD_NUMBER: _ClassVar[int]
        UNCLAIMED_SOUL_EGGS_D_FIELD_NUMBER: _ClassVar[int]
        UNCLAIMED_SOUL_EGGS_FIELD_NUMBER: _ClassVar[int]
        UNCLIAMED_GOLDEN_EGGS_FIELD_NUMBER: _ClassVar[int]
        achievements: _containers.RepeatedCompositeFieldContainer[Backup.AchievementInfo]
        boosts: _containers.RepeatedCompositeFieldContainer[Backup.OwnedBoost]
        current_farm: int
        current_multiplier: float
        current_multiplier_expiration: float
        egg_medal_level: _containers.RepeatedScalarFieldContainer[int]
        eggs_of_prophecy: int
        epic_research: _containers.RepeatedCompositeFieldContainer[Backup.ResearchItem]
        force_elite_contracts: bool
        golden_eggs_earned: int
        golden_eggs_spent: int
        hyperloop_station: bool
        last_daily_gift_collected_day: int
        last_news_time: float
        lifetime_cash_earned: float
        long_idle_notification_set: bool
        long_idle_notification_threshold: float
        long_idle_reward: float
        max_egg_reached: Egg
        max_farm_size_reached: _containers.RepeatedScalarFieldContainer[int]
        new_player_event_end_time: float
        news: _containers.RepeatedCompositeFieldContainer[Backup.NewsHeadline]
        next_daily_gift_time: float
        num_daily_gifts_collected: int
        permit_level: int
        piggy_bank: int
        piggy_full_alert_shown: bool
        prestige_cash_earned: float
        prestige_soul_boost_cash: float
        shell_scripts_earned: int
        shell_scripts_spent: int
        soul_eggs: int
        soul_eggs_d: float
        time_cheat_debt: float
        total_time_cheats_detected: int
        unclaimed_eggs_of_prophecy: int
        unclaimed_shell_scripts: int
        unclaimed_soul_eggs: int
        unclaimed_soul_eggs_d: float
        uncliamed_golden_eggs: int
        def __init__(self, current_farm: _Optional[int] = ..., max_egg_reached: _Optional[_Union[Egg, str]] = ..., golden_eggs_earned: _Optional[int] = ..., golden_eggs_spent: _Optional[int] = ..., uncliamed_golden_eggs: _Optional[int] = ..., soul_eggs: _Optional[int] = ..., unclaimed_soul_eggs: _Optional[int] = ..., soul_eggs_d: _Optional[float] = ..., unclaimed_soul_eggs_d: _Optional[float] = ..., eggs_of_prophecy: _Optional[int] = ..., unclaimed_eggs_of_prophecy: _Optional[int] = ..., shell_scripts_earned: _Optional[int] = ..., shell_scripts_spent: _Optional[int] = ..., unclaimed_shell_scripts: _Optional[int] = ..., prestige_cash_earned: _Optional[float] = ..., prestige_soul_boost_cash: _Optional[float] = ..., lifetime_cash_earned: _Optional[float] = ..., piggy_bank: _Optional[int] = ..., piggy_full_alert_shown: bool = ..., permit_level: _Optional[int] = ..., epic_research: _Optional[_Iterable[_Union[Backup.ResearchItem, _Mapping]]] = ..., hyperloop_station: bool = ..., next_daily_gift_time: _Optional[float] = ..., last_daily_gift_collected_day: _Optional[int] = ..., num_daily_gifts_collected: _Optional[int] = ..., news: _Optional[_Iterable[_Union[Backup.NewsHeadline, _Mapping]]] = ..., last_news_time: _Optional[float] = ..., current_multiplier: _Optional[float] = ..., current_multiplier_expiration: _Optional[float] = ..., achievements: _Optional[_Iterable[_Union[Backup.AchievementInfo, _Mapping]]] = ..., max_farm_size_reached: _Optional[_Iterable[int]] = ..., egg_medal_level: _Optional[_Iterable[int]] = ..., long_idle_notification_set: bool = ..., long_idle_notification_threshold: _Optional[float] = ..., long_idle_reward: _Optional[float] = ..., boosts: _Optional[_Iterable[_Union[Backup.OwnedBoost, _Mapping]]] = ..., total_time_cheats_detected: _Optional[int] = ..., force_elite_contracts: bool = ..., new_player_event_end_time: _Optional[float] = ..., time_cheat_debt: _Optional[float] = ...) -> None: ...
    class Misc(_message.Message):
        __slots__ = ["ar_alert", "backup_reminder_alert", "boost_token_alert", "challenges_alert", "chicken_btn_pref_big", "colleggtibles_alert", "contracts_alert", "contracts_alert_v2", "coop_alert", "coop_alert_v2", "egg_of_prophecy_alert", "eov_alert", "free_hatchery_refill_given", "friend_rank", "friend_rank_pop", "global_rank", "global_rank_pop", "last_prestige_alert_soul_eggs_DEPRECATED", "last_share_farm_value", "last_share_swarm_farm_value", "last_share_swarm_size", "max_button_alert", "mission_target_alert", "soul_egg_alert", "switch_alert", "trophy_alert"]
        AR_ALERT_FIELD_NUMBER: _ClassVar[int]
        BACKUP_REMINDER_ALERT_FIELD_NUMBER: _ClassVar[int]
        BOOST_TOKEN_ALERT_FIELD_NUMBER: _ClassVar[int]
        CHALLENGES_ALERT_FIELD_NUMBER: _ClassVar[int]
        CHICKEN_BTN_PREF_BIG_FIELD_NUMBER: _ClassVar[int]
        COLLEGGTIBLES_ALERT_FIELD_NUMBER: _ClassVar[int]
        CONTRACTS_ALERT_FIELD_NUMBER: _ClassVar[int]
        CONTRACTS_ALERT_V2_FIELD_NUMBER: _ClassVar[int]
        COOP_ALERT_FIELD_NUMBER: _ClassVar[int]
        COOP_ALERT_V2_FIELD_NUMBER: _ClassVar[int]
        EGG_OF_PROPHECY_ALERT_FIELD_NUMBER: _ClassVar[int]
        EOV_ALERT_FIELD_NUMBER: _ClassVar[int]
        FREE_HATCHERY_REFILL_GIVEN_FIELD_NUMBER: _ClassVar[int]
        FRIEND_RANK_FIELD_NUMBER: _ClassVar[int]
        FRIEND_RANK_POP_FIELD_NUMBER: _ClassVar[int]
        GLOBAL_RANK_FIELD_NUMBER: _ClassVar[int]
        GLOBAL_RANK_POP_FIELD_NUMBER: _ClassVar[int]
        LAST_PRESTIGE_ALERT_SOUL_EGGS_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
        LAST_SHARE_FARM_VALUE_FIELD_NUMBER: _ClassVar[int]
        LAST_SHARE_SWARM_FARM_VALUE_FIELD_NUMBER: _ClassVar[int]
        LAST_SHARE_SWARM_SIZE_FIELD_NUMBER: _ClassVar[int]
        MAX_BUTTON_ALERT_FIELD_NUMBER: _ClassVar[int]
        MISSION_TARGET_ALERT_FIELD_NUMBER: _ClassVar[int]
        SOUL_EGG_ALERT_FIELD_NUMBER: _ClassVar[int]
        SWITCH_ALERT_FIELD_NUMBER: _ClassVar[int]
        TROPHY_ALERT_FIELD_NUMBER: _ClassVar[int]
        ar_alert: bool
        backup_reminder_alert: bool
        boost_token_alert: bool
        challenges_alert: bool
        chicken_btn_pref_big: bool
        colleggtibles_alert: bool
        contracts_alert: bool
        contracts_alert_v2: bool
        coop_alert: bool
        coop_alert_v2: bool
        egg_of_prophecy_alert: bool
        eov_alert: bool
        free_hatchery_refill_given: bool
        friend_rank: int
        friend_rank_pop: int
        global_rank: int
        global_rank_pop: int
        last_prestige_alert_soul_eggs_DEPRECATED: int
        last_share_farm_value: float
        last_share_swarm_farm_value: float
        last_share_swarm_size: float
        max_button_alert: bool
        mission_target_alert: bool
        soul_egg_alert: bool
        switch_alert: bool
        trophy_alert: bool
        def __init__(self, chicken_btn_pref_big: bool = ..., free_hatchery_refill_given: bool = ..., last_share_farm_value: _Optional[float] = ..., last_share_swarm_farm_value: _Optional[float] = ..., last_share_swarm_size: _Optional[float] = ..., last_prestige_alert_soul_eggs_DEPRECATED: _Optional[int] = ..., friend_rank: _Optional[int] = ..., friend_rank_pop: _Optional[int] = ..., global_rank: _Optional[int] = ..., global_rank_pop: _Optional[int] = ..., challenges_alert: bool = ..., trophy_alert: bool = ..., ar_alert: bool = ..., contracts_alert: bool = ..., contracts_alert_v2: bool = ..., coop_alert: bool = ..., coop_alert_v2: bool = ..., switch_alert: bool = ..., egg_of_prophecy_alert: bool = ..., boost_token_alert: bool = ..., soul_egg_alert: bool = ..., backup_reminder_alert: bool = ..., max_button_alert: bool = ..., mission_target_alert: bool = ..., colleggtibles_alert: bool = ..., eov_alert: bool = ...) -> None: ...
    class Mission(_message.Message):
        __slots__ = ["current_mission", "current_missions", "missions", "reference_value"]
        CURRENT_MISSIONS_FIELD_NUMBER: _ClassVar[int]
        CURRENT_MISSION_FIELD_NUMBER: _ClassVar[int]
        MISSIONS_FIELD_NUMBER: _ClassVar[int]
        REFERENCE_VALUE_FIELD_NUMBER: _ClassVar[int]
        current_mission: str
        current_missions: _containers.RepeatedScalarFieldContainer[str]
        missions: _containers.RepeatedCompositeFieldContainer[Backup.MissionInfo]
        reference_value: float
        def __init__(self, current_mission: _Optional[str] = ..., reference_value: _Optional[float] = ..., current_missions: _Optional[_Iterable[str]] = ..., missions: _Optional[_Iterable[_Union[Backup.MissionInfo, _Mapping]]] = ...) -> None: ...
    class MissionInfo(_message.Message):
        __slots__ = ["completed", "id", "reference_value"]
        COMPLETED_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        REFERENCE_VALUE_FIELD_NUMBER: _ClassVar[int]
        completed: bool
        id: str
        reference_value: float
        def __init__(self, id: _Optional[str] = ..., completed: bool = ..., reference_value: _Optional[float] = ...) -> None: ...
    class NewsHeadline(_message.Message):
        __slots__ = ["id", "read"]
        ID_FIELD_NUMBER: _ClassVar[int]
        READ_FIELD_NUMBER: _ClassVar[int]
        id: str
        read: bool
        def __init__(self, id: _Optional[str] = ..., read: bool = ...) -> None: ...
    class OwnedBoost(_message.Message):
        __slots__ = ["boost_id", "count"]
        BOOST_ID_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        boost_id: str
        count: int
        def __init__(self, boost_id: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...
    class ResearchItem(_message.Message):
        __slots__ = ["id", "level"]
        ID_FIELD_NUMBER: _ClassVar[int]
        LEVEL_FIELD_NUMBER: _ClassVar[int]
        id: str
        level: int
        def __init__(self, id: _Optional[str] = ..., level: _Optional[int] = ...) -> None: ...
    class Settings(_message.Message):
        __slots__ = ["age_queried", "age_restricted", "artifact_sparkle", "auto_stop_fueling", "contracts_widget_enabled", "coppa_queried", "coppa_restricted", "data_collection_consent_given", "data_collection_consent_queried", "force_touch_chicken_btn", "gdpr_age_restricted", "gdpr_consent_given", "gdpr_consent_queried", "hide_cc_status", "last_backup_time", "last_day_age_queried", "last_notification_query_time", "low_battery_mode", "low_performance", "low_performance_mode", "max_enabled", "music", "notifications_on", "notifications_queried", "notify_daily_gift", "sfx", "user_ads_enabled", "user_analytics_enabled", "user_cloud_enabled", "user_personalized_ads_enabled"]
        AGE_QUERIED_FIELD_NUMBER: _ClassVar[int]
        AGE_RESTRICTED_FIELD_NUMBER: _ClassVar[int]
        ARTIFACT_SPARKLE_FIELD_NUMBER: _ClassVar[int]
        AUTO_STOP_FUELING_FIELD_NUMBER: _ClassVar[int]
        CONTRACTS_WIDGET_ENABLED_FIELD_NUMBER: _ClassVar[int]
        COPPA_QUERIED_FIELD_NUMBER: _ClassVar[int]
        COPPA_RESTRICTED_FIELD_NUMBER: _ClassVar[int]
        DATA_COLLECTION_CONSENT_GIVEN_FIELD_NUMBER: _ClassVar[int]
        DATA_COLLECTION_CONSENT_QUERIED_FIELD_NUMBER: _ClassVar[int]
        FORCE_TOUCH_CHICKEN_BTN_FIELD_NUMBER: _ClassVar[int]
        GDPR_AGE_RESTRICTED_FIELD_NUMBER: _ClassVar[int]
        GDPR_CONSENT_GIVEN_FIELD_NUMBER: _ClassVar[int]
        GDPR_CONSENT_QUERIED_FIELD_NUMBER: _ClassVar[int]
        HIDE_CC_STATUS_FIELD_NUMBER: _ClassVar[int]
        LAST_BACKUP_TIME_FIELD_NUMBER: _ClassVar[int]
        LAST_DAY_AGE_QUERIED_FIELD_NUMBER: _ClassVar[int]
        LAST_NOTIFICATION_QUERY_TIME_FIELD_NUMBER: _ClassVar[int]
        LOW_BATTERY_MODE_FIELD_NUMBER: _ClassVar[int]
        LOW_PERFORMANCE_FIELD_NUMBER: _ClassVar[int]
        LOW_PERFORMANCE_MODE_FIELD_NUMBER: _ClassVar[int]
        MAX_ENABLED_FIELD_NUMBER: _ClassVar[int]
        MUSIC_FIELD_NUMBER: _ClassVar[int]
        NOTIFICATIONS_ON_FIELD_NUMBER: _ClassVar[int]
        NOTIFICATIONS_QUERIED_FIELD_NUMBER: _ClassVar[int]
        NOTIFY_DAILY_GIFT_FIELD_NUMBER: _ClassVar[int]
        SFX_FIELD_NUMBER: _ClassVar[int]
        USER_ADS_ENABLED_FIELD_NUMBER: _ClassVar[int]
        USER_ANALYTICS_ENABLED_FIELD_NUMBER: _ClassVar[int]
        USER_CLOUD_ENABLED_FIELD_NUMBER: _ClassVar[int]
        USER_PERSONALIZED_ADS_ENABLED_FIELD_NUMBER: _ClassVar[int]
        age_queried: bool
        age_restricted: bool
        artifact_sparkle: bool
        auto_stop_fueling: bool
        contracts_widget_enabled: bool
        coppa_queried: bool
        coppa_restricted: bool
        data_collection_consent_given: bool
        data_collection_consent_queried: bool
        force_touch_chicken_btn: bool
        gdpr_age_restricted: bool
        gdpr_consent_given: bool
        gdpr_consent_queried: bool
        hide_cc_status: bool
        last_backup_time: float
        last_day_age_queried: int
        last_notification_query_time: float
        low_battery_mode: bool
        low_performance: bool
        low_performance_mode: bool
        max_enabled: bool
        music: bool
        notifications_on: bool
        notifications_queried: bool
        notify_daily_gift: bool
        sfx: bool
        user_ads_enabled: bool
        user_analytics_enabled: bool
        user_cloud_enabled: bool
        user_personalized_ads_enabled: bool
        def __init__(self, sfx: bool = ..., music: bool = ..., low_battery_mode: bool = ..., low_performance_mode: bool = ..., force_touch_chicken_btn: bool = ..., notifications_queried: bool = ..., last_notification_query_time: _Optional[float] = ..., notifications_on: bool = ..., notify_daily_gift: bool = ..., low_performance: bool = ..., auto_stop_fueling: bool = ..., max_enabled: bool = ..., hide_cc_status: bool = ..., contracts_widget_enabled: bool = ..., artifact_sparkle: bool = ..., last_backup_time: _Optional[float] = ..., coppa_queried: bool = ..., coppa_restricted: bool = ..., gdpr_consent_queried: bool = ..., gdpr_age_restricted: bool = ..., gdpr_consent_given: bool = ..., age_queried: bool = ..., age_restricted: bool = ..., data_collection_consent_queried: bool = ..., data_collection_consent_given: bool = ..., last_day_age_queried: _Optional[int] = ..., user_ads_enabled: bool = ..., user_cloud_enabled: bool = ..., user_analytics_enabled: bool = ..., user_personalized_ads_enabled: bool = ...) -> None: ...
    class Shells(_message.Message):
        __slots__ = ["contracts_intro_alert", "intro_alert", "num_new"]
        CONTRACTS_INTRO_ALERT_FIELD_NUMBER: _ClassVar[int]
        INTRO_ALERT_FIELD_NUMBER: _ClassVar[int]
        NUM_NEW_FIELD_NUMBER: _ClassVar[int]
        contracts_intro_alert: bool
        intro_alert: bool
        num_new: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, intro_alert: bool = ..., contracts_intro_alert: bool = ..., num_new: _Optional[_Iterable[int]] = ...) -> None: ...
    class Simulation(_message.Message):
        __slots__ = ["active_boosts", "boost_tokens_given", "boost_tokens_received", "boost_tokens_spent", "cash_earned", "cash_spent", "common_research", "contract_id", "egg_type", "eggs_laid", "eggs_paid_for", "eggs_shipped", "farm_type", "gametime_until_next_boost_token", "hab_incubator_popuplation", "hab_population", "hab_population_indound", "habs", "hatchery_population", "last_cash_boost_time", "last_step_time", "num_chickens", "num_chickens_running", "num_chickens_unsettled", "silos_owned", "time_cheat_debt_DEP", "time_cheats_detected", "total_step_time", "train_length", "unclaimed_boost_tokens", "unclaimed_cash", "vehicles"]
        ACTIVE_BOOSTS_FIELD_NUMBER: _ClassVar[int]
        BOOST_TOKENS_GIVEN_FIELD_NUMBER: _ClassVar[int]
        BOOST_TOKENS_RECEIVED_FIELD_NUMBER: _ClassVar[int]
        BOOST_TOKENS_SPENT_FIELD_NUMBER: _ClassVar[int]
        CASH_EARNED_FIELD_NUMBER: _ClassVar[int]
        CASH_SPENT_FIELD_NUMBER: _ClassVar[int]
        COMMON_RESEARCH_FIELD_NUMBER: _ClassVar[int]
        CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
        EGGS_LAID_FIELD_NUMBER: _ClassVar[int]
        EGGS_PAID_FOR_FIELD_NUMBER: _ClassVar[int]
        EGGS_SHIPPED_FIELD_NUMBER: _ClassVar[int]
        EGG_TYPE_FIELD_NUMBER: _ClassVar[int]
        FARM_TYPE_FIELD_NUMBER: _ClassVar[int]
        GAMETIME_UNTIL_NEXT_BOOST_TOKEN_FIELD_NUMBER: _ClassVar[int]
        HABS_FIELD_NUMBER: _ClassVar[int]
        HAB_INCUBATOR_POPUPLATION_FIELD_NUMBER: _ClassVar[int]
        HAB_POPULATION_FIELD_NUMBER: _ClassVar[int]
        HAB_POPULATION_INDOUND_FIELD_NUMBER: _ClassVar[int]
        HATCHERY_POPULATION_FIELD_NUMBER: _ClassVar[int]
        LAST_CASH_BOOST_TIME_FIELD_NUMBER: _ClassVar[int]
        LAST_STEP_TIME_FIELD_NUMBER: _ClassVar[int]
        NUM_CHICKENS_FIELD_NUMBER: _ClassVar[int]
        NUM_CHICKENS_RUNNING_FIELD_NUMBER: _ClassVar[int]
        NUM_CHICKENS_UNSETTLED_FIELD_NUMBER: _ClassVar[int]
        SILOS_OWNED_FIELD_NUMBER: _ClassVar[int]
        TIME_CHEATS_DETECTED_FIELD_NUMBER: _ClassVar[int]
        TIME_CHEAT_DEBT_DEP_FIELD_NUMBER: _ClassVar[int]
        TOTAL_STEP_TIME_FIELD_NUMBER: _ClassVar[int]
        TRAIN_LENGTH_FIELD_NUMBER: _ClassVar[int]
        UNCLAIMED_BOOST_TOKENS_FIELD_NUMBER: _ClassVar[int]
        UNCLAIMED_CASH_FIELD_NUMBER: _ClassVar[int]
        VEHICLES_FIELD_NUMBER: _ClassVar[int]
        active_boosts: _containers.RepeatedCompositeFieldContainer[Backup.ActiveBoost]
        boost_tokens_given: int
        boost_tokens_received: int
        boost_tokens_spent: int
        cash_earned: float
        cash_spent: float
        common_research: _containers.RepeatedCompositeFieldContainer[Backup.ResearchItem]
        contract_id: str
        egg_type: Egg
        eggs_laid: float
        eggs_paid_for: float
        eggs_shipped: float
        farm_type: FarmType
        gametime_until_next_boost_token: float
        hab_incubator_popuplation: _containers.RepeatedScalarFieldContainer[float]
        hab_population: _containers.RepeatedScalarFieldContainer[int]
        hab_population_indound: _containers.RepeatedScalarFieldContainer[int]
        habs: _containers.RepeatedScalarFieldContainer[int]
        hatchery_population: float
        last_cash_boost_time: float
        last_step_time: float
        num_chickens: int
        num_chickens_running: int
        num_chickens_unsettled: int
        silos_owned: int
        time_cheat_debt_DEP: float
        time_cheats_detected: int
        total_step_time: float
        train_length: _containers.RepeatedScalarFieldContainer[int]
        unclaimed_boost_tokens: int
        unclaimed_cash: float
        vehicles: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, egg_type: _Optional[_Union[Egg, str]] = ..., farm_type: _Optional[_Union[FarmType, str]] = ..., contract_id: _Optional[str] = ..., cash_earned: _Optional[float] = ..., cash_spent: _Optional[float] = ..., unclaimed_cash: _Optional[float] = ..., last_step_time: _Optional[float] = ..., num_chickens: _Optional[int] = ..., num_chickens_unsettled: _Optional[int] = ..., num_chickens_running: _Optional[int] = ..., eggs_laid: _Optional[float] = ..., eggs_shipped: _Optional[float] = ..., eggs_paid_for: _Optional[float] = ..., silos_owned: _Optional[int] = ..., habs: _Optional[_Iterable[int]] = ..., hab_population: _Optional[_Iterable[int]] = ..., hab_population_indound: _Optional[_Iterable[int]] = ..., hab_incubator_popuplation: _Optional[_Iterable[float]] = ..., hatchery_population: _Optional[float] = ..., vehicles: _Optional[_Iterable[int]] = ..., train_length: _Optional[_Iterable[int]] = ..., common_research: _Optional[_Iterable[_Union[Backup.ResearchItem, _Mapping]]] = ..., active_boosts: _Optional[_Iterable[_Union[Backup.ActiveBoost, _Mapping]]] = ..., last_cash_boost_time: _Optional[float] = ..., time_cheats_detected: _Optional[int] = ..., time_cheat_debt_DEP: _Optional[float] = ..., boost_tokens_received: _Optional[int] = ..., boost_tokens_spent: _Optional[int] = ..., boost_tokens_given: _Optional[int] = ..., unclaimed_boost_tokens: _Optional[int] = ..., gametime_until_next_boost_token: _Optional[float] = ..., total_step_time: _Optional[float] = ...) -> None: ...
    class Stats(_message.Message):
        __slots__ = ["boosts_used", "drone_takedowns", "drone_takedowns_elite", "egg_totals", "egg_totals_OLD", "iap_packs_purchased", "lost_piggy_increments", "num_piggy_breaks", "num_prestiges", "piggy_found_full", "piggy_full", "refill_uses", "time_piggy_filled_realtime", "time_piggy_full_gametime", "unlimited_chickens_uses", "video_doubler_uses", "warp_1_uses", "warp_8_uses"]
        BOOSTS_USED_FIELD_NUMBER: _ClassVar[int]
        DRONE_TAKEDOWNS_ELITE_FIELD_NUMBER: _ClassVar[int]
        DRONE_TAKEDOWNS_FIELD_NUMBER: _ClassVar[int]
        EGG_TOTALS_FIELD_NUMBER: _ClassVar[int]
        EGG_TOTALS_OLD_FIELD_NUMBER: _ClassVar[int]
        IAP_PACKS_PURCHASED_FIELD_NUMBER: _ClassVar[int]
        LOST_PIGGY_INCREMENTS_FIELD_NUMBER: _ClassVar[int]
        NUM_PIGGY_BREAKS_FIELD_NUMBER: _ClassVar[int]
        NUM_PRESTIGES_FIELD_NUMBER: _ClassVar[int]
        PIGGY_FOUND_FULL_FIELD_NUMBER: _ClassVar[int]
        PIGGY_FULL_FIELD_NUMBER: _ClassVar[int]
        REFILL_USES_FIELD_NUMBER: _ClassVar[int]
        TIME_PIGGY_FILLED_REALTIME_FIELD_NUMBER: _ClassVar[int]
        TIME_PIGGY_FULL_GAMETIME_FIELD_NUMBER: _ClassVar[int]
        UNLIMITED_CHICKENS_USES_FIELD_NUMBER: _ClassVar[int]
        VIDEO_DOUBLER_USES_FIELD_NUMBER: _ClassVar[int]
        WARP_1_USES_FIELD_NUMBER: _ClassVar[int]
        WARP_8_USES_FIELD_NUMBER: _ClassVar[int]
        boosts_used: int
        drone_takedowns: int
        drone_takedowns_elite: int
        egg_totals: _containers.RepeatedScalarFieldContainer[float]
        egg_totals_OLD: _containers.RepeatedScalarFieldContainer[int]
        iap_packs_purchased: int
        lost_piggy_increments: int
        num_piggy_breaks: int
        num_prestiges: int
        piggy_found_full: bool
        piggy_full: bool
        refill_uses: int
        time_piggy_filled_realtime: float
        time_piggy_full_gametime: float
        unlimited_chickens_uses: int
        video_doubler_uses: int
        warp_1_uses: int
        warp_8_uses: int
        def __init__(self, egg_totals_OLD: _Optional[_Iterable[int]] = ..., egg_totals: _Optional[_Iterable[float]] = ..., unlimited_chickens_uses: _Optional[int] = ..., refill_uses: _Optional[int] = ..., warp_1_uses: _Optional[int] = ..., warp_8_uses: _Optional[int] = ..., boosts_used: _Optional[int] = ..., video_doubler_uses: _Optional[int] = ..., drone_takedowns: _Optional[int] = ..., drone_takedowns_elite: _Optional[int] = ..., num_prestiges: _Optional[int] = ..., num_piggy_breaks: _Optional[int] = ..., iap_packs_purchased: _Optional[int] = ..., piggy_full: bool = ..., piggy_found_full: bool = ..., time_piggy_filled_realtime: _Optional[float] = ..., time_piggy_full_gametime: _Optional[float] = ..., lost_piggy_increments: _Optional[int] = ...) -> None: ...
    class Tutorial(_message.Message):
        __slots__ = ["buy_hab_shown", "click_tutorial_shown", "contract_info_shown", "contracts_tab_shown", "hire_vehicle_shown", "intro_shown", "join_coop_shown", "q_num_shown", "s_num_shown", "switch_farm_shown", "tutorial_shown"]
        BUY_HAB_SHOWN_FIELD_NUMBER: _ClassVar[int]
        CLICK_TUTORIAL_SHOWN_FIELD_NUMBER: _ClassVar[int]
        CONTRACTS_TAB_SHOWN_FIELD_NUMBER: _ClassVar[int]
        CONTRACT_INFO_SHOWN_FIELD_NUMBER: _ClassVar[int]
        HIRE_VEHICLE_SHOWN_FIELD_NUMBER: _ClassVar[int]
        INTRO_SHOWN_FIELD_NUMBER: _ClassVar[int]
        JOIN_COOP_SHOWN_FIELD_NUMBER: _ClassVar[int]
        Q_NUM_SHOWN_FIELD_NUMBER: _ClassVar[int]
        SWITCH_FARM_SHOWN_FIELD_NUMBER: _ClassVar[int]
        S_NUM_SHOWN_FIELD_NUMBER: _ClassVar[int]
        TUTORIAL_SHOWN_FIELD_NUMBER: _ClassVar[int]
        buy_hab_shown: bool
        click_tutorial_shown: bool
        contract_info_shown: bool
        contracts_tab_shown: bool
        hire_vehicle_shown: bool
        intro_shown: bool
        join_coop_shown: bool
        q_num_shown: bool
        s_num_shown: bool
        switch_farm_shown: bool
        tutorial_shown: _containers.RepeatedScalarFieldContainer[bool]
        def __init__(self, intro_shown: bool = ..., click_tutorial_shown: bool = ..., buy_hab_shown: bool = ..., hire_vehicle_shown: bool = ..., q_num_shown: bool = ..., s_num_shown: bool = ..., contracts_tab_shown: bool = ..., contract_info_shown: bool = ..., join_coop_shown: bool = ..., switch_farm_shown: bool = ..., tutorial_shown: _Optional[_Iterable[bool]] = ...) -> None: ...
    class Virtue(_message.Message):
        __slots__ = ["active_afx", "afx", "eggs_delivered", "eov_earned", "last_sync", "resets", "shift_count"]
        ACTIVE_AFX_FIELD_NUMBER: _ClassVar[int]
        AFX_FIELD_NUMBER: _ClassVar[int]
        EGGS_DELIVERED_FIELD_NUMBER: _ClassVar[int]
        EOV_EARNED_FIELD_NUMBER: _ClassVar[int]
        LAST_SYNC_FIELD_NUMBER: _ClassVar[int]
        RESETS_FIELD_NUMBER: _ClassVar[int]
        SHIFT_COUNT_FIELD_NUMBER: _ClassVar[int]
        active_afx: _containers.RepeatedCompositeFieldContainer[ActiveArtifactSlot]
        afx: Backup.Artifacts
        eggs_delivered: _containers.RepeatedScalarFieldContainer[float]
        eov_earned: _containers.RepeatedScalarFieldContainer[int]
        last_sync: float
        resets: int
        shift_count: int
        def __init__(self, shift_count: _Optional[int] = ..., resets: _Optional[int] = ..., eov_earned: _Optional[_Iterable[int]] = ..., eggs_delivered: _Optional[_Iterable[float]] = ..., afx: _Optional[_Union[Backup.Artifacts, _Mapping]] = ..., active_afx: _Optional[_Iterable[_Union[ActiveArtifactSlot, _Mapping]]] = ..., last_sync: _Optional[float] = ...) -> None: ...
    APPROX_TIME_FIELD_NUMBER: _ClassVar[int]
    ARTIFACTS_DB_FIELD_NUMBER: _ClassVar[int]
    ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    CONTRACTS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    EI_USER_ID_FIELD_NUMBER: _ClassVar[int]
    FARMS_FIELD_NUMBER: _ClassVar[int]
    FORCE_BACKUP_FIELD_NUMBER: _ClassVar[int]
    FORCE_OFFER_BACKUP_FIELD_NUMBER: _ClassVar[int]
    GAME_FIELD_NUMBER: _ClassVar[int]
    GAME_SERVICES_ID_FIELD_NUMBER: _ClassVar[int]
    MAIL_STATE_FIELD_NUMBER: _ClassVar[int]
    MISC_FIELD_NUMBER: _ClassVar[int]
    MISSION_FIELD_NUMBER: _ClassVar[int]
    PUSH_USER_ID_FIELD_NUMBER: _ClassVar[int]
    READ_MAIL_IDS_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SHELLS_FIELD_NUMBER: _ClassVar[int]
    SHELL_DB_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SIM_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    TUTORIAL_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    VIRTUE_FIELD_NUMBER: _ClassVar[int]
    approx_time: float
    artifacts: Backup.Artifacts
    artifacts_db: ArtifactsDB
    checksum: int
    contracts: MyContracts
    device_id: str
    ei_user_id: str
    farms: _containers.RepeatedCompositeFieldContainer[Backup.Simulation]
    force_backup: bool
    force_offer_backup: bool
    game: Backup.Game
    game_services_id: str
    mail_state: MailState
    misc: Backup.Misc
    mission: Backup.Mission
    push_user_id: str
    read_mail_ids: _containers.RepeatedScalarFieldContainer[str]
    settings: Backup.Settings
    shell_db: ShellDB
    shells: Backup.Shells
    signature: str
    sim: Backup.Simulation
    stats: Backup.Stats
    tutorial: Backup.Tutorial
    user_id: str
    user_name: str
    version: int
    virtue: Backup.Virtue
    def __init__(self, user_id: _Optional[str] = ..., ei_user_id: _Optional[str] = ..., game_services_id: _Optional[str] = ..., push_user_id: _Optional[str] = ..., device_id: _Optional[str] = ..., user_name: _Optional[str] = ..., approx_time: _Optional[float] = ..., version: _Optional[int] = ..., force_offer_backup: bool = ..., force_backup: bool = ..., settings: _Optional[_Union[Backup.Settings, _Mapping]] = ..., tutorial: _Optional[_Union[Backup.Tutorial, _Mapping]] = ..., stats: _Optional[_Union[Backup.Stats, _Mapping]] = ..., game: _Optional[_Union[Backup.Game, _Mapping]] = ..., artifacts: _Optional[_Union[Backup.Artifacts, _Mapping]] = ..., virtue: _Optional[_Union[Backup.Virtue, _Mapping]] = ..., shells: _Optional[_Union[Backup.Shells, _Mapping]] = ..., sim: _Optional[_Union[Backup.Simulation, _Mapping]] = ..., farms: _Optional[_Iterable[_Union[Backup.Simulation, _Mapping]]] = ..., mission: _Optional[_Union[Backup.Mission, _Mapping]] = ..., misc: _Optional[_Union[Backup.Misc, _Mapping]] = ..., contracts: _Optional[_Union[MyContracts, _Mapping]] = ..., artifacts_db: _Optional[_Union[ArtifactsDB, _Mapping]] = ..., shell_db: _Optional[_Union[ShellDB, _Mapping]] = ..., read_mail_ids: _Optional[_Iterable[str]] = ..., mail_state: _Optional[_Union[MailState, _Mapping]] = ..., checksum: _Optional[int] = ..., signature: _Optional[str] = ...) -> None: ...

class BasicRequestInfo(_message.Message):
    __slots__ = ["build", "client_version", "country", "debug", "ei_user_id", "language", "platform", "version"]
    BUILD_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    DEBUG_FIELD_NUMBER: _ClassVar[int]
    EI_USER_ID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    build: str
    client_version: int
    country: str
    debug: bool
    ei_user_id: str
    language: str
    platform: str
    version: str
    def __init__(self, ei_user_id: _Optional[str] = ..., client_version: _Optional[int] = ..., version: _Optional[str] = ..., build: _Optional[str] = ..., platform: _Optional[str] = ..., country: _Optional[str] = ..., language: _Optional[str] = ..., debug: bool = ...) -> None: ...

class CXPEvalRolloutInfo(_message.Message):
    __slots__ = ["basis_points", "current_id"]
    BASIS_POINTS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_ID_FIELD_NUMBER: _ClassVar[int]
    basis_points: int
    current_id: str
    def __init__(self, current_id: _Optional[str] = ..., basis_points: _Optional[int] = ...) -> None: ...

class CleanAccountRequest(_message.Message):
    __slots__ = ["ei_user_id_to_keep", "game_services_id"]
    EI_USER_ID_TO_KEEP_FIELD_NUMBER: _ClassVar[int]
    GAME_SERVICES_ID_FIELD_NUMBER: _ClassVar[int]
    ei_user_id_to_keep: str
    game_services_id: str
    def __init__(self, ei_user_id_to_keep: _Optional[str] = ..., game_services_id: _Optional[str] = ...) -> None: ...

class ClearAllUserDataRequest(_message.Message):
    __slots__ = ["backup_checksum", "device_id", "rinfo", "user_id"]
    BACKUP_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    backup_checksum: int
    device_id: str
    rinfo: BasicRequestInfo
    user_id: str
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., user_id: _Optional[str] = ..., device_id: _Optional[str] = ..., backup_checksum: _Optional[int] = ...) -> None: ...

class CollectContractArtifactRewardsRequest(_message.Message):
    __slots__ = ["best_ship", "contract_identifier", "goal_index", "grade", "league", "rinfo"]
    BEST_SHIP_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    GOAL_INDEX_FIELD_NUMBER: _ClassVar[int]
    GRADE_FIELD_NUMBER: _ClassVar[int]
    LEAGUE_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    best_ship: MissionInfo.Spaceship
    contract_identifier: str
    goal_index: int
    grade: Contract.PlayerGrade
    league: int
    rinfo: BasicRequestInfo
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., contract_identifier: _Optional[str] = ..., league: _Optional[int] = ..., grade: _Optional[_Union[Contract.PlayerGrade, str]] = ..., goal_index: _Optional[int] = ..., best_ship: _Optional[_Union[MissionInfo.Spaceship, str]] = ...) -> None: ...

class CollectSeasonArtifactRewardsRequest(_message.Message):
    __slots__ = ["best_ship", "cxp", "rinfo", "season_identifier"]
    BEST_SHIP_FIELD_NUMBER: _ClassVar[int]
    CXP_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    SEASON_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    best_ship: MissionInfo.Spaceship
    cxp: float
    rinfo: BasicRequestInfo
    season_identifier: str
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., season_identifier: _Optional[str] = ..., cxp: _Optional[float] = ..., best_ship: _Optional[_Union[MissionInfo.Spaceship, str]] = ...) -> None: ...

class CompleteArtifact(_message.Message):
    __slots__ = ["spec", "stones"]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STONES_FIELD_NUMBER: _ClassVar[int]
    spec: ArtifactSpec
    stones: _containers.RepeatedCompositeFieldContainer[ArtifactSpec]
    def __init__(self, spec: _Optional[_Union[ArtifactSpec, _Mapping]] = ..., stones: _Optional[_Iterable[_Union[ArtifactSpec, _Mapping]]] = ...) -> None: ...

class CompleteMissionResponse(_message.Message):
    __slots__ = ["artifacts", "ei_user_id", "info", "other_rewards", "success"]
    class SecureArtifactSpec(_message.Message):
        __slots__ = ["server_id", "spec"]
        SERVER_ID_FIELD_NUMBER: _ClassVar[int]
        SPEC_FIELD_NUMBER: _ClassVar[int]
        server_id: str
        spec: ArtifactSpec
        def __init__(self, spec: _Optional[_Union[ArtifactSpec, _Mapping]] = ..., server_id: _Optional[str] = ...) -> None: ...
    ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    EI_USER_ID_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    OTHER_REWARDS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    artifacts: _containers.RepeatedCompositeFieldContainer[CompleteMissionResponse.SecureArtifactSpec]
    ei_user_id: str
    info: MissionInfo
    other_rewards: _containers.RepeatedCompositeFieldContainer[Reward]
    success: bool
    def __init__(self, success: bool = ..., info: _Optional[_Union[MissionInfo, _Mapping]] = ..., artifacts: _Optional[_Iterable[_Union[CompleteMissionResponse.SecureArtifactSpec, _Mapping]]] = ..., other_rewards: _Optional[_Iterable[_Union[Reward, _Mapping]]] = ..., ei_user_id: _Optional[str] = ...) -> None: ...

class ConfigRequest(_message.Message):
    __slots__ = ["artifacts_unlocked", "contracts_unlocked", "fuel_tank_unlocked", "pro_permit", "rinfo", "soul_eggs", "tips_checksum", "ultra"]
    ARTIFACTS_UNLOCKED_FIELD_NUMBER: _ClassVar[int]
    CONTRACTS_UNLOCKED_FIELD_NUMBER: _ClassVar[int]
    FUEL_TANK_UNLOCKED_FIELD_NUMBER: _ClassVar[int]
    PRO_PERMIT_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    SOUL_EGGS_FIELD_NUMBER: _ClassVar[int]
    TIPS_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    ULTRA_FIELD_NUMBER: _ClassVar[int]
    artifacts_unlocked: bool
    contracts_unlocked: bool
    fuel_tank_unlocked: bool
    pro_permit: bool
    rinfo: BasicRequestInfo
    soul_eggs: float
    tips_checksum: str
    ultra: bool
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., soul_eggs: _Optional[float] = ..., contracts_unlocked: bool = ..., artifacts_unlocked: bool = ..., fuel_tank_unlocked: bool = ..., pro_permit: bool = ..., ultra: bool = ..., tips_checksum: _Optional[str] = ...) -> None: ...

class ConfigResponse(_message.Message):
    __slots__ = ["dlc_catalog", "live_config", "mail_bag"]
    DLC_CATALOG_FIELD_NUMBER: _ClassVar[int]
    LIVE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MAIL_BAG_FIELD_NUMBER: _ClassVar[int]
    dlc_catalog: DLCCatalog
    live_config: LiveConfig
    mail_bag: MailDB
    def __init__(self, live_config: _Optional[_Union[LiveConfig, _Mapping]] = ..., mail_bag: _Optional[_Union[MailDB, _Mapping]] = ..., dlc_catalog: _Optional[_Union[DLCCatalog, _Mapping]] = ...) -> None: ...

class ConsumeArtifactRequest(_message.Message):
    __slots__ = ["additional_item_ids", "additional_server_ids", "artifact_server_id", "ei_user_id", "original_item_id", "quantity", "rinfo", "spec"]
    ADDITIONAL_ITEM_IDS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_SERVER_IDS_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    EI_USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    additional_item_ids: _containers.RepeatedScalarFieldContainer[int]
    additional_server_ids: _containers.RepeatedScalarFieldContainer[str]
    artifact_server_id: str
    ei_user_id: str
    original_item_id: int
    quantity: int
    rinfo: BasicRequestInfo
    spec: ArtifactSpec
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., ei_user_id: _Optional[str] = ..., spec: _Optional[_Union[ArtifactSpec, _Mapping]] = ..., artifact_server_id: _Optional[str] = ..., original_item_id: _Optional[int] = ..., additional_server_ids: _Optional[_Iterable[str]] = ..., additional_item_ids: _Optional[_Iterable[int]] = ..., quantity: _Optional[int] = ...) -> None: ...

class ConsumeArtifactResponse(_message.Message):
    __slots__ = ["additional_item_ids", "byproducts", "ei_user_id", "original_item_id", "other_rewards", "success"]
    ADDITIONAL_ITEM_IDS_FIELD_NUMBER: _ClassVar[int]
    BYPRODUCTS_FIELD_NUMBER: _ClassVar[int]
    EI_USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    OTHER_REWARDS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    additional_item_ids: _containers.RepeatedScalarFieldContainer[int]
    byproducts: _containers.RepeatedCompositeFieldContainer[ArtifactSpec]
    ei_user_id: str
    original_item_id: int
    other_rewards: _containers.RepeatedCompositeFieldContainer[Reward]
    success: bool
    def __init__(self, success: bool = ..., original_item_id: _Optional[int] = ..., additional_item_ids: _Optional[_Iterable[int]] = ..., byproducts: _Optional[_Iterable[_Union[ArtifactSpec, _Mapping]]] = ..., other_rewards: _Optional[_Iterable[_Union[Reward, _Mapping]]] = ..., ei_user_id: _Optional[str] = ...) -> None: ...

class Contract(_message.Message):
    __slots__ = ["cc_only", "chicken_run_cooldown_minutes", "coop_allowed", "custom_egg_id", "debug", "default_shell_ids", "description", "egg", "expiration_time", "goal_sets", "goals", "grade_specs", "identifier", "key", "leggacy", "length_seconds", "max_boosts", "max_coop_size", "max_soul_eggs", "min_client_version", "minutes_per_token", "name", "season_id", "start_time"]
    class PlayerGrade(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Goal(_message.Message):
        __slots__ = ["reward_amount", "reward_sub_type", "reward_type", "target_amount", "target_soul_eggs", "type"]
        REWARD_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        REWARD_SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
        REWARD_TYPE_FIELD_NUMBER: _ClassVar[int]
        TARGET_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        TARGET_SOUL_EGGS_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        reward_amount: float
        reward_sub_type: str
        reward_type: RewardType
        target_amount: float
        target_soul_eggs: float
        type: GoalType
        def __init__(self, type: _Optional[_Union[GoalType, str]] = ..., target_amount: _Optional[float] = ..., reward_type: _Optional[_Union[RewardType, str]] = ..., reward_sub_type: _Optional[str] = ..., reward_amount: _Optional[float] = ..., target_soul_eggs: _Optional[float] = ...) -> None: ...
    class GoalSet(_message.Message):
        __slots__ = ["goals"]
        GOALS_FIELD_NUMBER: _ClassVar[int]
        goals: _containers.RepeatedCompositeFieldContainer[Contract.Goal]
        def __init__(self, goals: _Optional[_Iterable[_Union[Contract.Goal, _Mapping]]] = ...) -> None: ...
    class GradeSpec(_message.Message):
        __slots__ = ["goals", "grade", "length_seconds", "modifiers"]
        GOALS_FIELD_NUMBER: _ClassVar[int]
        GRADE_FIELD_NUMBER: _ClassVar[int]
        LENGTH_SECONDS_FIELD_NUMBER: _ClassVar[int]
        MODIFIERS_FIELD_NUMBER: _ClassVar[int]
        goals: _containers.RepeatedCompositeFieldContainer[Contract.Goal]
        grade: Contract.PlayerGrade
        length_seconds: float
        modifiers: _containers.RepeatedCompositeFieldContainer[GameModifier]
        def __init__(self, grade: _Optional[_Union[Contract.PlayerGrade, str]] = ..., goals: _Optional[_Iterable[_Union[Contract.Goal, _Mapping]]] = ..., modifiers: _Optional[_Iterable[_Union[GameModifier, _Mapping]]] = ..., length_seconds: _Optional[float] = ...) -> None: ...
    CC_ONLY_FIELD_NUMBER: _ClassVar[int]
    CHICKEN_RUN_COOLDOWN_MINUTES_FIELD_NUMBER: _ClassVar[int]
    COOP_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_EGG_ID_FIELD_NUMBER: _ClassVar[int]
    DEBUG_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SHELL_IDS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EGG_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    GOALS_FIELD_NUMBER: _ClassVar[int]
    GOAL_SETS_FIELD_NUMBER: _ClassVar[int]
    GRADE_A: Contract.PlayerGrade
    GRADE_AA: Contract.PlayerGrade
    GRADE_AAA: Contract.PlayerGrade
    GRADE_B: Contract.PlayerGrade
    GRADE_C: Contract.PlayerGrade
    GRADE_SPECS_FIELD_NUMBER: _ClassVar[int]
    GRADE_UNSET: Contract.PlayerGrade
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    LEGGACY_FIELD_NUMBER: _ClassVar[int]
    LENGTH_SECONDS_FIELD_NUMBER: _ClassVar[int]
    MAX_BOOSTS_FIELD_NUMBER: _ClassVar[int]
    MAX_COOP_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAX_SOUL_EGGS_FIELD_NUMBER: _ClassVar[int]
    MINUTES_PER_TOKEN_FIELD_NUMBER: _ClassVar[int]
    MIN_CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SEASON_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    cc_only: bool
    chicken_run_cooldown_minutes: float
    coop_allowed: bool
    custom_egg_id: str
    debug: bool
    default_shell_ids: _containers.RepeatedScalarFieldContainer[str]
    description: str
    egg: Egg
    expiration_time: float
    goal_sets: _containers.RepeatedCompositeFieldContainer[Contract.GoalSet]
    goals: _containers.RepeatedCompositeFieldContainer[Contract.Goal]
    grade_specs: _containers.RepeatedCompositeFieldContainer[Contract.GradeSpec]
    identifier: str
    key: str
    leggacy: bool
    length_seconds: float
    max_boosts: int
    max_coop_size: int
    max_soul_eggs: float
    min_client_version: int
    minutes_per_token: float
    name: str
    season_id: str
    start_time: float
    def __init__(self, identifier: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., egg: _Optional[_Union[Egg, str]] = ..., custom_egg_id: _Optional[str] = ..., goals: _Optional[_Iterable[_Union[Contract.Goal, _Mapping]]] = ..., goal_sets: _Optional[_Iterable[_Union[Contract.GoalSet, _Mapping]]] = ..., grade_specs: _Optional[_Iterable[_Union[Contract.GradeSpec, _Mapping]]] = ..., season_id: _Optional[str] = ..., coop_allowed: bool = ..., max_coop_size: _Optional[int] = ..., max_boosts: _Optional[int] = ..., minutes_per_token: _Optional[float] = ..., chicken_run_cooldown_minutes: _Optional[float] = ..., start_time: _Optional[float] = ..., expiration_time: _Optional[float] = ..., length_seconds: _Optional[float] = ..., max_soul_eggs: _Optional[float] = ..., min_client_version: _Optional[int] = ..., leggacy: bool = ..., cc_only: bool = ..., default_shell_ids: _Optional[_Iterable[str]] = ..., debug: bool = ..., key: _Optional[str] = ...) -> None: ...

class ContractAction(_message.Message):
    __slots__ = ["action_name", "approx_time", "autojoin", "boost_id", "cc_only", "contract_id", "coop_id", "dest_user_id", "goal_index", "grade", "kick_reason", "points_replay", "public", "replay", "reward_amount", "reward_subtype", "reward_type", "tokens", "user_id"]
    ACTION_NAME_FIELD_NUMBER: _ClassVar[int]
    APPROX_TIME_FIELD_NUMBER: _ClassVar[int]
    AUTOJOIN_FIELD_NUMBER: _ClassVar[int]
    BOOST_ID_FIELD_NUMBER: _ClassVar[int]
    CC_ONLY_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    COOP_ID_FIELD_NUMBER: _ClassVar[int]
    DEST_USER_ID_FIELD_NUMBER: _ClassVar[int]
    GOAL_INDEX_FIELD_NUMBER: _ClassVar[int]
    GRADE_FIELD_NUMBER: _ClassVar[int]
    KICK_REASON_FIELD_NUMBER: _ClassVar[int]
    POINTS_REPLAY_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    REPLAY_FIELD_NUMBER: _ClassVar[int]
    REWARD_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    REWARD_SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    REWARD_TYPE_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    action_name: str
    approx_time: float
    autojoin: bool
    boost_id: str
    cc_only: bool
    contract_id: str
    coop_id: str
    dest_user_id: str
    goal_index: int
    grade: int
    kick_reason: int
    points_replay: bool
    public: bool
    replay: bool
    reward_amount: float
    reward_subtype: str
    reward_type: int
    tokens: int
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., action_name: _Optional[str] = ..., approx_time: _Optional[float] = ..., dest_user_id: _Optional[str] = ..., contract_id: _Optional[str] = ..., coop_id: _Optional[str] = ..., autojoin: bool = ..., grade: _Optional[int] = ..., replay: bool = ..., points_replay: bool = ..., reward_type: _Optional[int] = ..., reward_subtype: _Optional[str] = ..., reward_amount: _Optional[float] = ..., goal_index: _Optional[int] = ..., boost_id: _Optional[str] = ..., tokens: _Optional[int] = ..., kick_reason: _Optional[int] = ..., public: bool = ..., cc_only: bool = ...) -> None: ...

class ContractCitation(_message.Message):
    __slots__ = ["grade", "issue", "timestamp"]
    GRADE_FIELD_NUMBER: _ClassVar[int]
    ISSUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    grade: Contract.PlayerGrade
    issue: ContractEvaluation.PoorBehavior
    timestamp: float
    def __init__(self, issue: _Optional[_Union[ContractEvaluation.PoorBehavior, str]] = ..., timestamp: _Optional[float] = ..., grade: _Optional[_Union[Contract.PlayerGrade, str]] = ...) -> None: ...

class ContractCoopStatusRequest(_message.Message):
    __slots__ = ["client_timestamp", "client_version", "contract_identifier", "coop_identifier", "rinfo", "user_id"]
    CLIENT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    COOP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    client_timestamp: float
    client_version: int
    contract_identifier: str
    coop_identifier: str
    rinfo: BasicRequestInfo
    user_id: str
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., contract_identifier: _Optional[str] = ..., coop_identifier: _Optional[str] = ..., user_id: _Optional[str] = ..., client_version: _Optional[int] = ..., client_timestamp: _Optional[float] = ...) -> None: ...

class ContractCoopStatusResponse(_message.Message):
    __slots__ = ["all_goals_achieved", "all_members_reporting", "auto_generated", "background_sync", "chicken_runs", "cleared_for_exit", "client_timestamp", "contract_identifier", "contributors", "coop_identifier", "creator_id", "gifts", "grace_period_seconds_remaining", "grade", "last_sync_DEP", "public", "response_status", "seconds_remaining", "seconds_since_all_goals_achieved", "total_amount"]
    class MemberStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class ResponseStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class ChickenRun(_message.Message):
        __slots__ = ["amount", "user_id", "user_name"]
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        USER_NAME_FIELD_NUMBER: _ClassVar[int]
        amount: int
        user_id: str
        user_name: str
        def __init__(self, user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., amount: _Optional[int] = ...) -> None: ...
    class ContributionInfo(_message.Message):
        __slots__ = ["active", "autojoined", "ban_votes", "boost_tokens", "boost_tokens_spent", "buff_history", "cc_member", "chicken_run_cooldown", "contract_identifier", "contribution_amount", "contribution_rate", "farm_info", "finalized", "leech", "platform", "production_params", "push_id", "rank_change", "recently_active", "soul_power", "time_cheat_detected", "user_id", "user_name", "uuid"]
        ACTIVE_FIELD_NUMBER: _ClassVar[int]
        AUTOJOINED_FIELD_NUMBER: _ClassVar[int]
        BAN_VOTES_FIELD_NUMBER: _ClassVar[int]
        BOOST_TOKENS_FIELD_NUMBER: _ClassVar[int]
        BOOST_TOKENS_SPENT_FIELD_NUMBER: _ClassVar[int]
        BUFF_HISTORY_FIELD_NUMBER: _ClassVar[int]
        CC_MEMBER_FIELD_NUMBER: _ClassVar[int]
        CHICKEN_RUN_COOLDOWN_FIELD_NUMBER: _ClassVar[int]
        CONTRACT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        CONTRIBUTION_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        CONTRIBUTION_RATE_FIELD_NUMBER: _ClassVar[int]
        FARM_INFO_FIELD_NUMBER: _ClassVar[int]
        FINALIZED_FIELD_NUMBER: _ClassVar[int]
        LEECH_FIELD_NUMBER: _ClassVar[int]
        PLATFORM_FIELD_NUMBER: _ClassVar[int]
        PRODUCTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
        PUSH_ID_FIELD_NUMBER: _ClassVar[int]
        RANK_CHANGE_FIELD_NUMBER: _ClassVar[int]
        RECENTLY_ACTIVE_FIELD_NUMBER: _ClassVar[int]
        SOUL_POWER_FIELD_NUMBER: _ClassVar[int]
        TIME_CHEAT_DETECTED_FIELD_NUMBER: _ClassVar[int]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        USER_NAME_FIELD_NUMBER: _ClassVar[int]
        UUID_FIELD_NUMBER: _ClassVar[int]
        active: bool
        autojoined: bool
        ban_votes: int
        boost_tokens: int
        boost_tokens_spent: int
        buff_history: _containers.RepeatedCompositeFieldContainer[CoopBuffState]
        cc_member: bool
        chicken_run_cooldown: float
        contract_identifier: str
        contribution_amount: float
        contribution_rate: float
        farm_info: PlayerFarmInfo
        finalized: bool
        leech: bool
        platform: Platform
        production_params: FarmProductionParams
        push_id: str
        rank_change: int
        recently_active: bool
        soul_power: float
        time_cheat_detected: bool
        user_id: str
        user_name: str
        uuid: str
        def __init__(self, uuid: _Optional[str] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., contract_identifier: _Optional[str] = ..., contribution_amount: _Optional[float] = ..., contribution_rate: _Optional[float] = ..., soul_power: _Optional[float] = ..., production_params: _Optional[_Union[FarmProductionParams, _Mapping]] = ..., farm_info: _Optional[_Union[PlayerFarmInfo, _Mapping]] = ..., rank_change: _Optional[int] = ..., recently_active: bool = ..., active: bool = ..., cc_member: bool = ..., leech: bool = ..., finalized: bool = ..., time_cheat_detected: bool = ..., platform: _Optional[_Union[Platform, str]] = ..., push_id: _Optional[str] = ..., ban_votes: _Optional[int] = ..., autojoined: bool = ..., boost_tokens: _Optional[int] = ..., boost_tokens_spent: _Optional[int] = ..., buff_history: _Optional[_Iterable[_Union[CoopBuffState, _Mapping]]] = ..., chicken_run_cooldown: _Optional[float] = ...) -> None: ...
    class CoopGift(_message.Message):
        __slots__ = ["amount", "tracking", "user_id", "user_name"]
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        TRACKING_FIELD_NUMBER: _ClassVar[int]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        USER_NAME_FIELD_NUMBER: _ClassVar[int]
        amount: int
        tracking: str
        user_id: str
        user_name: str
        def __init__(self, user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., amount: _Optional[int] = ..., tracking: _Optional[str] = ...) -> None: ...
    ACTIVE: ContractCoopStatusResponse.Status
    ALL_GOALS_ACHIEVED_FIELD_NUMBER: _ClassVar[int]
    ALL_MEMBERS_REPORTING_FIELD_NUMBER: _ClassVar[int]
    AUTO_GENERATED_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_SYNC_FIELD_NUMBER: _ClassVar[int]
    CHICKEN_RUNS_FIELD_NUMBER: _ClassVar[int]
    CLEARED_FOR_EXIT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    COMPLETE: ContractCoopStatusResponse.Status
    CONTRACT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_NOT_FOUND: ContractCoopStatusResponse.ResponseStatus
    CONTRIBUTORS_FIELD_NUMBER: _ClassVar[int]
    COOP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    COOP_NOT_FOUND: ContractCoopStatusResponse.ResponseStatus
    CREATOR_ID_FIELD_NUMBER: _ClassVar[int]
    FINALIZED: ContractCoopStatusResponse.Status
    GIFTS_FIELD_NUMBER: _ClassVar[int]
    GRACE_PERIOD_SECONDS_REMAINING_FIELD_NUMBER: _ClassVar[int]
    GRADE_FIELD_NUMBER: _ClassVar[int]
    INVALID_MEMBERSHIP: ContractCoopStatusResponse.ResponseStatus
    KICKED_CHEATS: ContractCoopStatusResponse.MemberStatus
    KICKED_INACTIVE: ContractCoopStatusResponse.MemberStatus
    KICKED_LEECH: ContractCoopStatusResponse.MemberStatus
    KICKED_PRIVATE: ContractCoopStatusResponse.MemberStatus
    LAST_SYNC_DEP_FIELD_NUMBER: _ClassVar[int]
    LOBBY: ContractCoopStatusResponse.Status
    MEMBERSHIP_NOT_FOUND: ContractCoopStatusResponse.ResponseStatus
    MISSING_CONTRACT_ID: ContractCoopStatusResponse.ResponseStatus
    MISSING_COOP_ID: ContractCoopStatusResponse.ResponseStatus
    MISSING_USER: ContractCoopStatusResponse.ResponseStatus
    NO_ERROR: ContractCoopStatusResponse.ResponseStatus
    NO_HTTP_RESPONSE: ContractCoopStatusResponse.ResponseStatus
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STATUS_FIELD_NUMBER: _ClassVar[int]
    SECONDS_REMAINING_FIELD_NUMBER: _ClassVar[int]
    SECONDS_SINCE_ALL_GOALS_ACHIEVED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN: ContractCoopStatusResponse.Status
    VALID: ContractCoopStatusResponse.MemberStatus
    all_goals_achieved: bool
    all_members_reporting: bool
    auto_generated: bool
    background_sync: bool
    chicken_runs: _containers.RepeatedCompositeFieldContainer[ContractCoopStatusResponse.ChickenRun]
    cleared_for_exit: bool
    client_timestamp: float
    contract_identifier: str
    contributors: _containers.RepeatedCompositeFieldContainer[ContractCoopStatusResponse.ContributionInfo]
    coop_identifier: str
    creator_id: str
    gifts: _containers.RepeatedCompositeFieldContainer[ContractCoopStatusResponse.CoopGift]
    grace_period_seconds_remaining: float
    grade: Contract.PlayerGrade
    last_sync_DEP: float
    public: bool
    response_status: ContractCoopStatusResponse.ResponseStatus
    seconds_remaining: float
    seconds_since_all_goals_achieved: float
    total_amount: float
    def __init__(self, response_status: _Optional[_Union[ContractCoopStatusResponse.ResponseStatus, str]] = ..., contract_identifier: _Optional[str] = ..., total_amount: _Optional[float] = ..., coop_identifier: _Optional[str] = ..., grade: _Optional[_Union[Contract.PlayerGrade, str]] = ..., contributors: _Optional[_Iterable[_Union[ContractCoopStatusResponse.ContributionInfo, _Mapping]]] = ..., auto_generated: bool = ..., public: bool = ..., creator_id: _Optional[str] = ..., seconds_remaining: _Optional[float] = ..., seconds_since_all_goals_achieved: _Optional[float] = ..., all_goals_achieved: bool = ..., all_members_reporting: bool = ..., grace_period_seconds_remaining: _Optional[float] = ..., cleared_for_exit: bool = ..., gifts: _Optional[_Iterable[_Union[ContractCoopStatusResponse.CoopGift, _Mapping]]] = ..., chicken_runs: _Optional[_Iterable[_Union[ContractCoopStatusResponse.ChickenRun, _Mapping]]] = ..., client_timestamp: _Optional[float] = ..., background_sync: bool = ..., last_sync_DEP: _Optional[float] = ...) -> None: ...

class ContractCoopStatusUpdateRequest(_message.Message):
    __slots__ = ["amount", "boost_tokens", "boost_tokens_spent", "contract_identifier", "coop_identifier", "earnings_buff", "egg_laying_rate_buff", "eop", "farm_info", "hide_cc_status", "last_idle_summary", "production_params", "push_user_id", "rate", "rinfo", "soul_power", "time_cheats_detected", "total_step_time", "user_id"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    BOOST_TOKENS_FIELD_NUMBER: _ClassVar[int]
    BOOST_TOKENS_SPENT_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    COOP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    EARNINGS_BUFF_FIELD_NUMBER: _ClassVar[int]
    EGG_LAYING_RATE_BUFF_FIELD_NUMBER: _ClassVar[int]
    EOP_FIELD_NUMBER: _ClassVar[int]
    FARM_INFO_FIELD_NUMBER: _ClassVar[int]
    HIDE_CC_STATUS_FIELD_NUMBER: _ClassVar[int]
    LAST_IDLE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    PRODUCTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PUSH_USER_ID_FIELD_NUMBER: _ClassVar[int]
    RATE_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    SOUL_POWER_FIELD_NUMBER: _ClassVar[int]
    TIME_CHEATS_DETECTED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_STEP_TIME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    amount: float
    boost_tokens: int
    boost_tokens_spent: int
    contract_identifier: str
    coop_identifier: str
    earnings_buff: float
    egg_laying_rate_buff: float
    eop: int
    farm_info: PlayerFarmInfo
    hide_cc_status: bool
    last_idle_summary: IdleSessionSummary
    production_params: FarmProductionParams
    push_user_id: str
    rate: float
    rinfo: BasicRequestInfo
    soul_power: float
    time_cheats_detected: int
    total_step_time: float
    user_id: str
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., user_id: _Optional[str] = ..., contract_identifier: _Optional[str] = ..., coop_identifier: _Optional[str] = ..., push_user_id: _Optional[str] = ..., amount: _Optional[float] = ..., rate: _Optional[float] = ..., time_cheats_detected: _Optional[int] = ..., total_step_time: _Optional[float] = ..., soul_power: _Optional[float] = ..., eop: _Optional[int] = ..., boost_tokens: _Optional[int] = ..., boost_tokens_spent: _Optional[int] = ..., hide_cc_status: bool = ..., production_params: _Optional[_Union[FarmProductionParams, _Mapping]] = ..., farm_info: _Optional[_Union[PlayerFarmInfo, _Mapping]] = ..., last_idle_summary: _Optional[_Union[IdleSessionSummary, _Mapping]] = ..., egg_laying_rate_buff: _Optional[float] = ..., earnings_buff: _Optional[float] = ...) -> None: ...

class ContractCoopStatusUpdateResponse(_message.Message):
    __slots__ = ["exists", "finalized", "status"]
    EXISTS_FIELD_NUMBER: _ClassVar[int]
    FINALIZED_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    exists: bool
    finalized: bool
    status: ContractCoopStatusResponse.MemberStatus
    def __init__(self, finalized: bool = ..., exists: bool = ..., status: _Optional[_Union[ContractCoopStatusResponse.MemberStatus, str]] = ...) -> None: ...

class ContractEvaluation(_message.Message):
    __slots__ = ["boost_token_allotment", "buff_time_value", "chicken_runs_sent", "completion_percent", "completion_time", "contract_identifier", "contribution_ratio", "coop_identifier", "coop_size", "counted_in_season", "cxp", "cxp_change", "evaluation_start_time", "extra_players", "gift_token_value_received", "gift_token_value_sent", "gift_tokens_received", "gift_tokens_sent", "grade", "grade_performance", "issues", "last_contribution_time", "notes", "old_goals", "old_league", "original_length", "other_bonuses", "replay", "season_id", "solo", "soul_power", "status", "teamwork_score", "time_cheats", "version"]
    class PoorBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ABANDONED_COOP: ContractEvaluation.PoorBehavior
    BAD_CONTRIBUTION: ContractEvaluation.PoorBehavior
    BOOST_TOKEN_ALLOTMENT_FIELD_NUMBER: _ClassVar[int]
    BUFF_TIME_VALUE_FIELD_NUMBER: _ClassVar[int]
    CHICKEN_RUNS_SENT_FIELD_NUMBER: _ClassVar[int]
    COMPLETE: ContractEvaluation.Status
    COMPLETION_PERCENT_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_TIME_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    CONTRIBUTION_RATIO_FIELD_NUMBER: _ClassVar[int]
    COOP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    COOP_SIZE_FIELD_NUMBER: _ClassVar[int]
    COUNTED_IN_SEASON_FIELD_NUMBER: _ClassVar[int]
    CXP_CHANGE_FIELD_NUMBER: _ClassVar[int]
    CXP_FIELD_NUMBER: _ClassVar[int]
    DISHONORABLY_DISCHARGED: ContractEvaluation.PoorBehavior
    EVALUATING: ContractEvaluation.Status
    EVALUATION_START_TIME_FIELD_NUMBER: _ClassVar[int]
    EXTRA_PLAYERS_FIELD_NUMBER: _ClassVar[int]
    GIFT_TOKENS_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    GIFT_TOKENS_SENT_FIELD_NUMBER: _ClassVar[int]
    GIFT_TOKEN_VALUE_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    GIFT_TOKEN_VALUE_SENT_FIELD_NUMBER: _ClassVar[int]
    GRADE_FIELD_NUMBER: _ClassVar[int]
    GRADE_PERFORMANCE_FIELD_NUMBER: _ClassVar[int]
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    LAST_CONTRIBUTION_TIME_FIELD_NUMBER: _ClassVar[int]
    LOW_CONTRIBUTION: ContractEvaluation.PoorBehavior
    NONE: ContractEvaluation.PoorBehavior
    NOTES_FIELD_NUMBER: _ClassVar[int]
    OLD_GOALS_FIELD_NUMBER: _ClassVar[int]
    OLD_LEAGUE_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_LENGTH_FIELD_NUMBER: _ClassVar[int]
    OTHER_BONUSES_FIELD_NUMBER: _ClassVar[int]
    PENDING: ContractEvaluation.Status
    POOR_TEAMWORK: ContractEvaluation.PoorBehavior
    REPLAY_FIELD_NUMBER: _ClassVar[int]
    SEASON_ID_FIELD_NUMBER: _ClassVar[int]
    SOLO_FIELD_NUMBER: _ClassVar[int]
    SOUL_POWER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TEAMWORK_SCORE_FIELD_NUMBER: _ClassVar[int]
    TIME_CHEAT: ContractEvaluation.PoorBehavior
    TIME_CHEATS_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN: ContractEvaluation.Status
    VERSION_FIELD_NUMBER: _ClassVar[int]
    boost_token_allotment: int
    buff_time_value: float
    chicken_runs_sent: int
    completion_percent: float
    completion_time: float
    contract_identifier: str
    contribution_ratio: float
    coop_identifier: str
    coop_size: int
    counted_in_season: bool
    cxp: float
    cxp_change: float
    evaluation_start_time: float
    extra_players: int
    gift_token_value_received: float
    gift_token_value_sent: float
    gift_tokens_received: int
    gift_tokens_sent: int
    grade: Contract.PlayerGrade
    grade_performance: int
    issues: _containers.RepeatedScalarFieldContainer[ContractEvaluation.PoorBehavior]
    last_contribution_time: float
    notes: _containers.RepeatedScalarFieldContainer[str]
    old_goals: bool
    old_league: int
    original_length: float
    other_bonuses: float
    replay: bool
    season_id: str
    solo: bool
    soul_power: float
    status: ContractEvaluation.Status
    teamwork_score: float
    time_cheats: int
    version: str
    def __init__(self, contract_identifier: _Optional[str] = ..., coop_identifier: _Optional[str] = ..., cxp: _Optional[float] = ..., replay: bool = ..., cxp_change: _Optional[float] = ..., grade_performance: _Optional[int] = ..., old_league: _Optional[int] = ..., old_goals: bool = ..., grade: _Optional[_Union[Contract.PlayerGrade, str]] = ..., contribution_ratio: _Optional[float] = ..., completion_percent: _Optional[float] = ..., original_length: _Optional[float] = ..., coop_size: _Optional[int] = ..., solo: bool = ..., soul_power: _Optional[float] = ..., last_contribution_time: _Optional[float] = ..., completion_time: _Optional[float] = ..., chicken_runs_sent: _Optional[int] = ..., gift_tokens_sent: _Optional[int] = ..., gift_tokens_received: _Optional[int] = ..., gift_token_value_sent: _Optional[float] = ..., gift_token_value_received: _Optional[float] = ..., boost_token_allotment: _Optional[int] = ..., buff_time_value: _Optional[float] = ..., teamwork_score: _Optional[float] = ..., other_bonuses: _Optional[float] = ..., counted_in_season: bool = ..., season_id: _Optional[str] = ..., time_cheats: _Optional[int] = ..., extra_players: _Optional[int] = ..., issues: _Optional[_Iterable[_Union[ContractEvaluation.PoorBehavior, str]]] = ..., notes: _Optional[_Iterable[str]] = ..., version: _Optional[str] = ..., evaluation_start_time: _Optional[float] = ..., status: _Optional[_Union[ContractEvaluation.Status, str]] = ...) -> None: ...

class ContractEvaluationBatch(_message.Message):
    __slots__ = ["evals"]
    class Pair(_message.Message):
        __slots__ = ["cev", "user_id"]
        CEV_FIELD_NUMBER: _ClassVar[int]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        cev: ContractEvaluation
        user_id: str
        def __init__(self, user_id: _Optional[str] = ..., cev: _Optional[_Union[ContractEvaluation, _Mapping]] = ...) -> None: ...
    EVALS_FIELD_NUMBER: _ClassVar[int]
    evals: _containers.RepeatedCompositeFieldContainer[ContractEvaluationBatch.Pair]
    def __init__(self, evals: _Optional[_Iterable[_Union[ContractEvaluationBatch.Pair, _Mapping]]] = ...) -> None: ...

class ContractPlayerInfo(_message.Message):
    __slots__ = ["grade", "grade_progress", "grade_score", "issue_score", "issues", "last_evaluation_time", "last_evaluation_version", "season_cxp", "season_progress", "soul_power", "status", "target_grade_score", "target_soul_power", "total_cxp", "unread_evaluations"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class SeasonProgress(_message.Message):
        __slots__ = ["active_DEP", "cxp_last_reward_given", "season_id", "starting_grade", "total_cxp"]
        ACTIVE_DEP_FIELD_NUMBER: _ClassVar[int]
        CXP_LAST_REWARD_GIVEN_FIELD_NUMBER: _ClassVar[int]
        SEASON_ID_FIELD_NUMBER: _ClassVar[int]
        STARTING_GRADE_FIELD_NUMBER: _ClassVar[int]
        TOTAL_CXP_FIELD_NUMBER: _ClassVar[int]
        active_DEP: bool
        cxp_last_reward_given: float
        season_id: str
        starting_grade: Contract.PlayerGrade
        total_cxp: float
        def __init__(self, season_id: _Optional[str] = ..., active_DEP: bool = ..., starting_grade: _Optional[_Union[Contract.PlayerGrade, str]] = ..., total_cxp: _Optional[float] = ..., cxp_last_reward_given: _Optional[float] = ...) -> None: ...
    CALCULATING: ContractPlayerInfo.Status
    COMPLETE: ContractPlayerInfo.Status
    GRADE_FIELD_NUMBER: _ClassVar[int]
    GRADE_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    GRADE_SCORE_FIELD_NUMBER: _ClassVar[int]
    INCOMPLETE: ContractPlayerInfo.Status
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    ISSUE_SCORE_FIELD_NUMBER: _ClassVar[int]
    LAST_EVALUATION_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_EVALUATION_VERSION_FIELD_NUMBER: _ClassVar[int]
    OUT_OF_DATE: ContractPlayerInfo.Status
    SEASON_CXP_FIELD_NUMBER: _ClassVar[int]
    SEASON_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    SOUL_POWER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TARGET_GRADE_SCORE_FIELD_NUMBER: _ClassVar[int]
    TARGET_SOUL_POWER_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CXP_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN: ContractPlayerInfo.Status
    UNREAD_EVALUATIONS_FIELD_NUMBER: _ClassVar[int]
    grade: Contract.PlayerGrade
    grade_progress: float
    grade_score: float
    issue_score: float
    issues: _containers.RepeatedScalarFieldContainer[ContractEvaluation.PoorBehavior]
    last_evaluation_time: float
    last_evaluation_version: str
    season_cxp: float
    season_progress: _containers.RepeatedCompositeFieldContainer[ContractPlayerInfo.SeasonProgress]
    soul_power: float
    status: ContractPlayerInfo.Status
    target_grade_score: float
    target_soul_power: float
    total_cxp: float
    unread_evaluations: _containers.RepeatedCompositeFieldContainer[ContractEvaluation]
    def __init__(self, grade: _Optional[_Union[Contract.PlayerGrade, str]] = ..., total_cxp: _Optional[float] = ..., season_cxp: _Optional[float] = ..., grade_score: _Optional[float] = ..., target_grade_score: _Optional[float] = ..., soul_power: _Optional[float] = ..., target_soul_power: _Optional[float] = ..., grade_progress: _Optional[float] = ..., issues: _Optional[_Iterable[_Union[ContractEvaluation.PoorBehavior, str]]] = ..., issue_score: _Optional[float] = ..., status: _Optional[_Union[ContractPlayerInfo.Status, str]] = ..., last_evaluation_time: _Optional[float] = ..., last_evaluation_version: _Optional[str] = ..., unread_evaluations: _Optional[_Iterable[_Union[ContractEvaluation, _Mapping]]] = ..., season_progress: _Optional[_Iterable[_Union[ContractPlayerInfo.SeasonProgress, _Mapping]]] = ...) -> None: ...

class ContractSeasonGoal(_message.Message):
    __slots__ = ["cxp", "reward_amount", "reward_sub_type", "reward_type"]
    CXP_FIELD_NUMBER: _ClassVar[int]
    REWARD_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    REWARD_SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    REWARD_TYPE_FIELD_NUMBER: _ClassVar[int]
    cxp: float
    reward_amount: float
    reward_sub_type: str
    reward_type: RewardType
    def __init__(self, cxp: _Optional[float] = ..., reward_type: _Optional[_Union[RewardType, str]] = ..., reward_sub_type: _Optional[str] = ..., reward_amount: _Optional[float] = ...) -> None: ...

class ContractSeasonInfo(_message.Message):
    __slots__ = ["grade_goals", "id", "name", "start_time"]
    class GoalSet(_message.Message):
        __slots__ = ["goals", "grade"]
        GOALS_FIELD_NUMBER: _ClassVar[int]
        GRADE_FIELD_NUMBER: _ClassVar[int]
        goals: _containers.RepeatedCompositeFieldContainer[ContractSeasonGoal]
        grade: Contract.PlayerGrade
        def __init__(self, grade: _Optional[_Union[Contract.PlayerGrade, str]] = ..., goals: _Optional[_Iterable[_Union[ContractSeasonGoal, _Mapping]]] = ...) -> None: ...
    GRADE_GOALS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    grade_goals: _containers.RepeatedCompositeFieldContainer[ContractSeasonInfo.GoalSet]
    id: str
    name: str
    start_time: float
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., start_time: _Optional[float] = ..., grade_goals: _Optional[_Iterable[_Union[ContractSeasonInfo.GoalSet, _Mapping]]] = ...) -> None: ...

class ContractSeasonInfos(_message.Message):
    __slots__ = ["infos"]
    INFOS_FIELD_NUMBER: _ClassVar[int]
    infos: _containers.RepeatedCompositeFieldContainer[ContractSeasonInfo]
    def __init__(self, infos: _Optional[_Iterable[_Union[ContractSeasonInfo, _Mapping]]] = ...) -> None: ...

class ContractSeasonRewardConfirmationRequest(_message.Message):
    __slots__ = ["goal", "rinfo", "season_id"]
    GOAL_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    SEASON_ID_FIELD_NUMBER: _ClassVar[int]
    goal: ContractSeasonGoal
    rinfo: BasicRequestInfo
    season_id: str
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., season_id: _Optional[str] = ..., goal: _Optional[_Union[ContractSeasonGoal, _Mapping]] = ...) -> None: ...

class ContractSimConfig(_message.Message):
    __slots__ = ["grade_configs"]
    class ContractGradeSimConfig(_message.Message):
        __slots__ = ["goal_params", "grade"]
        class GoalParams(_message.Message):
            __slots__ = ["cps_mult", "earnings_mult", "elr_mult", "epic_research_budget", "hab_capacity_mult", "target_se", "time_efficacy"]
            CPS_MULT_FIELD_NUMBER: _ClassVar[int]
            EARNINGS_MULT_FIELD_NUMBER: _ClassVar[int]
            ELR_MULT_FIELD_NUMBER: _ClassVar[int]
            EPIC_RESEARCH_BUDGET_FIELD_NUMBER: _ClassVar[int]
            HAB_CAPACITY_MULT_FIELD_NUMBER: _ClassVar[int]
            TARGET_SE_FIELD_NUMBER: _ClassVar[int]
            TIME_EFFICACY_FIELD_NUMBER: _ClassVar[int]
            cps_mult: float
            earnings_mult: float
            elr_mult: float
            epic_research_budget: float
            hab_capacity_mult: float
            target_se: float
            time_efficacy: float
            def __init__(self, target_se: _Optional[float] = ..., cps_mult: _Optional[float] = ..., elr_mult: _Optional[float] = ..., earnings_mult: _Optional[float] = ..., time_efficacy: _Optional[float] = ..., hab_capacity_mult: _Optional[float] = ..., epic_research_budget: _Optional[float] = ...) -> None: ...
        GOAL_PARAMS_FIELD_NUMBER: _ClassVar[int]
        GRADE_FIELD_NUMBER: _ClassVar[int]
        goal_params: _containers.RepeatedCompositeFieldContainer[ContractSimConfig.ContractGradeSimConfig.GoalParams]
        grade: Contract.PlayerGrade
        def __init__(self, grade: _Optional[_Union[Contract.PlayerGrade, str]] = ..., goal_params: _Optional[_Iterable[_Union[ContractSimConfig.ContractGradeSimConfig.GoalParams, _Mapping]]] = ...) -> None: ...
    GRADE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    grade_configs: _containers.RepeatedCompositeFieldContainer[ContractSimConfig.ContractGradeSimConfig]
    def __init__(self, grade_configs: _Optional[_Iterable[_Union[ContractSimConfig.ContractGradeSimConfig, _Mapping]]] = ...) -> None: ...

class ContractSimPoll(_message.Message):
    __slots__ = ["client_version"]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    client_version: int
    def __init__(self, client_version: _Optional[int] = ...) -> None: ...

class ContractSimPollResponse(_message.Message):
    __slots__ = ["contract_to_simulate", "sim_config"]
    CONTRACT_TO_SIMULATE_FIELD_NUMBER: _ClassVar[int]
    SIM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    contract_to_simulate: Contract
    sim_config: ContractSimConfig
    def __init__(self, contract_to_simulate: _Optional[_Union[Contract, _Mapping]] = ..., sim_config: _Optional[_Union[ContractSimConfig, _Mapping]] = ...) -> None: ...

class ContractSimResultUpdate(_message.Message):
    __slots__ = ["contract_id", "goal_infos"]
    class GoalInfo(_message.Message):
        __slots__ = ["goal_index", "grade", "projected_eggs_laid"]
        GOAL_INDEX_FIELD_NUMBER: _ClassVar[int]
        GRADE_FIELD_NUMBER: _ClassVar[int]
        PROJECTED_EGGS_LAID_FIELD_NUMBER: _ClassVar[int]
        goal_index: int
        grade: Contract.PlayerGrade
        projected_eggs_laid: float
        def __init__(self, grade: _Optional[_Union[Contract.PlayerGrade, str]] = ..., goal_index: _Optional[int] = ..., projected_eggs_laid: _Optional[float] = ...) -> None: ...
    CONTRACT_ID_FIELD_NUMBER: _ClassVar[int]
    GOAL_INFOS_FIELD_NUMBER: _ClassVar[int]
    contract_id: str
    goal_infos: _containers.RepeatedCompositeFieldContainer[ContractSimResultUpdate.GoalInfo]
    def __init__(self, contract_id: _Optional[str] = ..., goal_infos: _Optional[_Iterable[_Union[ContractSimResultUpdate.GoalInfo, _Mapping]]] = ...) -> None: ...

class ContractsArchive(_message.Message):
    __slots__ = ["archive"]
    ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    archive: _containers.RepeatedCompositeFieldContainer[LocalContract]
    def __init__(self, archive: _Optional[_Iterable[_Union[LocalContract, _Mapping]]] = ...) -> None: ...

class ContractsRequest(_message.Message):
    __slots__ = ["client_version", "soul_eggs", "user_id"]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    SOUL_EGGS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    client_version: int
    soul_eggs: float
    user_id: str
    def __init__(self, soul_eggs: _Optional[float] = ..., client_version: _Optional[int] = ..., user_id: _Optional[str] = ...) -> None: ...

class ContractsResponse(_message.Message):
    __slots__ = ["contracts", "current_season", "custom_eggs", "max_eop", "server_time", "total_eop", "warning_message"]
    CONTRACTS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SEASON_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_EGGS_FIELD_NUMBER: _ClassVar[int]
    MAX_EOP_FIELD_NUMBER: _ClassVar[int]
    SERVER_TIME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_EOP_FIELD_NUMBER: _ClassVar[int]
    WARNING_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    contracts: _containers.RepeatedCompositeFieldContainer[Contract]
    current_season: ContractSeasonInfo
    custom_eggs: _containers.RepeatedCompositeFieldContainer[CustomEgg]
    max_eop: int
    server_time: float
    total_eop: float
    warning_message: str
    def __init__(self, contracts: _Optional[_Iterable[_Union[Contract, _Mapping]]] = ..., custom_eggs: _Optional[_Iterable[_Union[CustomEgg, _Mapping]]] = ..., warning_message: _Optional[str] = ..., total_eop: _Optional[float] = ..., server_time: _Optional[float] = ..., max_eop: _Optional[int] = ..., current_season: _Optional[_Union[ContractSeasonInfo, _Mapping]] = ...) -> None: ...

class CoopBuffHistory(_message.Message):
    __slots__ = ["history"]
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    history: _containers.RepeatedCompositeFieldContainer[CoopBuffState]
    def __init__(self, history: _Optional[_Iterable[_Union[CoopBuffState, _Mapping]]] = ...) -> None: ...

class CoopBuffState(_message.Message):
    __slots__ = ["earnings", "egg_laying_rate", "server_timestamp"]
    EARNINGS_FIELD_NUMBER: _ClassVar[int]
    EGG_LAYING_RATE_FIELD_NUMBER: _ClassVar[int]
    SERVER_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    earnings: float
    egg_laying_rate: float
    server_timestamp: float
    def __init__(self, egg_laying_rate: _Optional[float] = ..., earnings: _Optional[float] = ..., server_timestamp: _Optional[float] = ...) -> None: ...

class CoopChickenRunEntry(_message.Message):
    __slots__ = ["server_timestamp", "user_id"]
    SERVER_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    server_timestamp: float
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., server_timestamp: _Optional[float] = ...) -> None: ...

class CoopCompletionSnapshot(_message.Message):
    __slots__ = ["contributors"]
    class ContributorSnapshot(_message.Message):
        __slots__ = ["contribution", "finalized", "last_contribution_time", "soul_power", "tokens", "tokens_spent", "total_step_time", "user_id"]
        CONTRIBUTION_FIELD_NUMBER: _ClassVar[int]
        FINALIZED_FIELD_NUMBER: _ClassVar[int]
        LAST_CONTRIBUTION_TIME_FIELD_NUMBER: _ClassVar[int]
        SOUL_POWER_FIELD_NUMBER: _ClassVar[int]
        TOKENS_FIELD_NUMBER: _ClassVar[int]
        TOKENS_SPENT_FIELD_NUMBER: _ClassVar[int]
        TOTAL_STEP_TIME_FIELD_NUMBER: _ClassVar[int]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        contribution: float
        finalized: bool
        last_contribution_time: float
        soul_power: float
        tokens: int
        tokens_spent: int
        total_step_time: float
        user_id: str
        def __init__(self, contribution: _Optional[float] = ..., total_step_time: _Optional[float] = ..., last_contribution_time: _Optional[float] = ..., finalized: bool = ..., soul_power: _Optional[float] = ..., user_id: _Optional[str] = ..., tokens: _Optional[int] = ..., tokens_spent: _Optional[int] = ...) -> None: ...
    CONTRIBUTORS_FIELD_NUMBER: _ClassVar[int]
    contributors: _containers.RepeatedCompositeFieldContainer[CoopCompletionSnapshot.ContributorSnapshot]
    def __init__(self, contributors: _Optional[_Iterable[_Union[CoopCompletionSnapshot.ContributorSnapshot, _Mapping]]] = ...) -> None: ...

class CoopLastChickenRunTimes(_message.Message):
    __slots__ = ["entries"]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[PlayerLastChickenRunTimes]
    def __init__(self, entries: _Optional[_Iterable[_Union[PlayerLastChickenRunTimes, _Mapping]]] = ...) -> None: ...

class CraftArtifactRequest(_message.Message):
    __slots__ = ["crafting_count", "crafting_xp", "ei_user_id", "gold_price_paid", "ingredients", "item_id", "rinfo", "spec"]
    CRAFTING_COUNT_FIELD_NUMBER: _ClassVar[int]
    CRAFTING_XP_FIELD_NUMBER: _ClassVar[int]
    EI_USER_ID_FIELD_NUMBER: _ClassVar[int]
    GOLD_PRICE_PAID_FIELD_NUMBER: _ClassVar[int]
    INGREDIENTS_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    crafting_count: int
    crafting_xp: float
    ei_user_id: str
    gold_price_paid: float
    ingredients: _containers.RepeatedCompositeFieldContainer[ArtifactInventoryItem]
    item_id: int
    rinfo: BasicRequestInfo
    spec: ArtifactSpec
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., ei_user_id: _Optional[str] = ..., spec: _Optional[_Union[ArtifactSpec, _Mapping]] = ..., item_id: _Optional[int] = ..., gold_price_paid: _Optional[float] = ..., crafting_count: _Optional[int] = ..., crafting_xp: _Optional[float] = ..., ingredients: _Optional[_Iterable[_Union[ArtifactInventoryItem, _Mapping]]] = ...) -> None: ...

class CraftArtifactResponse(_message.Message):
    __slots__ = ["ei_user_id", "item_id", "rarity_achieved", "server_id"]
    EI_USER_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    RARITY_ACHIEVED_FIELD_NUMBER: _ClassVar[int]
    SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    ei_user_id: str
    item_id: int
    rarity_achieved: ArtifactSpec.Rarity
    server_id: str
    def __init__(self, item_id: _Optional[int] = ..., ei_user_id: _Optional[str] = ..., rarity_achieved: _Optional[_Union[ArtifactSpec.Rarity, str]] = ..., server_id: _Optional[str] = ...) -> None: ...

class CreateCoopRequest(_message.Message):
    __slots__ = ["allow_all_grades", "cc_only", "client_version", "contract_identifier", "coop_identifier", "eop", "grade", "league", "platform", "points_replay", "public", "rinfo", "seconds_remaining", "soul_power", "user_id", "user_name"]
    ALLOW_ALL_GRADES_FIELD_NUMBER: _ClassVar[int]
    CC_ONLY_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    COOP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    EOP_FIELD_NUMBER: _ClassVar[int]
    GRADE_FIELD_NUMBER: _ClassVar[int]
    LEAGUE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    POINTS_REPLAY_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    SECONDS_REMAINING_FIELD_NUMBER: _ClassVar[int]
    SOUL_POWER_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    allow_all_grades: bool
    cc_only: bool
    client_version: int
    contract_identifier: str
    coop_identifier: str
    eop: float
    grade: Contract.PlayerGrade
    league: int
    platform: Platform
    points_replay: bool
    public: bool
    rinfo: BasicRequestInfo
    seconds_remaining: float
    soul_power: float
    user_id: str
    user_name: str
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., contract_identifier: _Optional[str] = ..., coop_identifier: _Optional[str] = ..., public: bool = ..., cc_only: bool = ..., allow_all_grades: bool = ..., seconds_remaining: _Optional[float] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., soul_power: _Optional[float] = ..., eop: _Optional[float] = ..., league: _Optional[int] = ..., grade: _Optional[_Union[Contract.PlayerGrade, str]] = ..., points_replay: bool = ..., platform: _Optional[_Union[Platform, str]] = ..., client_version: _Optional[int] = ...) -> None: ...

class CreateCoopResponse(_message.Message):
    __slots__ = ["message", "success"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    message: str
    success: bool
    def __init__(self, success: bool = ..., message: _Optional[str] = ...) -> None: ...

class CurrencyFlowBatchRequest(_message.Message):
    __slots__ = ["logs", "rinfo"]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    logs: _containers.RepeatedCompositeFieldContainer[CurrencyFlowLog]
    rinfo: BasicRequestInfo
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., logs: _Optional[_Iterable[_Union[CurrencyFlowLog, _Mapping]]] = ...) -> None: ...

class CurrencyFlowLog(_message.Message):
    __slots__ = ["amount", "approx_time", "currency", "gold_spent", "location", "platform", "soul_eggs", "tickets_spent", "user_id", "version"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    APPROX_TIME_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    GOLD_SPENT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    SOUL_EGGS_FIELD_NUMBER: _ClassVar[int]
    TICKETS_SPENT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    amount: int
    approx_time: float
    currency: RewardType
    gold_spent: int
    location: str
    platform: str
    soul_eggs: float
    tickets_spent: int
    user_id: str
    version: str
    def __init__(self, user_id: _Optional[str] = ..., approx_time: _Optional[float] = ..., currency: _Optional[_Union[RewardType, str]] = ..., amount: _Optional[int] = ..., location: _Optional[str] = ..., version: _Optional[str] = ..., platform: _Optional[str] = ..., soul_eggs: _Optional[float] = ..., tickets_spent: _Optional[int] = ..., gold_spent: _Optional[int] = ...) -> None: ...

class CustomEgg(_message.Message):
    __slots__ = ["buffs", "description", "hatchery_id", "hatchery_max_x", "icon", "icon_height", "icon_width", "identifier", "name", "value"]
    BUFFS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HATCHERY_ID_FIELD_NUMBER: _ClassVar[int]
    HATCHERY_MAX_X_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    ICON_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    ICON_WIDTH_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    buffs: _containers.RepeatedCompositeFieldContainer[GameModifier]
    description: str
    hatchery_id: str
    hatchery_max_x: float
    icon: DLCItem
    icon_height: float
    icon_width: float
    identifier: str
    name: str
    value: float
    def __init__(self, identifier: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., value: _Optional[float] = ..., hatchery_id: _Optional[str] = ..., hatchery_max_x: _Optional[float] = ..., icon: _Optional[_Union[DLCItem, _Mapping]] = ..., icon_width: _Optional[float] = ..., icon_height: _Optional[float] = ..., buffs: _Optional[_Iterable[_Union[GameModifier, _Mapping]]] = ...) -> None: ...

class DLCCatalog(_message.Message):
    __slots__ = ["decorators", "items", "shell_groups", "shell_objects", "shell_sets", "shells", "shells_showcase_last_featured_time"]
    DECORATORS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    SHELLS_FIELD_NUMBER: _ClassVar[int]
    SHELLS_SHOWCASE_LAST_FEATURED_TIME_FIELD_NUMBER: _ClassVar[int]
    SHELL_GROUPS_FIELD_NUMBER: _ClassVar[int]
    SHELL_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    SHELL_SETS_FIELD_NUMBER: _ClassVar[int]
    decorators: _containers.RepeatedCompositeFieldContainer[ShellSetSpec]
    items: _containers.RepeatedCompositeFieldContainer[DLCItem]
    shell_groups: _containers.RepeatedCompositeFieldContainer[ShellGroupSpec]
    shell_objects: _containers.RepeatedCompositeFieldContainer[ShellObjectSpec]
    shell_sets: _containers.RepeatedCompositeFieldContainer[ShellSetSpec]
    shells: _containers.RepeatedCompositeFieldContainer[ShellSpec]
    shells_showcase_last_featured_time: float
    def __init__(self, items: _Optional[_Iterable[_Union[DLCItem, _Mapping]]] = ..., shells: _Optional[_Iterable[_Union[ShellSpec, _Mapping]]] = ..., shell_sets: _Optional[_Iterable[_Union[ShellSetSpec, _Mapping]]] = ..., decorators: _Optional[_Iterable[_Union[ShellSetSpec, _Mapping]]] = ..., shell_objects: _Optional[_Iterable[_Union[ShellObjectSpec, _Mapping]]] = ..., shell_groups: _Optional[_Iterable[_Union[ShellGroupSpec, _Mapping]]] = ..., shells_showcase_last_featured_time: _Optional[float] = ...) -> None: ...

class DLCItem(_message.Message):
    __slots__ = ["checksum", "compressed", "directory", "ext", "name", "original_size", "url"]
    CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    EXT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    checksum: str
    compressed: bool
    directory: str
    ext: str
    name: str
    original_size: int
    url: str
    def __init__(self, name: _Optional[str] = ..., directory: _Optional[str] = ..., ext: _Optional[str] = ..., compressed: bool = ..., original_size: _Optional[int] = ..., url: _Optional[str] = ..., checksum: _Optional[str] = ...) -> None: ...

class DailyGiftInfo(_message.Message):
    __slots__ = ["current_day", "seconds_to_next_day"]
    CURRENT_DAY_FIELD_NUMBER: _ClassVar[int]
    SECONDS_TO_NEXT_DAY_FIELD_NUMBER: _ClassVar[int]
    current_day: int
    seconds_to_next_day: float
    def __init__(self, current_day: _Optional[int] = ..., seconds_to_next_day: _Optional[float] = ...) -> None: ...

class DeviceInfo(_message.Message):
    __slots__ = ["advertising_id", "device_bucket", "device_id", "device_name", "form_factor", "gpu_model", "gpu_vendor", "locale_country", "locale_language", "platform", "platform_version", "screen_height", "screen_width"]
    ADVERTISING_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BUCKET_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    FORM_FACTOR_FIELD_NUMBER: _ClassVar[int]
    GPU_MODEL_FIELD_NUMBER: _ClassVar[int]
    GPU_VENDOR_FIELD_NUMBER: _ClassVar[int]
    LOCALE_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    LOCALE_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_VERSION_FIELD_NUMBER: _ClassVar[int]
    SCREEN_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    SCREEN_WIDTH_FIELD_NUMBER: _ClassVar[int]
    advertising_id: str
    device_bucket: str
    device_id: str
    device_name: str
    form_factor: str
    gpu_model: str
    gpu_vendor: str
    locale_country: str
    locale_language: str
    platform: str
    platform_version: str
    screen_height: int
    screen_width: int
    def __init__(self, device_id: _Optional[str] = ..., advertising_id: _Optional[str] = ..., platform: _Optional[str] = ..., form_factor: _Optional[str] = ..., device_name: _Optional[str] = ..., platform_version: _Optional[str] = ..., locale_country: _Optional[str] = ..., locale_language: _Optional[str] = ..., gpu_vendor: _Optional[str] = ..., gpu_model: _Optional[str] = ..., device_bucket: _Optional[str] = ..., screen_width: _Optional[int] = ..., screen_height: _Optional[int] = ...) -> None: ...

class EggIncAdConfig(_message.Message):
    __slots__ = ["network_priority"]
    NETWORK_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    network_priority: _containers.RepeatedScalarFieldContainer[AdNetwork]
    def __init__(self, network_priority: _Optional[_Iterable[_Union[AdNetwork, str]]] = ...) -> None: ...

class EggIncCurrentEvents(_message.Message):
    __slots__ = ["events"]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[EggIncEvent]
    def __init__(self, events: _Optional[_Iterable[_Union[EggIncEvent, _Mapping]]] = ...) -> None: ...

class EggIncEvent(_message.Message):
    __slots__ = ["cc_only", "duration", "identifier", "multiplier", "seconds_remaining", "start_time", "subtitle", "type"]
    CC_ONLY_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    SECONDS_REMAINING_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    cc_only: bool
    duration: float
    identifier: str
    multiplier: float
    seconds_remaining: float
    start_time: float
    subtitle: str
    type: str
    def __init__(self, identifier: _Optional[str] = ..., seconds_remaining: _Optional[float] = ..., type: _Optional[str] = ..., multiplier: _Optional[float] = ..., subtitle: _Optional[str] = ..., start_time: _Optional[float] = ..., duration: _Optional[float] = ..., cc_only: bool = ...) -> None: ...

class EggIncFirstContactRequest(_message.Message):
    __slots__ = ["client_version", "device_id", "ei_user_id", "game_services_id", "platform", "rinfo", "user_id", "username"]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    EI_USER_ID_FIELD_NUMBER: _ClassVar[int]
    GAME_SERVICES_ID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    client_version: int
    device_id: str
    ei_user_id: str
    game_services_id: str
    platform: Platform
    rinfo: BasicRequestInfo
    user_id: str
    username: str
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., ei_user_id: _Optional[str] = ..., user_id: _Optional[str] = ..., game_services_id: _Optional[str] = ..., device_id: _Optional[str] = ..., username: _Optional[str] = ..., client_version: _Optional[int] = ..., platform: _Optional[_Union[Platform, str]] = ...) -> None: ...

class EggIncFirstContactResponse(_message.Message):
    __slots__ = ["backup", "ei_user_id", "error_code", "error_message", "ids_transferred"]
    class ErrorCodes(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BACKUP_CONFLICT: EggIncFirstContactResponse.ErrorCodes
    BACKUP_FIELD_NUMBER: _ClassVar[int]
    EI_USER_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EXISTING_USER_W_GAMER_ID: EggIncFirstContactResponse.ErrorCodes
    IDS_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    NO_ERROR: EggIncFirstContactResponse.ErrorCodes
    USER_NOT_FOUND: EggIncFirstContactResponse.ErrorCodes
    backup: Backup
    ei_user_id: str
    error_code: int
    error_message: str
    ids_transferred: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ei_user_id: _Optional[str] = ..., ids_transferred: _Optional[_Iterable[str]] = ..., error_code: _Optional[int] = ..., error_message: _Optional[str] = ..., backup: _Optional[_Union[Backup, _Mapping]] = ...) -> None: ...

class FarmProductionParams(_message.Message):
    __slots__ = ["delivered", "elr", "farm_capacity", "farm_population", "ihr", "sr"]
    DELIVERED_FIELD_NUMBER: _ClassVar[int]
    ELR_FIELD_NUMBER: _ClassVar[int]
    FARM_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    FARM_POPULATION_FIELD_NUMBER: _ClassVar[int]
    IHR_FIELD_NUMBER: _ClassVar[int]
    SR_FIELD_NUMBER: _ClassVar[int]
    delivered: float
    elr: float
    farm_capacity: float
    farm_population: float
    ihr: float
    sr: float
    def __init__(self, farm_population: _Optional[float] = ..., farm_capacity: _Optional[float] = ..., elr: _Optional[float] = ..., ihr: _Optional[float] = ..., sr: _Optional[float] = ..., delivered: _Optional[float] = ...) -> None: ...

class GameModifier(_message.Message):
    __slots__ = ["description", "dimension", "value"]
    class GameDimension(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AWAY_EARNINGS: GameModifier.GameDimension
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    EARNINGS: GameModifier.GameDimension
    EGG_LAYING_RATE: GameModifier.GameDimension
    HAB_CAPACITY: GameModifier.GameDimension
    HAB_COST: GameModifier.GameDimension
    INTERNAL_HATCHERY_RATE: GameModifier.GameDimension
    INVALID: GameModifier.GameDimension
    RESEARCH_COST: GameModifier.GameDimension
    SHIPPING_CAPACITY: GameModifier.GameDimension
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_COST: GameModifier.GameDimension
    description: str
    dimension: GameModifier.GameDimension
    value: float
    def __init__(self, dimension: _Optional[_Union[GameModifier.GameDimension, str]] = ..., value: _Optional[float] = ..., description: _Optional[str] = ...) -> None: ...

class GenericAction(_message.Message):
    __slots__ = ["action_name", "advertising_id", "app", "approx_time", "approx_time_DEP", "cc_user", "data", "device", "user_id"]
    ACTION_NAME_FIELD_NUMBER: _ClassVar[int]
    ADVERTISING_ID_FIELD_NUMBER: _ClassVar[int]
    APPROX_TIME_DEP_FIELD_NUMBER: _ClassVar[int]
    APPROX_TIME_FIELD_NUMBER: _ClassVar[int]
    APP_FIELD_NUMBER: _ClassVar[int]
    CC_USER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    action_name: str
    advertising_id: str
    app: AppInfo
    approx_time: float
    approx_time_DEP: float
    cc_user: bool
    data: _containers.RepeatedCompositeFieldContainer[ActionKeyValuePair]
    device: DeviceInfo
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., cc_user: bool = ..., advertising_id: _Optional[str] = ..., approx_time_DEP: _Optional[float] = ..., approx_time: _Optional[float] = ..., action_name: _Optional[str] = ..., data: _Optional[_Iterable[_Union[ActionKeyValuePair, _Mapping]]] = ..., app: _Optional[_Union[AppInfo, _Mapping]] = ..., device: _Optional[_Union[DeviceInfo, _Mapping]] = ...) -> None: ...

class GenericActionBatchRequest(_message.Message):
    __slots__ = ["actions", "rinfo"]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedCompositeFieldContainer[GenericAction]
    rinfo: BasicRequestInfo
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., actions: _Optional[_Iterable[_Union[GenericAction, _Mapping]]] = ...) -> None: ...

class GetActiveMissionsRequest(_message.Message):
    __slots__ = ["reset_index", "rinfo"]
    RESET_INDEX_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    reset_index: int
    rinfo: BasicRequestInfo
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., reset_index: _Optional[int] = ...) -> None: ...

class GetActiveMissionsResponse(_message.Message):
    __slots__ = ["active_missions", "success"]
    ACTIVE_MISSIONS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    active_missions: _containers.RepeatedCompositeFieldContainer[MissionInfo]
    success: bool
    def __init__(self, success: bool = ..., active_missions: _Optional[_Iterable[_Union[MissionInfo, _Mapping]]] = ...) -> None: ...

class GetPeriodicalsRequest(_message.Message):
    __slots__ = ["artifacts_unlocked", "contracts_unlocked", "current_client_version", "debug", "eop", "lost_increments", "mystical_earnings_mult", "piggy_found_full", "piggy_full", "rinfo", "seconds_full_gametime", "seconds_full_realtime", "soul_eggs", "user_id"]
    ARTIFACTS_UNLOCKED_FIELD_NUMBER: _ClassVar[int]
    CONTRACTS_UNLOCKED_FIELD_NUMBER: _ClassVar[int]
    CURRENT_CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    DEBUG_FIELD_NUMBER: _ClassVar[int]
    EOP_FIELD_NUMBER: _ClassVar[int]
    LOST_INCREMENTS_FIELD_NUMBER: _ClassVar[int]
    MYSTICAL_EARNINGS_MULT_FIELD_NUMBER: _ClassVar[int]
    PIGGY_FOUND_FULL_FIELD_NUMBER: _ClassVar[int]
    PIGGY_FULL_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    SECONDS_FULL_GAMETIME_FIELD_NUMBER: _ClassVar[int]
    SECONDS_FULL_REALTIME_FIELD_NUMBER: _ClassVar[int]
    SOUL_EGGS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    artifacts_unlocked: bool
    contracts_unlocked: bool
    current_client_version: int
    debug: bool
    eop: int
    lost_increments: int
    mystical_earnings_mult: float
    piggy_found_full: bool
    piggy_full: bool
    rinfo: BasicRequestInfo
    seconds_full_gametime: float
    seconds_full_realtime: float
    soul_eggs: float
    user_id: str
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., user_id: _Optional[str] = ..., piggy_full: bool = ..., piggy_found_full: bool = ..., seconds_full_realtime: _Optional[float] = ..., seconds_full_gametime: _Optional[float] = ..., lost_increments: _Optional[int] = ..., soul_eggs: _Optional[float] = ..., mystical_earnings_mult: _Optional[float] = ..., eop: _Optional[int] = ..., contracts_unlocked: bool = ..., artifacts_unlocked: bool = ..., current_client_version: _Optional[int] = ..., debug: bool = ...) -> None: ...

class GiftPlayerCoopRequest(_message.Message):
    __slots__ = ["amount", "client_version", "contract_identifier", "coop_identifier", "player_identifier", "requesting_user_id", "requesting_user_name", "rinfo"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    COOP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    PLAYER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    REQUESTING_USER_ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTING_USER_NAME_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    amount: int
    client_version: int
    contract_identifier: str
    coop_identifier: str
    player_identifier: str
    requesting_user_id: str
    requesting_user_name: str
    rinfo: BasicRequestInfo
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., contract_identifier: _Optional[str] = ..., coop_identifier: _Optional[str] = ..., player_identifier: _Optional[str] = ..., requesting_user_id: _Optional[str] = ..., requesting_user_name: _Optional[str] = ..., amount: _Optional[int] = ..., client_version: _Optional[int] = ...) -> None: ...

class IAPSaleEntry(_message.Message):
    __slots__ = ["discount_string", "product_id", "sale_id", "seconds_remaining"]
    DISCOUNT_STRING_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    SALE_ID_FIELD_NUMBER: _ClassVar[int]
    SECONDS_REMAINING_FIELD_NUMBER: _ClassVar[int]
    discount_string: str
    product_id: str
    sale_id: str
    seconds_remaining: float
    def __init__(self, product_id: _Optional[str] = ..., seconds_remaining: _Optional[float] = ..., discount_string: _Optional[str] = ..., sale_id: _Optional[str] = ...) -> None: ...

class IdleSessionSummary(_message.Message):
    __slots__ = ["average_egg_delivery_rate", "average_elr", "average_msr", "eggs_delivered", "farm_index", "last_egg_delivery_rate", "silos_owned", "stats", "success", "time_away", "time_simulated"]
    class Stat(_message.Message):
        __slots__ = ["avg", "max", "min", "name", "total_time"]
        AVG_FIELD_NUMBER: _ClassVar[int]
        MAX_FIELD_NUMBER: _ClassVar[int]
        MIN_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        TOTAL_TIME_FIELD_NUMBER: _ClassVar[int]
        avg: float
        max: float
        min: float
        name: str
        total_time: float
        def __init__(self, name: _Optional[str] = ..., min: _Optional[float] = ..., max: _Optional[float] = ..., avg: _Optional[float] = ..., total_time: _Optional[float] = ...) -> None: ...
    AVERAGE_EGG_DELIVERY_RATE_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_ELR_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_MSR_FIELD_NUMBER: _ClassVar[int]
    EGGS_DELIVERED_FIELD_NUMBER: _ClassVar[int]
    FARM_INDEX_FIELD_NUMBER: _ClassVar[int]
    LAST_EGG_DELIVERY_RATE_FIELD_NUMBER: _ClassVar[int]
    SILOS_OWNED_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    TIME_AWAY_FIELD_NUMBER: _ClassVar[int]
    TIME_SIMULATED_FIELD_NUMBER: _ClassVar[int]
    average_egg_delivery_rate: float
    average_elr: float
    average_msr: float
    eggs_delivered: float
    farm_index: int
    last_egg_delivery_rate: float
    silos_owned: int
    stats: _containers.RepeatedCompositeFieldContainer[IdleSessionSummary.Stat]
    success: bool
    time_away: float
    time_simulated: float
    def __init__(self, success: bool = ..., time_away: _Optional[float] = ..., time_simulated: _Optional[float] = ..., silos_owned: _Optional[int] = ..., average_elr: _Optional[float] = ..., average_msr: _Optional[float] = ..., average_egg_delivery_rate: _Optional[float] = ..., last_egg_delivery_rate: _Optional[float] = ..., eggs_delivered: _Optional[float] = ..., stats: _Optional[_Iterable[_Union[IdleSessionSummary.Stat, _Mapping]]] = ..., farm_index: _Optional[int] = ...) -> None: ...

class InGameMail(_message.Message):
    __slots__ = ["action", "app_link", "app_link_extra", "builds", "category", "date", "days_until_retry", "gold_tip", "id", "image", "image_height", "image_width", "max_client_version", "max_retries", "max_soul_eggs", "message", "min_client_version", "min_days_since_last_tip", "min_mystical_bonus", "min_piggy_breaks", "min_soul_eggs", "platform", "priority", "tip", "title", "url", "user_type"]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    APP_LINK_EXTRA_FIELD_NUMBER: _ClassVar[int]
    APP_LINK_FIELD_NUMBER: _ClassVar[int]
    BUILDS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    DAYS_UNTIL_RETRY_FIELD_NUMBER: _ClassVar[int]
    GOLD_TIP_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_WIDTH_FIELD_NUMBER: _ClassVar[int]
    MAX_CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    MAX_RETRIES_FIELD_NUMBER: _ClassVar[int]
    MAX_SOUL_EGGS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MIN_CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    MIN_DAYS_SINCE_LAST_TIP_FIELD_NUMBER: _ClassVar[int]
    MIN_MYSTICAL_BONUS_FIELD_NUMBER: _ClassVar[int]
    MIN_PIGGY_BREAKS_FIELD_NUMBER: _ClassVar[int]
    MIN_SOUL_EGGS_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    TIP_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    USER_TYPE_FIELD_NUMBER: _ClassVar[int]
    action: str
    app_link: UILocation
    app_link_extra: str
    builds: _containers.RepeatedScalarFieldContainer[str]
    category: str
    date: str
    days_until_retry: float
    gold_tip: float
    id: str
    image: DLCItem
    image_height: float
    image_width: float
    max_client_version: int
    max_retries: int
    max_soul_eggs: float
    message: str
    min_client_version: int
    min_days_since_last_tip: float
    min_mystical_bonus: float
    min_piggy_breaks: int
    min_soul_eggs: float
    platform: int
    priority: int
    tip: bool
    title: str
    url: str
    user_type: UserType
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., date: _Optional[str] = ..., message: _Optional[str] = ..., action: _Optional[str] = ..., url: _Optional[str] = ..., app_link: _Optional[_Union[UILocation, str]] = ..., app_link_extra: _Optional[str] = ..., image: _Optional[_Union[DLCItem, _Mapping]] = ..., image_width: _Optional[float] = ..., image_height: _Optional[float] = ..., platform: _Optional[int] = ..., builds: _Optional[_Iterable[str]] = ..., min_client_version: _Optional[int] = ..., max_client_version: _Optional[int] = ..., min_soul_eggs: _Optional[float] = ..., max_soul_eggs: _Optional[float] = ..., min_mystical_bonus: _Optional[float] = ..., user_type: _Optional[_Union[UserType, str]] = ..., min_piggy_breaks: _Optional[int] = ..., gold_tip: _Optional[float] = ..., tip: bool = ..., priority: _Optional[int] = ..., min_days_since_last_tip: _Optional[float] = ..., max_retries: _Optional[int] = ..., days_until_retry: _Optional[float] = ..., category: _Optional[str] = ...) -> None: ...

class InventorySlot(_message.Message):
    __slots__ = ["item_id", "occupied"]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    OCCUPIED_FIELD_NUMBER: _ClassVar[int]
    item_id: int
    occupied: bool
    def __init__(self, occupied: bool = ..., item_id: _Optional[int] = ...) -> None: ...

class JoinCoopRequest(_message.Message):
    __slots__ = ["client_version", "contract_identifier", "coop_identifier", "eop", "grade", "league", "platform", "points_replay", "rinfo", "seconds_remaining", "soul_power", "user_id", "user_name"]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    COOP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    EOP_FIELD_NUMBER: _ClassVar[int]
    GRADE_FIELD_NUMBER: _ClassVar[int]
    LEAGUE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    POINTS_REPLAY_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    SECONDS_REMAINING_FIELD_NUMBER: _ClassVar[int]
    SOUL_POWER_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    client_version: int
    contract_identifier: str
    coop_identifier: str
    eop: float
    grade: Contract.PlayerGrade
    league: int
    platform: Platform
    points_replay: bool
    rinfo: BasicRequestInfo
    seconds_remaining: float
    soul_power: float
    user_id: str
    user_name: str
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., contract_identifier: _Optional[str] = ..., coop_identifier: _Optional[str] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., soul_power: _Optional[float] = ..., eop: _Optional[float] = ..., league: _Optional[int] = ..., grade: _Optional[_Union[Contract.PlayerGrade, str]] = ..., points_replay: bool = ..., platform: _Optional[_Union[Platform, str]] = ..., seconds_remaining: _Optional[float] = ..., client_version: _Optional[int] = ...) -> None: ...

class JoinCoopResponse(_message.Message):
    __slots__ = ["banned", "can_start", "coop_identifier", "grade", "match_percent", "message", "num_members", "seconds_remaining", "status", "success"]
    BANNED_FIELD_NUMBER: _ClassVar[int]
    CAN_START_FIELD_NUMBER: _ClassVar[int]
    COOP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    GRADE_FIELD_NUMBER: _ClassVar[int]
    MATCH_PERCENT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    NUM_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    SECONDS_REMAINING_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    banned: bool
    can_start: bool
    coop_identifier: str
    grade: Contract.PlayerGrade
    match_percent: float
    message: str
    num_members: int
    seconds_remaining: float
    status: ContractCoopStatusResponse.Status
    success: bool
    def __init__(self, success: bool = ..., message: _Optional[str] = ..., banned: bool = ..., coop_identifier: _Optional[str] = ..., seconds_remaining: _Optional[float] = ..., match_percent: _Optional[float] = ..., num_members: _Optional[int] = ..., status: _Optional[_Union[ContractCoopStatusResponse.Status, str]] = ..., grade: _Optional[_Union[Contract.PlayerGrade, str]] = ..., can_start: bool = ...) -> None: ...

class KickPlayerCoopRequest(_message.Message):
    __slots__ = ["client_version", "contract_identifier", "coop_identifier", "player_identifier", "reason", "requesting_user_id", "rinfo"]
    class Reason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CHEATER: KickPlayerCoopRequest.Reason
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    COOP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    IDLE: KickPlayerCoopRequest.Reason
    INVALID: KickPlayerCoopRequest.Reason
    LEECH: KickPlayerCoopRequest.Reason
    PLAYER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    PRIVATE: KickPlayerCoopRequest.Reason
    REASON_FIELD_NUMBER: _ClassVar[int]
    REQUESTING_USER_ID_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    client_version: int
    contract_identifier: str
    coop_identifier: str
    player_identifier: str
    reason: KickPlayerCoopRequest.Reason
    requesting_user_id: str
    rinfo: BasicRequestInfo
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., contract_identifier: _Optional[str] = ..., coop_identifier: _Optional[str] = ..., player_identifier: _Optional[str] = ..., requesting_user_id: _Optional[str] = ..., reason: _Optional[_Union[KickPlayerCoopRequest.Reason, str]] = ..., client_version: _Optional[int] = ...) -> None: ...

class LeaderboardAnalysis(_message.Message):
    __slots__ = ["chunks", "count", "cursor", "high_score", "low_score"]
    class Chunk(_message.Message):
        __slots__ = ["end_cursor", "end_index", "high_score", "low_score", "start_cursor", "start_index"]
        END_CURSOR_FIELD_NUMBER: _ClassVar[int]
        END_INDEX_FIELD_NUMBER: _ClassVar[int]
        HIGH_SCORE_FIELD_NUMBER: _ClassVar[int]
        LOW_SCORE_FIELD_NUMBER: _ClassVar[int]
        START_CURSOR_FIELD_NUMBER: _ClassVar[int]
        START_INDEX_FIELD_NUMBER: _ClassVar[int]
        end_cursor: str
        end_index: int
        high_score: float
        low_score: float
        start_cursor: str
        start_index: int
        def __init__(self, start_index: _Optional[int] = ..., end_index: _Optional[int] = ..., high_score: _Optional[float] = ..., low_score: _Optional[float] = ..., start_cursor: _Optional[str] = ..., end_cursor: _Optional[str] = ...) -> None: ...
    CHUNKS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    HIGH_SCORE_FIELD_NUMBER: _ClassVar[int]
    LOW_SCORE_FIELD_NUMBER: _ClassVar[int]
    chunks: _containers.RepeatedCompositeFieldContainer[LeaderboardAnalysis.Chunk]
    count: int
    cursor: str
    high_score: float
    low_score: float
    def __init__(self, chunks: _Optional[_Iterable[_Union[LeaderboardAnalysis.Chunk, _Mapping]]] = ..., count: _Optional[int] = ..., high_score: _Optional[float] = ..., low_score: _Optional[float] = ..., cursor: _Optional[str] = ...) -> None: ...

class LeaderboardInfo(_message.Message):
    __slots__ = ["all_time_scope", "seasons"]
    class Season(_message.Message):
        __slots__ = ["name", "scope"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        SCOPE_FIELD_NUMBER: _ClassVar[int]
        name: str
        scope: str
        def __init__(self, scope: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
    ALL_TIME_SCOPE_FIELD_NUMBER: _ClassVar[int]
    SEASONS_FIELD_NUMBER: _ClassVar[int]
    all_time_scope: str
    seasons: _containers.RepeatedCompositeFieldContainer[LeaderboardInfo.Season]
    def __init__(self, seasons: _Optional[_Iterable[_Union[LeaderboardInfo.Season, _Mapping]]] = ..., all_time_scope: _Optional[str] = ...) -> None: ...

class LeaderboardRequest(_message.Message):
    __slots__ = ["grade", "rinfo", "scope"]
    GRADE_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    grade: Contract.PlayerGrade
    rinfo: BasicRequestInfo
    scope: str
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., scope: _Optional[str] = ..., grade: _Optional[_Union[Contract.PlayerGrade, str]] = ...) -> None: ...

class LeaderboardResponse(_message.Message):
    __slots__ = ["count", "grade", "rank", "scope", "score", "top_entries"]
    class Entry(_message.Message):
        __slots__ = ["alias", "rank", "score"]
        ALIAS_FIELD_NUMBER: _ClassVar[int]
        RANK_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        alias: str
        rank: int
        score: float
        def __init__(self, rank: _Optional[int] = ..., alias: _Optional[str] = ..., score: _Optional[float] = ...) -> None: ...
    COUNT_FIELD_NUMBER: _ClassVar[int]
    GRADE_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    TOP_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    count: int
    grade: Contract.PlayerGrade
    rank: int
    scope: str
    score: float
    top_entries: _containers.RepeatedCompositeFieldContainer[LeaderboardResponse.Entry]
    def __init__(self, scope: _Optional[str] = ..., grade: _Optional[_Union[Contract.PlayerGrade, str]] = ..., top_entries: _Optional[_Iterable[_Union[LeaderboardResponse.Entry, _Mapping]]] = ..., count: _Optional[int] = ..., rank: _Optional[int] = ..., score: _Optional[float] = ...) -> None: ...

class LeaveCoopRequest(_message.Message):
    __slots__ = ["client_version", "contract_identifier", "coop_identifier", "player_identifier", "rinfo"]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    COOP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    PLAYER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    client_version: int
    contract_identifier: str
    coop_identifier: str
    player_identifier: str
    rinfo: BasicRequestInfo
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., contract_identifier: _Optional[str] = ..., coop_identifier: _Optional[str] = ..., player_identifier: _Optional[str] = ..., client_version: _Optional[int] = ...) -> None: ...

class LiveConfig(_message.Message):
    __slots__ = ["boosts_config", "config_id", "gift_config", "help_config", "misc_config"]
    class BoostsConfig(_message.Message):
        __slots__ = ["cash_boost_cooloff_time", "item_configs"]
        class ItemConfig(_message.Message):
            __slots__ = ["boost_id", "price", "se_required", "token_price"]
            BOOST_ID_FIELD_NUMBER: _ClassVar[int]
            PRICE_FIELD_NUMBER: _ClassVar[int]
            SE_REQUIRED_FIELD_NUMBER: _ClassVar[int]
            TOKEN_PRICE_FIELD_NUMBER: _ClassVar[int]
            boost_id: str
            price: int
            se_required: float
            token_price: int
            def __init__(self, boost_id: _Optional[str] = ..., price: _Optional[int] = ..., token_price: _Optional[int] = ..., se_required: _Optional[float] = ...) -> None: ...
        CASH_BOOST_COOLOFF_TIME_FIELD_NUMBER: _ClassVar[int]
        ITEM_CONFIGS_FIELD_NUMBER: _ClassVar[int]
        cash_boost_cooloff_time: float
        item_configs: _containers.RepeatedCompositeFieldContainer[LiveConfig.BoostsConfig.ItemConfig]
        def __init__(self, item_configs: _Optional[_Iterable[_Union[LiveConfig.BoostsConfig.ItemConfig, _Mapping]]] = ..., cash_boost_cooloff_time: _Optional[float] = ...) -> None: ...
    class GiftConfig(_message.Message):
        __slots__ = ["gift_configs", "gift_mu_max_spent", "gift_mu_min_spent", "gift_mu_overall_mult", "package_interval", "package_interval_contract", "package_interval_piggy_extra_full", "package_interval_piggy_full", "package_reset_on_idle", "random_gift_mu_config", "video_gift_mu_config", "video_offer_interval", "video_offer_interval_contract", "video_offer_interval_piggy_extra_full", "video_offer_interval_piggy_full", "video_reset_on_idle"]
        class GiftMuConfig(_message.Message):
            __slots__ = ["max_spent", "min_spent", "overall_mult"]
            MAX_SPENT_FIELD_NUMBER: _ClassVar[int]
            MIN_SPENT_FIELD_NUMBER: _ClassVar[int]
            OVERALL_MULT_FIELD_NUMBER: _ClassVar[int]
            max_spent: float
            min_spent: float
            overall_mult: float
            def __init__(self, min_spent: _Optional[float] = ..., max_spent: _Optional[float] = ..., overall_mult: _Optional[float] = ...) -> None: ...
        class GiftValueConfig(_message.Message):
            __slots__ = ["amount", "gift_id", "rand_max", "rand_min", "video_max", "video_min"]
            AMOUNT_FIELD_NUMBER: _ClassVar[int]
            GIFT_ID_FIELD_NUMBER: _ClassVar[int]
            RAND_MAX_FIELD_NUMBER: _ClassVar[int]
            RAND_MIN_FIELD_NUMBER: _ClassVar[int]
            VIDEO_MAX_FIELD_NUMBER: _ClassVar[int]
            VIDEO_MIN_FIELD_NUMBER: _ClassVar[int]
            amount: float
            gift_id: str
            rand_max: float
            rand_min: float
            video_max: float
            video_min: float
            def __init__(self, gift_id: _Optional[str] = ..., amount: _Optional[float] = ..., rand_min: _Optional[float] = ..., rand_max: _Optional[float] = ..., video_min: _Optional[float] = ..., video_max: _Optional[float] = ...) -> None: ...
        GIFT_CONFIGS_FIELD_NUMBER: _ClassVar[int]
        GIFT_MU_MAX_SPENT_FIELD_NUMBER: _ClassVar[int]
        GIFT_MU_MIN_SPENT_FIELD_NUMBER: _ClassVar[int]
        GIFT_MU_OVERALL_MULT_FIELD_NUMBER: _ClassVar[int]
        PACKAGE_INTERVAL_CONTRACT_FIELD_NUMBER: _ClassVar[int]
        PACKAGE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
        PACKAGE_INTERVAL_PIGGY_EXTRA_FULL_FIELD_NUMBER: _ClassVar[int]
        PACKAGE_INTERVAL_PIGGY_FULL_FIELD_NUMBER: _ClassVar[int]
        PACKAGE_RESET_ON_IDLE_FIELD_NUMBER: _ClassVar[int]
        RANDOM_GIFT_MU_CONFIG_FIELD_NUMBER: _ClassVar[int]
        VIDEO_GIFT_MU_CONFIG_FIELD_NUMBER: _ClassVar[int]
        VIDEO_OFFER_INTERVAL_CONTRACT_FIELD_NUMBER: _ClassVar[int]
        VIDEO_OFFER_INTERVAL_FIELD_NUMBER: _ClassVar[int]
        VIDEO_OFFER_INTERVAL_PIGGY_EXTRA_FULL_FIELD_NUMBER: _ClassVar[int]
        VIDEO_OFFER_INTERVAL_PIGGY_FULL_FIELD_NUMBER: _ClassVar[int]
        VIDEO_RESET_ON_IDLE_FIELD_NUMBER: _ClassVar[int]
        gift_configs: _containers.RepeatedCompositeFieldContainer[LiveConfig.GiftConfig.GiftValueConfig]
        gift_mu_max_spent: float
        gift_mu_min_spent: float
        gift_mu_overall_mult: float
        package_interval: float
        package_interval_contract: float
        package_interval_piggy_extra_full: float
        package_interval_piggy_full: float
        package_reset_on_idle: bool
        random_gift_mu_config: LiveConfig.GiftConfig.GiftMuConfig
        video_gift_mu_config: LiveConfig.GiftConfig.GiftMuConfig
        video_offer_interval: float
        video_offer_interval_contract: float
        video_offer_interval_piggy_extra_full: float
        video_offer_interval_piggy_full: float
        video_reset_on_idle: bool
        def __init__(self, gift_configs: _Optional[_Iterable[_Union[LiveConfig.GiftConfig.GiftValueConfig, _Mapping]]] = ..., gift_mu_min_spent: _Optional[float] = ..., gift_mu_max_spent: _Optional[float] = ..., gift_mu_overall_mult: _Optional[float] = ..., random_gift_mu_config: _Optional[_Union[LiveConfig.GiftConfig.GiftMuConfig, _Mapping]] = ..., video_gift_mu_config: _Optional[_Union[LiveConfig.GiftConfig.GiftMuConfig, _Mapping]] = ..., package_interval: _Optional[float] = ..., video_offer_interval: _Optional[float] = ..., video_offer_interval_contract: _Optional[float] = ..., video_offer_interval_piggy_full: _Optional[float] = ..., video_offer_interval_piggy_extra_full: _Optional[float] = ..., video_reset_on_idle: bool = ..., package_interval_contract: _Optional[float] = ..., package_interval_piggy_full: _Optional[float] = ..., package_interval_piggy_extra_full: _Optional[float] = ..., package_reset_on_idle: bool = ...) -> None: ...
    class HelpConfig(_message.Message):
        __slots__ = ["video_infos"]
        class HowToVideoInfo(_message.Message):
            __slots__ = ["description", "duration", "name", "soul_eggs", "type", "url"]
            class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = []
            ARTICLE: LiveConfig.HelpConfig.HowToVideoInfo.Type
            DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
            DURATION_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            SOUL_EGGS_FIELD_NUMBER: _ClassVar[int]
            TYPE_FIELD_NUMBER: _ClassVar[int]
            URL_FIELD_NUMBER: _ClassVar[int]
            VIDEO: LiveConfig.HelpConfig.HowToVideoInfo.Type
            description: str
            duration: str
            name: str
            soul_eggs: float
            type: LiveConfig.HelpConfig.HowToVideoInfo.Type
            url: str
            def __init__(self, type: _Optional[_Union[LiveConfig.HelpConfig.HowToVideoInfo.Type, str]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., duration: _Optional[str] = ..., url: _Optional[str] = ..., soul_eggs: _Optional[float] = ...) -> None: ...
        VIDEO_INFOS_FIELD_NUMBER: _ClassVar[int]
        video_infos: _containers.RepeatedCompositeFieldContainer[LiveConfig.HelpConfig.HowToVideoInfo]
        def __init__(self, video_infos: _Optional[_Iterable[_Union[LiveConfig.HelpConfig.HowToVideoInfo, _Mapping]]] = ...) -> None: ...
    class MiscConfig(_message.Message):
        __slots__ = ["ask_to_track", "ask_to_track_after_privacy", "ask_to_track_message", "ask_to_track_min_soul_eggs", "ask_to_track_show_pre_dialog", "chicken_run_boost_percentage", "contracts_beta", "contracts_club_available", "contracts_expert_league_min_soul_power", "new_player_event_duration", "season_rewards_enabled", "shells_intro_alert_threshold", "shells_intro_tickets", "shells_lighting_controls_price", "shells_max_free_chicken_configs"]
        ASK_TO_TRACK_AFTER_PRIVACY_FIELD_NUMBER: _ClassVar[int]
        ASK_TO_TRACK_FIELD_NUMBER: _ClassVar[int]
        ASK_TO_TRACK_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        ASK_TO_TRACK_MIN_SOUL_EGGS_FIELD_NUMBER: _ClassVar[int]
        ASK_TO_TRACK_SHOW_PRE_DIALOG_FIELD_NUMBER: _ClassVar[int]
        CHICKEN_RUN_BOOST_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        CONTRACTS_BETA_FIELD_NUMBER: _ClassVar[int]
        CONTRACTS_CLUB_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
        CONTRACTS_EXPERT_LEAGUE_MIN_SOUL_POWER_FIELD_NUMBER: _ClassVar[int]
        NEW_PLAYER_EVENT_DURATION_FIELD_NUMBER: _ClassVar[int]
        SEASON_REWARDS_ENABLED_FIELD_NUMBER: _ClassVar[int]
        SHELLS_INTRO_ALERT_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        SHELLS_INTRO_TICKETS_FIELD_NUMBER: _ClassVar[int]
        SHELLS_LIGHTING_CONTROLS_PRICE_FIELD_NUMBER: _ClassVar[int]
        SHELLS_MAX_FREE_CHICKEN_CONFIGS_FIELD_NUMBER: _ClassVar[int]
        ask_to_track: bool
        ask_to_track_after_privacy: bool
        ask_to_track_message: str
        ask_to_track_min_soul_eggs: float
        ask_to_track_show_pre_dialog: bool
        chicken_run_boost_percentage: float
        contracts_beta: bool
        contracts_club_available: bool
        contracts_expert_league_min_soul_power: float
        new_player_event_duration: float
        season_rewards_enabled: bool
        shells_intro_alert_threshold: int
        shells_intro_tickets: int
        shells_lighting_controls_price: int
        shells_max_free_chicken_configs: int
        def __init__(self, ask_to_track: bool = ..., ask_to_track_min_soul_eggs: _Optional[float] = ..., ask_to_track_message: _Optional[str] = ..., ask_to_track_show_pre_dialog: bool = ..., ask_to_track_after_privacy: bool = ..., chicken_run_boost_percentage: _Optional[float] = ..., shells_intro_tickets: _Optional[int] = ..., shells_max_free_chicken_configs: _Optional[int] = ..., shells_intro_alert_threshold: _Optional[int] = ..., shells_lighting_controls_price: _Optional[int] = ..., contracts_expert_league_min_soul_power: _Optional[float] = ..., new_player_event_duration: _Optional[float] = ..., contracts_club_available: bool = ..., contracts_beta: bool = ..., season_rewards_enabled: bool = ...) -> None: ...
    BOOSTS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    GIFT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    HELP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MISC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    boosts_config: LiveConfig.BoostsConfig
    config_id: str
    gift_config: LiveConfig.GiftConfig
    help_config: LiveConfig.HelpConfig
    misc_config: LiveConfig.MiscConfig
    def __init__(self, config_id: _Optional[str] = ..., boosts_config: _Optional[_Union[LiveConfig.BoostsConfig, _Mapping]] = ..., gift_config: _Optional[_Union[LiveConfig.GiftConfig, _Mapping]] = ..., misc_config: _Optional[_Union[LiveConfig.MiscConfig, _Mapping]] = ..., help_config: _Optional[_Union[LiveConfig.HelpConfig, _Mapping]] = ...) -> None: ...

class LocalContract(_message.Message):
    __slots__ = ["accepted", "boosts_used", "cancelled", "contract", "coop_contribution_finalized", "coop_grace_period_end_time", "coop_identifier", "coop_last_uploaded_contribution", "coop_share_farm", "coop_shared_end_time", "coop_simulation_end_time", "coop_user_id", "evaluation", "grade", "last_amount_when_reward_given", "last_nag_time", "league", "max_farm_size_reached", "new", "num_goals_achieved", "points_replay", "reported_uuids", "time_accepted"]
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    BOOSTS_USED_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    COOP_CONTRIBUTION_FINALIZED_FIELD_NUMBER: _ClassVar[int]
    COOP_GRACE_PERIOD_END_TIME_FIELD_NUMBER: _ClassVar[int]
    COOP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    COOP_LAST_UPLOADED_CONTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    COOP_SHARED_END_TIME_FIELD_NUMBER: _ClassVar[int]
    COOP_SHARE_FARM_FIELD_NUMBER: _ClassVar[int]
    COOP_SIMULATION_END_TIME_FIELD_NUMBER: _ClassVar[int]
    COOP_USER_ID_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_FIELD_NUMBER: _ClassVar[int]
    GRADE_FIELD_NUMBER: _ClassVar[int]
    LAST_AMOUNT_WHEN_REWARD_GIVEN_FIELD_NUMBER: _ClassVar[int]
    LAST_NAG_TIME_FIELD_NUMBER: _ClassVar[int]
    LEAGUE_FIELD_NUMBER: _ClassVar[int]
    MAX_FARM_SIZE_REACHED_FIELD_NUMBER: _ClassVar[int]
    NEW_FIELD_NUMBER: _ClassVar[int]
    NUM_GOALS_ACHIEVED_FIELD_NUMBER: _ClassVar[int]
    POINTS_REPLAY_FIELD_NUMBER: _ClassVar[int]
    REPORTED_UUIDS_FIELD_NUMBER: _ClassVar[int]
    TIME_ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    accepted: bool
    boosts_used: int
    cancelled: bool
    contract: Contract
    coop_contribution_finalized: bool
    coop_grace_period_end_time: float
    coop_identifier: str
    coop_last_uploaded_contribution: float
    coop_share_farm: bool
    coop_shared_end_time: float
    coop_simulation_end_time: float
    coop_user_id: str
    evaluation: ContractEvaluation
    grade: Contract.PlayerGrade
    last_amount_when_reward_given: float
    last_nag_time: float
    league: int
    max_farm_size_reached: float
    new: bool
    num_goals_achieved: int
    points_replay: bool
    reported_uuids: _containers.RepeatedScalarFieldContainer[str]
    time_accepted: float
    def __init__(self, contract: _Optional[_Union[Contract, _Mapping]] = ..., coop_identifier: _Optional[str] = ..., accepted: bool = ..., time_accepted: _Optional[float] = ..., cancelled: bool = ..., new: bool = ..., coop_shared_end_time: _Optional[float] = ..., coop_simulation_end_time: _Optional[float] = ..., coop_grace_period_end_time: _Optional[float] = ..., coop_contribution_finalized: bool = ..., coop_last_uploaded_contribution: _Optional[float] = ..., coop_user_id: _Optional[str] = ..., coop_share_farm: bool = ..., last_amount_when_reward_given: _Optional[float] = ..., num_goals_achieved: _Optional[int] = ..., max_farm_size_reached: _Optional[float] = ..., boosts_used: _Optional[int] = ..., points_replay: bool = ..., league: _Optional[int] = ..., grade: _Optional[_Union[Contract.PlayerGrade, str]] = ..., last_nag_time: _Optional[float] = ..., evaluation: _Optional[_Union[ContractEvaluation, _Mapping]] = ..., reported_uuids: _Optional[_Iterable[str]] = ...) -> None: ...

class LogCompleteMissionPayload(_message.Message):
    __slots__ = ["req", "res"]
    REQ_FIELD_NUMBER: _ClassVar[int]
    RES_FIELD_NUMBER: _ClassVar[int]
    req: MissionRequest
    res: CompleteMissionResponse
    def __init__(self, req: _Optional[_Union[MissionRequest, _Mapping]] = ..., res: _Optional[_Union[CompleteMissionResponse, _Mapping]] = ...) -> None: ...

class LogConsumeArtifactPayload(_message.Message):
    __slots__ = ["req", "res"]
    REQ_FIELD_NUMBER: _ClassVar[int]
    RES_FIELD_NUMBER: _ClassVar[int]
    req: ConsumeArtifactRequest
    res: ConsumeArtifactResponse
    def __init__(self, req: _Optional[_Union[ConsumeArtifactRequest, _Mapping]] = ..., res: _Optional[_Union[ConsumeArtifactResponse, _Mapping]] = ...) -> None: ...

class LogCraftArtifactPayload(_message.Message):
    __slots__ = ["req", "res"]
    REQ_FIELD_NUMBER: _ClassVar[int]
    RES_FIELD_NUMBER: _ClassVar[int]
    req: CraftArtifactRequest
    res: CraftArtifactResponse
    def __init__(self, req: _Optional[_Union[CraftArtifactRequest, _Mapping]] = ..., res: _Optional[_Union[CraftArtifactResponse, _Mapping]] = ...) -> None: ...

class LogSetArtifactPayload(_message.Message):
    __slots__ = ["req", "res"]
    REQ_FIELD_NUMBER: _ClassVar[int]
    RES_FIELD_NUMBER: _ClassVar[int]
    req: SetArtifactRequest
    res: SetArtifactResponse
    def __init__(self, req: _Optional[_Union[SetArtifactRequest, _Mapping]] = ..., res: _Optional[_Union[SetArtifactResponse, _Mapping]] = ...) -> None: ...

class MailDB(_message.Message):
    __slots__ = ["mail", "tips_checksum", "tips_db_data"]
    MAIL_FIELD_NUMBER: _ClassVar[int]
    TIPS_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    TIPS_DB_DATA_FIELD_NUMBER: _ClassVar[int]
    mail: _containers.RepeatedCompositeFieldContainer[InGameMail]
    tips_checksum: str
    tips_db_data: bytes
    def __init__(self, mail: _Optional[_Iterable[_Union[InGameMail, _Mapping]]] = ..., tips_db_data: _Optional[bytes] = ..., tips_checksum: _Optional[str] = ...) -> None: ...

class MailState(_message.Message):
    __slots__ = ["read_mail_ids", "tips_checksum", "tips_states"]
    class TipState(_message.Message):
        __slots__ = ["id", "reads", "time_read"]
        ID_FIELD_NUMBER: _ClassVar[int]
        READS_FIELD_NUMBER: _ClassVar[int]
        TIME_READ_FIELD_NUMBER: _ClassVar[int]
        id: str
        reads: int
        time_read: float
        def __init__(self, id: _Optional[str] = ..., reads: _Optional[int] = ..., time_read: _Optional[float] = ...) -> None: ...
    READ_MAIL_IDS_FIELD_NUMBER: _ClassVar[int]
    TIPS_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    TIPS_STATES_FIELD_NUMBER: _ClassVar[int]
    read_mail_ids: _containers.RepeatedScalarFieldContainer[str]
    tips_checksum: str
    tips_states: _containers.RepeatedCompositeFieldContainer[MailState.TipState]
    def __init__(self, read_mail_ids: _Optional[_Iterable[str]] = ..., tips_states: _Optional[_Iterable[_Union[MailState.TipState, _Mapping]]] = ..., tips_checksum: _Optional[str] = ...) -> None: ...

class MissionInfo(_message.Message):
    __slots__ = ["capacity", "duration_seconds", "duration_type", "fuel", "identifier", "level", "mission_log", "quality_bump", "reset_index", "seconds_remaining", "ship", "start_time_derived", "status", "target_artifact", "type"]
    class DurationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class MissionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Spaceship(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Fuel(_message.Message):
        __slots__ = ["amount", "egg"]
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        EGG_FIELD_NUMBER: _ClassVar[int]
        amount: float
        egg: Egg
        def __init__(self, egg: _Optional[_Union[Egg, str]] = ..., amount: _Optional[float] = ...) -> None: ...
    ABORTED: MissionInfo.Status
    ANALYZING: MissionInfo.Status
    ARCHIVED: MissionInfo.Status
    ATREGGIES: MissionInfo.Spaceship
    BCR: MissionInfo.Spaceship
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    CHICKEN_HEAVY: MissionInfo.Spaceship
    CHICKEN_NINE: MissionInfo.Spaceship
    CHICKEN_ONE: MissionInfo.Spaceship
    CHICKFIANT: MissionInfo.Spaceship
    COMPLETE: MissionInfo.Status
    CORELLIHEN_CORVETTE: MissionInfo.Spaceship
    DURATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
    DURATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    EPIC: MissionInfo.DurationType
    EXPLORING: MissionInfo.Status
    FUELING: MissionInfo.Status
    FUEL_FIELD_NUMBER: _ClassVar[int]
    GALEGGTICA: MissionInfo.Spaceship
    HENERPRISE: MissionInfo.Spaceship
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    LONG: MissionInfo.DurationType
    MILLENIUM_CHICKEN: MissionInfo.Spaceship
    MISSION_LOG_FIELD_NUMBER: _ClassVar[int]
    PREPARE_TO_LAUNCH: MissionInfo.Status
    QUALITY_BUMP_FIELD_NUMBER: _ClassVar[int]
    RESET_INDEX_FIELD_NUMBER: _ClassVar[int]
    RETURNED: MissionInfo.Status
    SECONDS_REMAINING_FIELD_NUMBER: _ClassVar[int]
    SHIP_FIELD_NUMBER: _ClassVar[int]
    SHORT: MissionInfo.DurationType
    STANDARD: MissionInfo.MissionType
    START_TIME_DERIVED_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TARGET_ARTIFACT_FIELD_NUMBER: _ClassVar[int]
    TUTORIAL: MissionInfo.DurationType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VIRTUE: MissionInfo.MissionType
    VOYEGGER: MissionInfo.Spaceship
    capacity: int
    duration_seconds: float
    duration_type: MissionInfo.DurationType
    fuel: _containers.RepeatedCompositeFieldContainer[MissionInfo.Fuel]
    identifier: str
    level: int
    mission_log: str
    quality_bump: float
    reset_index: int
    seconds_remaining: float
    ship: MissionInfo.Spaceship
    start_time_derived: float
    status: MissionInfo.Status
    target_artifact: ArtifactSpec.Name
    type: MissionInfo.MissionType
    def __init__(self, ship: _Optional[_Union[MissionInfo.Spaceship, str]] = ..., status: _Optional[_Union[MissionInfo.Status, str]] = ..., duration_type: _Optional[_Union[MissionInfo.DurationType, str]] = ..., type: _Optional[_Union[MissionInfo.MissionType, str]] = ..., reset_index: _Optional[int] = ..., fuel: _Optional[_Iterable[_Union[MissionInfo.Fuel, _Mapping]]] = ..., level: _Optional[int] = ..., duration_seconds: _Optional[float] = ..., capacity: _Optional[int] = ..., quality_bump: _Optional[float] = ..., target_artifact: _Optional[_Union[ArtifactSpec.Name, str]] = ..., seconds_remaining: _Optional[float] = ..., start_time_derived: _Optional[float] = ..., mission_log: _Optional[str] = ..., identifier: _Optional[str] = ...) -> None: ...

class MissionRequest(_message.Message):
    __slots__ = ["client_info", "client_version", "ei_user_id", "info", "rinfo"]
    CLIENT_INFO_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    EI_USER_ID_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    client_info: ArtifactsClientInfo
    client_version: int
    ei_user_id: str
    info: MissionInfo
    rinfo: BasicRequestInfo
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., client_version: _Optional[int] = ..., ei_user_id: _Optional[str] = ..., info: _Optional[_Union[MissionInfo, _Mapping]] = ..., client_info: _Optional[_Union[ArtifactsClientInfo, _Mapping]] = ...) -> None: ...

class MissionResponse(_message.Message):
    __slots__ = ["info", "success"]
    INFO_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    info: MissionInfo
    success: bool
    def __init__(self, success: bool = ..., info: _Optional[_Union[MissionInfo, _Mapping]] = ...) -> None: ...

class MyContracts(_message.Message):
    __slots__ = ["archive", "contract_ids_seen", "contracts", "current_coop_statuses", "custom_egg_info", "initial_grade_revealed", "last_cpi", "last_grade_progress_shown", "show_advanced_evaluations"]
    ARCHIVE_FIELD_NUMBER: _ClassVar[int]
    CONTRACTS_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_IDS_SEEN_FIELD_NUMBER: _ClassVar[int]
    CURRENT_COOP_STATUSES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_EGG_INFO_FIELD_NUMBER: _ClassVar[int]
    INITIAL_GRADE_REVEALED_FIELD_NUMBER: _ClassVar[int]
    LAST_CPI_FIELD_NUMBER: _ClassVar[int]
    LAST_GRADE_PROGRESS_SHOWN_FIELD_NUMBER: _ClassVar[int]
    SHOW_ADVANCED_EVALUATIONS_FIELD_NUMBER: _ClassVar[int]
    archive: _containers.RepeatedCompositeFieldContainer[LocalContract]
    contract_ids_seen: _containers.RepeatedScalarFieldContainer[str]
    contracts: _containers.RepeatedCompositeFieldContainer[LocalContract]
    current_coop_statuses: _containers.RepeatedCompositeFieldContainer[ContractCoopStatusResponse]
    custom_egg_info: _containers.RepeatedCompositeFieldContainer[CustomEgg]
    initial_grade_revealed: bool
    last_cpi: ContractPlayerInfo
    last_grade_progress_shown: float
    show_advanced_evaluations: bool
    def __init__(self, contract_ids_seen: _Optional[_Iterable[str]] = ..., contracts: _Optional[_Iterable[_Union[LocalContract, _Mapping]]] = ..., archive: _Optional[_Iterable[_Union[LocalContract, _Mapping]]] = ..., current_coop_statuses: _Optional[_Iterable[_Union[ContractCoopStatusResponse, _Mapping]]] = ..., last_cpi: _Optional[_Union[ContractPlayerInfo, _Mapping]] = ..., initial_grade_revealed: bool = ..., last_grade_progress_shown: _Optional[float] = ..., show_advanced_evaluations: bool = ..., custom_egg_info: _Optional[_Iterable[_Union[CustomEgg, _Mapping]]] = ...) -> None: ...

class PathOfVirtueInfo(_message.Message):
    __slots__ = ["reset_index", "server_time", "sim_time"]
    RESET_INDEX_FIELD_NUMBER: _ClassVar[int]
    SERVER_TIME_FIELD_NUMBER: _ClassVar[int]
    SIM_TIME_FIELD_NUMBER: _ClassVar[int]
    reset_index: int
    server_time: float
    sim_time: float
    def __init__(self, server_time: _Optional[float] = ..., sim_time: _Optional[float] = ..., reset_index: _Optional[int] = ...) -> None: ...

class PeriodicalsResponse(_message.Message):
    __slots__ = ["artifact_cases", "contract_player_info", "contracts", "evaluations", "events", "gifts", "live_config", "mail_bag", "sales", "showcase_royalties"]
    class RoyaltyInfo(_message.Message):
        __slots__ = ["amount", "id"]
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        amount: int
        id: str
        def __init__(self, id: _Optional[str] = ..., amount: _Optional[int] = ...) -> None: ...
    ARTIFACT_CASES_FIELD_NUMBER: _ClassVar[int]
    CONTRACTS_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_PLAYER_INFO_FIELD_NUMBER: _ClassVar[int]
    EVALUATIONS_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    GIFTS_FIELD_NUMBER: _ClassVar[int]
    LIVE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MAIL_BAG_FIELD_NUMBER: _ClassVar[int]
    SALES_FIELD_NUMBER: _ClassVar[int]
    SHOWCASE_ROYALTIES_FIELD_NUMBER: _ClassVar[int]
    artifact_cases: _containers.RepeatedCompositeFieldContainer[CompleteMissionResponse]
    contract_player_info: ContractPlayerInfo
    contracts: ContractsResponse
    evaluations: _containers.RepeatedCompositeFieldContainer[ContractEvaluation]
    events: EggIncCurrentEvents
    gifts: _containers.RepeatedCompositeFieldContainer[ServerGift]
    live_config: LiveConfig
    mail_bag: MailDB
    sales: SalesInfo
    showcase_royalties: _containers.RepeatedCompositeFieldContainer[PeriodicalsResponse.RoyaltyInfo]
    def __init__(self, sales: _Optional[_Union[SalesInfo, _Mapping]] = ..., events: _Optional[_Union[EggIncCurrentEvents, _Mapping]] = ..., contracts: _Optional[_Union[ContractsResponse, _Mapping]] = ..., evaluations: _Optional[_Iterable[_Union[ContractEvaluation, _Mapping]]] = ..., gifts: _Optional[_Iterable[_Union[ServerGift, _Mapping]]] = ..., artifact_cases: _Optional[_Iterable[_Union[CompleteMissionResponse, _Mapping]]] = ..., live_config: _Optional[_Union[LiveConfig, _Mapping]] = ..., mail_bag: _Optional[_Union[MailDB, _Mapping]] = ..., contract_player_info: _Optional[_Union[ContractPlayerInfo, _Mapping]] = ..., showcase_royalties: _Optional[_Iterable[_Union[PeriodicalsResponse.RoyaltyInfo, _Mapping]]] = ...) -> None: ...

class PlayerFarmInfo(_message.Message):
    __slots__ = ["active_boosts", "artifact_inventory_score", "boost_tokens_on_hand", "cash_on_hand", "client_version", "common_research", "egg_medal_level", "egg_type", "eggs_of_prophecy", "epic_research", "equipped_artifacts", "farm_appearance", "hab_capacity", "hab_population", "habs", "hyperloop_station", "permit_level", "silos_owned", "soul_eggs", "timestamp", "train_length", "vehicles"]
    ACTIVE_BOOSTS_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_INVENTORY_SCORE_FIELD_NUMBER: _ClassVar[int]
    BOOST_TOKENS_ON_HAND_FIELD_NUMBER: _ClassVar[int]
    CASH_ON_HAND_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    COMMON_RESEARCH_FIELD_NUMBER: _ClassVar[int]
    EGGS_OF_PROPHECY_FIELD_NUMBER: _ClassVar[int]
    EGG_MEDAL_LEVEL_FIELD_NUMBER: _ClassVar[int]
    EGG_TYPE_FIELD_NUMBER: _ClassVar[int]
    EPIC_RESEARCH_FIELD_NUMBER: _ClassVar[int]
    EQUIPPED_ARTIFACTS_FIELD_NUMBER: _ClassVar[int]
    FARM_APPEARANCE_FIELD_NUMBER: _ClassVar[int]
    HABS_FIELD_NUMBER: _ClassVar[int]
    HAB_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    HAB_POPULATION_FIELD_NUMBER: _ClassVar[int]
    HYPERLOOP_STATION_FIELD_NUMBER: _ClassVar[int]
    PERMIT_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SILOS_OWNED_FIELD_NUMBER: _ClassVar[int]
    SOUL_EGGS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TRAIN_LENGTH_FIELD_NUMBER: _ClassVar[int]
    VEHICLES_FIELD_NUMBER: _ClassVar[int]
    active_boosts: _containers.RepeatedCompositeFieldContainer[Backup.ActiveBoost]
    artifact_inventory_score: int
    boost_tokens_on_hand: int
    cash_on_hand: float
    client_version: int
    common_research: _containers.RepeatedCompositeFieldContainer[Backup.ResearchItem]
    egg_medal_level: _containers.RepeatedScalarFieldContainer[int]
    egg_type: Egg
    eggs_of_prophecy: int
    epic_research: _containers.RepeatedCompositeFieldContainer[Backup.ResearchItem]
    equipped_artifacts: _containers.RepeatedCompositeFieldContainer[CompleteArtifact]
    farm_appearance: ShellDB.FarmConfiguration
    hab_capacity: _containers.RepeatedScalarFieldContainer[int]
    hab_population: _containers.RepeatedScalarFieldContainer[int]
    habs: _containers.RepeatedScalarFieldContainer[int]
    hyperloop_station: bool
    permit_level: int
    silos_owned: int
    soul_eggs: float
    timestamp: float
    train_length: _containers.RepeatedScalarFieldContainer[int]
    vehicles: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, client_version: _Optional[int] = ..., soul_eggs: _Optional[float] = ..., eggs_of_prophecy: _Optional[int] = ..., permit_level: _Optional[int] = ..., hyperloop_station: bool = ..., egg_medal_level: _Optional[_Iterable[int]] = ..., epic_research: _Optional[_Iterable[_Union[Backup.ResearchItem, _Mapping]]] = ..., egg_type: _Optional[_Union[Egg, str]] = ..., cash_on_hand: _Optional[float] = ..., habs: _Optional[_Iterable[int]] = ..., hab_population: _Optional[_Iterable[int]] = ..., hab_capacity: _Optional[_Iterable[int]] = ..., vehicles: _Optional[_Iterable[int]] = ..., train_length: _Optional[_Iterable[int]] = ..., silos_owned: _Optional[int] = ..., common_research: _Optional[_Iterable[_Union[Backup.ResearchItem, _Mapping]]] = ..., active_boosts: _Optional[_Iterable[_Union[Backup.ActiveBoost, _Mapping]]] = ..., boost_tokens_on_hand: _Optional[int] = ..., equipped_artifacts: _Optional[_Iterable[_Union[CompleteArtifact, _Mapping]]] = ..., artifact_inventory_score: _Optional[int] = ..., farm_appearance: _Optional[_Union[ShellDB.FarmConfiguration, _Mapping]] = ..., timestamp: _Optional[float] = ...) -> None: ...

class PlayerLastChickenRunTimes(_message.Message):
    __slots__ = ["entries", "user_id"]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[CoopChickenRunEntry]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., entries: _Optional[_Iterable[_Union[CoopChickenRunEntry, _Mapping]]] = ...) -> None: ...

class QueryCoopRequest(_message.Message):
    __slots__ = ["client_version", "contract_identifier", "coop_identifier", "grade", "league", "rinfo"]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    COOP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    GRADE_FIELD_NUMBER: _ClassVar[int]
    LEAGUE_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    client_version: int
    contract_identifier: str
    coop_identifier: str
    grade: Contract.PlayerGrade
    league: int
    rinfo: BasicRequestInfo
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., contract_identifier: _Optional[str] = ..., coop_identifier: _Optional[str] = ..., league: _Optional[int] = ..., grade: _Optional[_Union[Contract.PlayerGrade, str]] = ..., client_version: _Optional[int] = ...) -> None: ...

class QueryCoopResponse(_message.Message):
    __slots__ = ["banned", "cc_only", "different_grade", "different_league", "exists", "expired", "full"]
    BANNED_FIELD_NUMBER: _ClassVar[int]
    CC_ONLY_FIELD_NUMBER: _ClassVar[int]
    DIFFERENT_GRADE_FIELD_NUMBER: _ClassVar[int]
    DIFFERENT_LEAGUE_FIELD_NUMBER: _ClassVar[int]
    EXISTS_FIELD_NUMBER: _ClassVar[int]
    EXPIRED_FIELD_NUMBER: _ClassVar[int]
    FULL_FIELD_NUMBER: _ClassVar[int]
    banned: bool
    cc_only: bool
    different_grade: bool
    different_league: bool
    exists: bool
    expired: bool
    full: bool
    def __init__(self, exists: bool = ..., full: bool = ..., expired: bool = ..., different_league: bool = ..., different_grade: bool = ..., cc_only: bool = ..., banned: bool = ...) -> None: ...

class ReportPlayerCoopRequest(_message.Message):
    __slots__ = ["contract_identifier", "coop_identifier", "reason", "rinfo", "user_id"]
    class Reason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CHEATING: ReportPlayerCoopRequest.Reason
    CONTRACT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    COOP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    LEECHING: ReportPlayerCoopRequest.Reason
    OFFENSIVE_NAME: ReportPlayerCoopRequest.Reason
    REASON_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN: ReportPlayerCoopRequest.Reason
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    contract_identifier: str
    coop_identifier: str
    reason: ReportPlayerCoopRequest.Reason
    rinfo: BasicRequestInfo
    user_id: str
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., contract_identifier: _Optional[str] = ..., coop_identifier: _Optional[str] = ..., user_id: _Optional[str] = ..., reason: _Optional[_Union[ReportPlayerCoopRequest.Reason, str]] = ...) -> None: ...

class ReturnEDTPayload(_message.Message):
    __slots__ = ["ei_user_id"]
    EI_USER_ID_FIELD_NUMBER: _ClassVar[int]
    ei_user_id: str
    def __init__(self, ei_user_id: _Optional[str] = ...) -> None: ...

class Reward(_message.Message):
    __slots__ = ["reward_amount", "reward_sub_type", "reward_type"]
    REWARD_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    REWARD_SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    REWARD_TYPE_FIELD_NUMBER: _ClassVar[int]
    reward_amount: float
    reward_sub_type: str
    reward_type: RewardType
    def __init__(self, reward_type: _Optional[_Union[RewardType, str]] = ..., reward_sub_type: _Optional[str] = ..., reward_amount: _Optional[float] = ...) -> None: ...

class SalesInfo(_message.Message):
    __slots__ = ["sales"]
    SALES_FIELD_NUMBER: _ClassVar[int]
    sales: _containers.RepeatedCompositeFieldContainer[IAPSaleEntry]
    def __init__(self, sales: _Optional[_Iterable[_Union[IAPSaleEntry, _Mapping]]] = ...) -> None: ...

class SalesInfoRequest(_message.Message):
    __slots__ = ["current_client_version", "lost_increments", "piggy_found_full", "piggy_full", "seconds_full_gametime", "seconds_full_realtime", "user_id"]
    CURRENT_CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    LOST_INCREMENTS_FIELD_NUMBER: _ClassVar[int]
    PIGGY_FOUND_FULL_FIELD_NUMBER: _ClassVar[int]
    PIGGY_FULL_FIELD_NUMBER: _ClassVar[int]
    SECONDS_FULL_GAMETIME_FIELD_NUMBER: _ClassVar[int]
    SECONDS_FULL_REALTIME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    current_client_version: int
    lost_increments: int
    piggy_found_full: bool
    piggy_full: bool
    seconds_full_gametime: float
    seconds_full_realtime: float
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., piggy_full: bool = ..., piggy_found_full: bool = ..., seconds_full_realtime: _Optional[float] = ..., seconds_full_gametime: _Optional[float] = ..., lost_increments: _Optional[int] = ..., current_client_version: _Optional[int] = ...) -> None: ...

class SaveBackupResponse(_message.Message):
    __slots__ = ["error_code", "existing_backup", "message", "success"]
    class ErrorCodes(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BACKUP_OFFERED: SaveBackupResponse.ErrorCodes
    BAD_USER_ID: SaveBackupResponse.ErrorCodes
    COULD_NOT_OVERWRITE: SaveBackupResponse.ErrorCodes
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    EXISTING_BACKUP_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    NO_ERROR: SaveBackupResponse.ErrorCodes
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    USER_NOT_FOUND: SaveBackupResponse.ErrorCodes
    error_code: int
    existing_backup: Backup
    message: str
    success: bool
    def __init__(self, success: bool = ..., error_code: _Optional[int] = ..., message: _Optional[str] = ..., existing_backup: _Optional[_Union[Backup, _Mapping]] = ...) -> None: ...

class SendChickenRunCoopRequest(_message.Message):
    __slots__ = ["client_version", "contract_identifier", "coop_identifier", "farm_pop", "player_identifier", "requesting_user_id", "requesting_user_name", "rinfo"]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    COOP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    FARM_POP_FIELD_NUMBER: _ClassVar[int]
    PLAYER_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    REQUESTING_USER_ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTING_USER_NAME_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    client_version: int
    contract_identifier: str
    coop_identifier: str
    farm_pop: int
    player_identifier: str
    requesting_user_id: str
    requesting_user_name: str
    rinfo: BasicRequestInfo
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., contract_identifier: _Optional[str] = ..., coop_identifier: _Optional[str] = ..., player_identifier: _Optional[str] = ..., requesting_user_id: _Optional[str] = ..., requesting_user_name: _Optional[str] = ..., farm_pop: _Optional[int] = ..., client_version: _Optional[int] = ...) -> None: ...

class ServerGift(_message.Message):
    __slots__ = ["reward_amount", "reward_sub_type", "reward_type", "user_id"]
    REWARD_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    REWARD_SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    REWARD_TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    reward_amount: float
    reward_sub_type: str
    reward_type: RewardType
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., reward_type: _Optional[_Union[RewardType, str]] = ..., reward_sub_type: _Optional[str] = ..., reward_amount: _Optional[float] = ...) -> None: ...

class SetArtifactRequest(_message.Message):
    __slots__ = ["artifact", "gold_price_paid", "rinfo", "stones"]
    ARTIFACT_FIELD_NUMBER: _ClassVar[int]
    GOLD_PRICE_PAID_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    STONES_FIELD_NUMBER: _ClassVar[int]
    artifact: ArtifactInventoryItem
    gold_price_paid: float
    rinfo: BasicRequestInfo
    stones: _containers.RepeatedCompositeFieldContainer[ArtifactSpec]
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., artifact: _Optional[_Union[ArtifactInventoryItem, _Mapping]] = ..., stones: _Optional[_Iterable[_Union[ArtifactSpec, _Mapping]]] = ..., gold_price_paid: _Optional[float] = ...) -> None: ...

class SetArtifactResponse(_message.Message):
    __slots__ = ["ei_user_id", "original_item_id", "success"]
    EI_USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ei_user_id: str
    original_item_id: int
    success: bool
    def __init__(self, success: bool = ..., original_item_id: _Optional[int] = ..., ei_user_id: _Optional[str] = ...) -> None: ...

class ShellDB(_message.Message):
    __slots__ = ["farm_configs", "last_showcase_featured_time_seen", "lighting_controls_unlocked", "new_shells_downloaded", "new_shells_seen", "saved_configs", "shell_element_inventory", "shell_inventory", "shell_object_inventory", "shell_set_inventory", "shell_variation_inventory"]
    class FarmElement(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class ChickenConfig(_message.Message):
        __slots__ = ["chicken_identifier", "hat_identifier"]
        CHICKEN_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        HAT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        chicken_identifier: str
        hat_identifier: str
        def __init__(self, chicken_identifier: _Optional[str] = ..., hat_identifier: _Optional[str] = ...) -> None: ...
    class FarmConfiguration(_message.Message):
        __slots__ = ["chicken_configs", "configure_chickens_by_group", "group_configs", "lighting_config", "lighting_config_enabled", "locked_elements", "shell_configs", "shell_set_configs"]
        CHICKEN_CONFIGS_FIELD_NUMBER: _ClassVar[int]
        CONFIGURE_CHICKENS_BY_GROUP_FIELD_NUMBER: _ClassVar[int]
        GROUP_CONFIGS_FIELD_NUMBER: _ClassVar[int]
        LIGHTING_CONFIG_ENABLED_FIELD_NUMBER: _ClassVar[int]
        LIGHTING_CONFIG_FIELD_NUMBER: _ClassVar[int]
        LOCKED_ELEMENTS_FIELD_NUMBER: _ClassVar[int]
        SHELL_CONFIGS_FIELD_NUMBER: _ClassVar[int]
        SHELL_SET_CONFIGS_FIELD_NUMBER: _ClassVar[int]
        chicken_configs: _containers.RepeatedCompositeFieldContainer[ShellDB.ChickenConfig]
        configure_chickens_by_group: bool
        group_configs: _containers.RepeatedCompositeFieldContainer[ShellDB.ShellGroupConfiguration]
        lighting_config: ShellDB.LightingConfig
        lighting_config_enabled: bool
        locked_elements: _containers.RepeatedScalarFieldContainer[ShellDB.FarmElement]
        shell_configs: _containers.RepeatedCompositeFieldContainer[ShellDB.ShellConfiguration]
        shell_set_configs: _containers.RepeatedCompositeFieldContainer[ShellDB.ShellSetConfiguration]
        def __init__(self, locked_elements: _Optional[_Iterable[_Union[ShellDB.FarmElement, str]]] = ..., shell_configs: _Optional[_Iterable[_Union[ShellDB.ShellConfiguration, _Mapping]]] = ..., shell_set_configs: _Optional[_Iterable[_Union[ShellDB.ShellSetConfiguration, _Mapping]]] = ..., configure_chickens_by_group: bool = ..., group_configs: _Optional[_Iterable[_Union[ShellDB.ShellGroupConfiguration, _Mapping]]] = ..., chicken_configs: _Optional[_Iterable[_Union[ShellDB.ChickenConfig, _Mapping]]] = ..., lighting_config_enabled: bool = ..., lighting_config: _Optional[_Union[ShellDB.LightingConfig, _Mapping]] = ...) -> None: ...
    class LightingConfig(_message.Message):
        __slots__ = ["fog_color", "fog_density", "fog_far", "fog_near", "light_ambient_color", "light_ambient_intensity", "light_dir", "light_direct_color", "light_direct_intensity"]
        FOG_COLOR_FIELD_NUMBER: _ClassVar[int]
        FOG_DENSITY_FIELD_NUMBER: _ClassVar[int]
        FOG_FAR_FIELD_NUMBER: _ClassVar[int]
        FOG_NEAR_FIELD_NUMBER: _ClassVar[int]
        LIGHT_AMBIENT_COLOR_FIELD_NUMBER: _ClassVar[int]
        LIGHT_AMBIENT_INTENSITY_FIELD_NUMBER: _ClassVar[int]
        LIGHT_DIRECT_COLOR_FIELD_NUMBER: _ClassVar[int]
        LIGHT_DIRECT_INTENSITY_FIELD_NUMBER: _ClassVar[int]
        LIGHT_DIR_FIELD_NUMBER: _ClassVar[int]
        fog_color: Vector4
        fog_density: float
        fog_far: float
        fog_near: float
        light_ambient_color: Vector4
        light_ambient_intensity: float
        light_dir: Vector3
        light_direct_color: Vector4
        light_direct_intensity: float
        def __init__(self, light_dir: _Optional[_Union[Vector3, _Mapping]] = ..., light_direct_color: _Optional[_Union[Vector4, _Mapping]] = ..., light_direct_intensity: _Optional[float] = ..., light_ambient_color: _Optional[_Union[Vector4, _Mapping]] = ..., light_ambient_intensity: _Optional[float] = ..., fog_color: _Optional[_Union[Vector4, _Mapping]] = ..., fog_near: _Optional[float] = ..., fog_far: _Optional[float] = ..., fog_density: _Optional[float] = ...) -> None: ...
    class SavedFarmConfiguration(_message.Message):
        __slots__ = ["client_save_time", "config", "display_name", "id", "purchased", "server_id"]
        CLIENT_SAVE_TIME_FIELD_NUMBER: _ClassVar[int]
        CONFIG_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        PURCHASED_FIELD_NUMBER: _ClassVar[int]
        SERVER_ID_FIELD_NUMBER: _ClassVar[int]
        client_save_time: float
        config: ShellDB.FarmConfiguration
        display_name: str
        id: str
        purchased: bool
        server_id: str
        def __init__(self, id: _Optional[str] = ..., config: _Optional[_Union[ShellDB.FarmConfiguration, _Mapping]] = ..., client_save_time: _Optional[float] = ..., server_id: _Optional[str] = ..., display_name: _Optional[str] = ..., purchased: bool = ...) -> None: ...
    class ShellConfiguration(_message.Message):
        __slots__ = ["asset_type", "index", "shell_identifier"]
        ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        SHELL_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        asset_type: ShellSpec.AssetType
        index: int
        shell_identifier: str
        def __init__(self, asset_type: _Optional[_Union[ShellSpec.AssetType, str]] = ..., index: _Optional[int] = ..., shell_identifier: _Optional[str] = ...) -> None: ...
    class ShellElementStatus(_message.Message):
        __slots__ = ["element", "set_identifier"]
        ELEMENT_FIELD_NUMBER: _ClassVar[int]
        SET_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        element: ShellDB.FarmElement
        set_identifier: str
        def __init__(self, element: _Optional[_Union[ShellDB.FarmElement, str]] = ..., set_identifier: _Optional[str] = ...) -> None: ...
    class ShellGroupConfiguration(_message.Message):
        __slots__ = ["asset_type", "group_identifier"]
        ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
        GROUP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        asset_type: ShellSpec.AssetType
        group_identifier: str
        def __init__(self, asset_type: _Optional[_Union[ShellSpec.AssetType, str]] = ..., group_identifier: _Optional[str] = ...) -> None: ...
    class ShellSetConfiguration(_message.Message):
        __slots__ = ["decorator_identifier", "element", "index", "shell_set_identifier", "variation_identifier"]
        DECORATOR_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        ELEMENT_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        SHELL_SET_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        VARIATION_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        decorator_identifier: str
        element: ShellDB.FarmElement
        index: int
        shell_set_identifier: str
        variation_identifier: str
        def __init__(self, element: _Optional[_Union[ShellDB.FarmElement, str]] = ..., index: _Optional[int] = ..., shell_set_identifier: _Optional[str] = ..., variation_identifier: _Optional[str] = ..., decorator_identifier: _Optional[str] = ...) -> None: ...
    class ShellSetVariationStatus(_message.Message):
        __slots__ = ["owned_variations", "set_identifier"]
        OWNED_VARIATIONS_FIELD_NUMBER: _ClassVar[int]
        SET_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        owned_variations: _containers.RepeatedScalarFieldContainer[str]
        set_identifier: str
        def __init__(self, set_identifier: _Optional[str] = ..., owned_variations: _Optional[_Iterable[str]] = ...) -> None: ...
    class ShellStatus(_message.Message):
        __slots__ = ["identifier", "owned"]
        IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        OWNED_FIELD_NUMBER: _ClassVar[int]
        identifier: str
        owned: bool
        def __init__(self, identifier: _Optional[str] = ..., owned: bool = ...) -> None: ...
    CHICKEN: ShellDB.FarmElement
    DEPOT: ShellDB.FarmElement
    FARM_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    FUEL_TANK: ShellDB.FarmElement
    GROUND: ShellDB.FarmElement
    HARDSCAPE: ShellDB.FarmElement
    HAT: ShellDB.FarmElement
    HATCHERY: ShellDB.FarmElement
    HEN_HOUSE: ShellDB.FarmElement
    HOA: ShellDB.FarmElement
    HYPERLOOP: ShellDB.FarmElement
    LAB: ShellDB.FarmElement
    LAST_SHOWCASE_FEATURED_TIME_SEEN_FIELD_NUMBER: _ClassVar[int]
    LIGHTING_CONTROLS_UNLOCKED_FIELD_NUMBER: _ClassVar[int]
    MAILBOX: ShellDB.FarmElement
    MISSION_CONTROL: ShellDB.FarmElement
    NEW_SHELLS_DOWNLOADED_FIELD_NUMBER: _ClassVar[int]
    NEW_SHELLS_SEEN_FIELD_NUMBER: _ClassVar[int]
    SAVED_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    SHELL_ELEMENT_INVENTORY_FIELD_NUMBER: _ClassVar[int]
    SHELL_INVENTORY_FIELD_NUMBER: _ClassVar[int]
    SHELL_OBJECT_INVENTORY_FIELD_NUMBER: _ClassVar[int]
    SHELL_SET_INVENTORY_FIELD_NUMBER: _ClassVar[int]
    SHELL_VARIATION_INVENTORY_FIELD_NUMBER: _ClassVar[int]
    SILO: ShellDB.FarmElement
    TROPHY_CASE: ShellDB.FarmElement
    UNKNOWN: ShellDB.FarmElement
    farm_configs: _containers.RepeatedCompositeFieldContainer[ShellDB.FarmConfiguration]
    last_showcase_featured_time_seen: float
    lighting_controls_unlocked: bool
    new_shells_downloaded: _containers.RepeatedScalarFieldContainer[str]
    new_shells_seen: _containers.RepeatedScalarFieldContainer[str]
    saved_configs: _containers.RepeatedCompositeFieldContainer[ShellDB.SavedFarmConfiguration]
    shell_element_inventory: _containers.RepeatedCompositeFieldContainer[ShellDB.ShellElementStatus]
    shell_inventory: _containers.RepeatedCompositeFieldContainer[ShellDB.ShellStatus]
    shell_object_inventory: _containers.RepeatedCompositeFieldContainer[ShellDB.ShellStatus]
    shell_set_inventory: _containers.RepeatedCompositeFieldContainer[ShellDB.ShellStatus]
    shell_variation_inventory: _containers.RepeatedCompositeFieldContainer[ShellDB.ShellSetVariationStatus]
    def __init__(self, shell_inventory: _Optional[_Iterable[_Union[ShellDB.ShellStatus, _Mapping]]] = ..., shell_element_inventory: _Optional[_Iterable[_Union[ShellDB.ShellElementStatus, _Mapping]]] = ..., shell_variation_inventory: _Optional[_Iterable[_Union[ShellDB.ShellSetVariationStatus, _Mapping]]] = ..., shell_set_inventory: _Optional[_Iterable[_Union[ShellDB.ShellStatus, _Mapping]]] = ..., shell_object_inventory: _Optional[_Iterable[_Union[ShellDB.ShellStatus, _Mapping]]] = ..., farm_configs: _Optional[_Iterable[_Union[ShellDB.FarmConfiguration, _Mapping]]] = ..., saved_configs: _Optional[_Iterable[_Union[ShellDB.SavedFarmConfiguration, _Mapping]]] = ..., new_shells_downloaded: _Optional[_Iterable[str]] = ..., new_shells_seen: _Optional[_Iterable[str]] = ..., last_showcase_featured_time_seen: _Optional[float] = ..., lighting_controls_unlocked: bool = ...) -> None: ...

class ShellGroupSpec(_message.Message):
    __slots__ = ["asset_type", "identifier", "member_ids", "name", "price_mult_DEPRECATED"]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRICE_MULT_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    asset_type: ShellSpec.AssetType
    identifier: str
    member_ids: _containers.RepeatedScalarFieldContainer[str]
    name: str
    price_mult_DEPRECATED: float
    def __init__(self, identifier: _Optional[str] = ..., name: _Optional[str] = ..., asset_type: _Optional[_Union[ShellSpec.AssetType, str]] = ..., member_ids: _Optional[_Iterable[str]] = ..., price_mult_DEPRECATED: _Optional[float] = ...) -> None: ...

class ShellObjectSpec(_message.Message):
    __slots__ = ["asset_type", "chicken_animation", "default_appearance", "expires", "icon_colors", "identifier", "is_new", "metadata", "name", "no_hats", "object_class", "pieces", "popularity", "price", "required_eop", "required_soul_eggs", "seconds_remaining", "seconds_until_available", "sort_priority"]
    class ChickenAnimation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class LODPiece(_message.Message):
        __slots__ = ["dlc", "lod"]
        DLC_FIELD_NUMBER: _ClassVar[int]
        LOD_FIELD_NUMBER: _ClassVar[int]
        dlc: DLCItem
        lod: int
        def __init__(self, dlc: _Optional[_Union[DLCItem, _Mapping]] = ..., lod: _Optional[int] = ...) -> None: ...
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHICKEN_ANIMATION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_APPEARANCE_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_FIELD_NUMBER: _ClassVar[int]
    HOVER: ShellObjectSpec.ChickenAnimation
    ICON_COLORS_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    IS_NEW_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NO_HATS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CLASS_FIELD_NUMBER: _ClassVar[int]
    PIECES_FIELD_NUMBER: _ClassVar[int]
    POPULARITY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_EOP_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_SOUL_EGGS_FIELD_NUMBER: _ClassVar[int]
    SECONDS_REMAINING_FIELD_NUMBER: _ClassVar[int]
    SECONDS_UNTIL_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    SIDEWAYS_LEAN: ShellObjectSpec.ChickenAnimation
    SIDEWAYS_SMOOTH: ShellObjectSpec.ChickenAnimation
    SLOWMO: ShellObjectSpec.ChickenAnimation
    SMOOTH: ShellObjectSpec.ChickenAnimation
    SMOOTH_LEAN: ShellObjectSpec.ChickenAnimation
    SORT_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    STANDARD_RUN: ShellObjectSpec.ChickenAnimation
    WOBBLE: ShellObjectSpec.ChickenAnimation
    WOBBLE_LEAN: ShellObjectSpec.ChickenAnimation
    asset_type: ShellSpec.AssetType
    chicken_animation: ShellObjectSpec.ChickenAnimation
    default_appearance: bool
    expires: bool
    icon_colors: _containers.RepeatedScalarFieldContainer[str]
    identifier: str
    is_new: bool
    metadata: _containers.RepeatedScalarFieldContainer[float]
    name: str
    no_hats: bool
    object_class: str
    pieces: _containers.RepeatedCompositeFieldContainer[ShellObjectSpec.LODPiece]
    popularity: int
    price: int
    required_eop: int
    required_soul_eggs: float
    seconds_remaining: float
    seconds_until_available: float
    sort_priority: int
    def __init__(self, identifier: _Optional[str] = ..., name: _Optional[str] = ..., asset_type: _Optional[_Union[ShellSpec.AssetType, str]] = ..., object_class: _Optional[str] = ..., icon_colors: _Optional[_Iterable[str]] = ..., price: _Optional[int] = ..., required_eop: _Optional[int] = ..., required_soul_eggs: _Optional[float] = ..., is_new: bool = ..., expires: bool = ..., seconds_until_available: _Optional[float] = ..., seconds_remaining: _Optional[float] = ..., popularity: _Optional[int] = ..., metadata: _Optional[_Iterable[float]] = ..., no_hats: bool = ..., chicken_animation: _Optional[_Union[ShellObjectSpec.ChickenAnimation, str]] = ..., sort_priority: _Optional[int] = ..., pieces: _Optional[_Iterable[_Union[ShellObjectSpec.LODPiece, _Mapping]]] = ..., default_appearance: bool = ...) -> None: ...

class ShellPopularityStats(_message.Message):
    __slots__ = ["data"]
    class Entry(_message.Message):
        __slots__ = ["count", "element", "id", "spent"]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        ELEMENT_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        SPENT_FIELD_NUMBER: _ClassVar[int]
        count: int
        element: ShellDB.FarmElement
        id: str
        spent: int
        def __init__(self, id: _Optional[str] = ..., element: _Optional[_Union[ShellDB.FarmElement, str]] = ..., spent: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[ShellPopularityStats.Entry]
    def __init__(self, data: _Optional[_Iterable[_Union[ShellPopularityStats.Entry, _Mapping]]] = ...) -> None: ...

class ShellSetSpec(_message.Message):
    __slots__ = ["custom_appearance", "decorator", "default_appearance", "discount", "element_set", "expires", "hex_base_color", "icon", "identifier", "is_new", "modified_geometry", "name", "popularity", "price", "price_mult_DEPRECATED", "required_eop", "required_parent_set", "required_soul_eggs", "seconds_remaining", "seconds_until_available", "variations"]
    class VariationSpec(_message.Message):
        __slots__ = ["custom_appearance", "default_appearance", "hex_color", "identifier", "price", "sort_priority"]
        CUSTOM_APPEARANCE_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_APPEARANCE_FIELD_NUMBER: _ClassVar[int]
        HEX_COLOR_FIELD_NUMBER: _ClassVar[int]
        IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        PRICE_FIELD_NUMBER: _ClassVar[int]
        SORT_PRIORITY_FIELD_NUMBER: _ClassVar[int]
        custom_appearance: bool
        default_appearance: bool
        hex_color: str
        identifier: str
        price: int
        sort_priority: int
        def __init__(self, identifier: _Optional[str] = ..., hex_color: _Optional[str] = ..., price: _Optional[int] = ..., sort_priority: _Optional[int] = ..., default_appearance: bool = ..., custom_appearance: bool = ...) -> None: ...
    CUSTOM_APPEARANCE_FIELD_NUMBER: _ClassVar[int]
    DECORATOR_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_APPEARANCE_FIELD_NUMBER: _ClassVar[int]
    DISCOUNT_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_SET_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_FIELD_NUMBER: _ClassVar[int]
    HEX_BASE_COLOR_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    IS_NEW_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    POPULARITY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    PRICE_MULT_DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_EOP_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_PARENT_SET_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_SOUL_EGGS_FIELD_NUMBER: _ClassVar[int]
    SECONDS_REMAINING_FIELD_NUMBER: _ClassVar[int]
    SECONDS_UNTIL_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    VARIATIONS_FIELD_NUMBER: _ClassVar[int]
    custom_appearance: bool
    decorator: bool
    default_appearance: bool
    discount: float
    element_set: bool
    expires: bool
    hex_base_color: str
    icon: DLCItem
    identifier: str
    is_new: bool
    modified_geometry: bool
    name: str
    popularity: int
    price: int
    price_mult_DEPRECATED: float
    required_eop: int
    required_parent_set: str
    required_soul_eggs: float
    seconds_remaining: float
    seconds_until_available: float
    variations: _containers.RepeatedCompositeFieldContainer[ShellSetSpec.VariationSpec]
    def __init__(self, identifier: _Optional[str] = ..., name: _Optional[str] = ..., price: _Optional[int] = ..., price_mult_DEPRECATED: _Optional[float] = ..., discount: _Optional[float] = ..., required_eop: _Optional[int] = ..., required_soul_eggs: _Optional[float] = ..., required_parent_set: _Optional[str] = ..., is_new: bool = ..., expires: bool = ..., seconds_until_available: _Optional[float] = ..., seconds_remaining: _Optional[float] = ..., popularity: _Optional[int] = ..., decorator: bool = ..., modified_geometry: bool = ..., element_set: bool = ..., hex_base_color: _Optional[str] = ..., variations: _Optional[_Iterable[_Union[ShellSetSpec.VariationSpec, _Mapping]]] = ..., icon: _Optional[_Union[DLCItem, _Mapping]] = ..., default_appearance: bool = ..., custom_appearance: bool = ...) -> None: ...

class ShellShowcase(_message.Message):
    __slots__ = ["featured", "fresh", "top"]
    FEATURED_FIELD_NUMBER: _ClassVar[int]
    FRESH_FIELD_NUMBER: _ClassVar[int]
    TOP_FIELD_NUMBER: _ClassVar[int]
    featured: _containers.RepeatedCompositeFieldContainer[ShellShowcaseListingInfo]
    fresh: _containers.RepeatedCompositeFieldContainer[ShellShowcaseListingInfo]
    top: _containers.RepeatedCompositeFieldContainer[ShellShowcaseListingInfo]
    def __init__(self, top: _Optional[_Iterable[_Union[ShellShowcaseListingInfo, _Mapping]]] = ..., featured: _Optional[_Iterable[_Union[ShellShowcaseListingInfo, _Mapping]]] = ..., fresh: _Optional[_Iterable[_Union[ShellShowcaseListingInfo, _Mapping]]] = ...) -> None: ...

class ShellShowcaseListingInfo(_message.Message):
    __slots__ = ["creator_name", "description", "dislikes", "equips", "farm_config", "gross", "id", "is_new", "likes", "local_id", "name", "sales", "share_url", "status", "views"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ARCHIVED: ShellShowcaseListingInfo.Status
    CREATOR_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISLIKES_FIELD_NUMBER: _ClassVar[int]
    EQUIPS_FIELD_NUMBER: _ClassVar[int]
    FARM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    FEATURED: ShellShowcaseListingInfo.Status
    FEATURED_ALUM: ShellShowcaseListingInfo.Status
    GROSS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INVALID: ShellShowcaseListingInfo.Status
    IS_NEW_FIELD_NUMBER: _ClassVar[int]
    LIKES_FIELD_NUMBER: _ClassVar[int]
    LIVE: ShellShowcaseListingInfo.Status
    LOCAL_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NONE: ShellShowcaseListingInfo.Status
    SALES_FIELD_NUMBER: _ClassVar[int]
    SHARE_URL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUBMITTED: ShellShowcaseListingInfo.Status
    VIEWS_FIELD_NUMBER: _ClassVar[int]
    creator_name: str
    description: str
    dislikes: int
    equips: int
    farm_config: ShellDB.FarmConfiguration
    gross: int
    id: str
    is_new: bool
    likes: int
    local_id: str
    name: str
    sales: int
    share_url: str
    status: ShellShowcaseListingInfo.Status
    views: int
    def __init__(self, id: _Optional[str] = ..., local_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., is_new: bool = ..., creator_name: _Optional[str] = ..., status: _Optional[_Union[ShellShowcaseListingInfo.Status, str]] = ..., farm_config: _Optional[_Union[ShellDB.FarmConfiguration, _Mapping]] = ..., sales: _Optional[int] = ..., gross: _Optional[int] = ..., views: _Optional[int] = ..., equips: _Optional[int] = ..., likes: _Optional[int] = ..., dislikes: _Optional[int] = ..., share_url: _Optional[str] = ...) -> None: ...

class ShellShowcaseListingSet(_message.Message):
    __slots__ = ["listings"]
    LISTINGS_FIELD_NUMBER: _ClassVar[int]
    listings: _containers.RepeatedCompositeFieldContainer[ShellShowcaseListingInfo]
    def __init__(self, listings: _Optional[_Iterable[_Union[ShellShowcaseListingInfo, _Mapping]]] = ...) -> None: ...

class ShellSpec(_message.Message):
    __slots__ = ["alt_assets", "default_appearance", "expires", "identifier", "is_new", "modified_geometry", "name", "pieces", "popularity", "price", "primary_piece", "required_eop", "required_parent_shell", "required_soul_eggs", "seconds_remaining", "seconds_until_available", "set_identifier"]
    class AssetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class ShellPiece(_message.Message):
        __slots__ = ["asset_type", "dlc"]
        ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
        DLC_FIELD_NUMBER: _ClassVar[int]
        asset_type: ShellSpec.AssetType
        dlc: DLCItem
        def __init__(self, asset_type: _Optional[_Union[ShellSpec.AssetType, str]] = ..., dlc: _Optional[_Union[DLCItem, _Mapping]] = ...) -> None: ...
    ALT_ASSETS_FIELD_NUMBER: _ClassVar[int]
    BUNKER: ShellSpec.AssetType
    CENTER: ShellSpec.AssetType
    CHICKEN: ShellSpec.AssetType
    CHICKEN_UNIVERSE: ShellSpec.AssetType
    COOP: ShellSpec.AssetType
    DEFAULT_APPEARANCE_FIELD_NUMBER: _ClassVar[int]
    DEPOT_1: ShellSpec.AssetType
    DEPOT_2: ShellSpec.AssetType
    DEPOT_3: ShellSpec.AssetType
    DEPOT_4: ShellSpec.AssetType
    DEPOT_5: ShellSpec.AssetType
    DEPOT_6: ShellSpec.AssetType
    DEPOT_7: ShellSpec.AssetType
    DOUBLE_DECKER: ShellSpec.AssetType
    EGGKEA: ShellSpec.AssetType
    EGGTOPIA: ShellSpec.AssetType
    EXPIRES_FIELD_NUMBER: _ClassVar[int]
    FUEL_TANK_1: ShellSpec.AssetType
    FUEL_TANK_2: ShellSpec.AssetType
    FUEL_TANK_3: ShellSpec.AssetType
    FUEL_TANK_4: ShellSpec.AssetType
    GROUND: ShellSpec.AssetType
    HAB_10K: ShellSpec.AssetType
    HAB_1K: ShellSpec.AssetType
    HANGAR: ShellSpec.AssetType
    HARDSCAPE: ShellSpec.AssetType
    HAT: ShellSpec.AssetType
    HATCHERY_AI: ShellSpec.AssetType
    HATCHERY_AI_TOP_1: ShellSpec.AssetType
    HATCHERY_AI_TOP_2: ShellSpec.AssetType
    HATCHERY_AI_TOP_3: ShellSpec.AssetType
    HATCHERY_AI_TOP_4: ShellSpec.AssetType
    HATCHERY_ANTIMATTER: ShellSpec.AssetType
    HATCHERY_CHOCOLATE: ShellSpec.AssetType
    HATCHERY_CURIOSITY: ShellSpec.AssetType
    HATCHERY_CURIOSITY_EXTRA: ShellSpec.AssetType
    HATCHERY_CUSTOM: ShellSpec.AssetType
    HATCHERY_DARK_MATTER: ShellSpec.AssetType
    HATCHERY_DARK_MATTER_RING_1: ShellSpec.AssetType
    HATCHERY_DARK_MATTER_RING_2: ShellSpec.AssetType
    HATCHERY_DARK_MATTER_RING_3: ShellSpec.AssetType
    HATCHERY_DILITHIUM: ShellSpec.AssetType
    HATCHERY_EASTER: ShellSpec.AssetType
    HATCHERY_EDIBLE: ShellSpec.AssetType
    HATCHERY_ENLIGHTENMENT: ShellSpec.AssetType
    HATCHERY_ENLIGHTENMENT_ORB: ShellSpec.AssetType
    HATCHERY_FIREWORK: ShellSpec.AssetType
    HATCHERY_FUSION: ShellSpec.AssetType
    HATCHERY_GRAVITON: ShellSpec.AssetType
    HATCHERY_GRAVITON_TOP: ShellSpec.AssetType
    HATCHERY_HUMILITY: ShellSpec.AssetType
    HATCHERY_HUMILITY_EXTRA: ShellSpec.AssetType
    HATCHERY_IMMORTALITY: ShellSpec.AssetType
    HATCHERY_INTEGRITY: ShellSpec.AssetType
    HATCHERY_INTEGRITY_EXTRA: ShellSpec.AssetType
    HATCHERY_KINDNESS: ShellSpec.AssetType
    HATCHERY_KINDNESS_EXTRA: ShellSpec.AssetType
    HATCHERY_MEDICAL: ShellSpec.AssetType
    HATCHERY_NEBULA: ShellSpec.AssetType
    HATCHERY_NEBULA_MIDDLE: ShellSpec.AssetType
    HATCHERY_NEBULA_TOP: ShellSpec.AssetType
    HATCHERY_PRODIGY: ShellSpec.AssetType
    HATCHERY_PUMPKIN: ShellSpec.AssetType
    HATCHERY_QUANTUM: ShellSpec.AssetType
    HATCHERY_RESILIENCE: ShellSpec.AssetType
    HATCHERY_RESILIENCE_EXTRA: ShellSpec.AssetType
    HATCHERY_ROCKET_FUEL: ShellSpec.AssetType
    HATCHERY_SUPERFOOD: ShellSpec.AssetType
    HATCHERY_SUPERMATERIAL: ShellSpec.AssetType
    HATCHERY_TACHYON: ShellSpec.AssetType
    HATCHERY_TERRAFORM: ShellSpec.AssetType
    HATCHERY_UNIVERSE: ShellSpec.AssetType
    HATCHERY_UNIVERSE_BOLT: ShellSpec.AssetType
    HATCHERY_UNIVERSE_PROBE: ShellSpec.AssetType
    HATCHERY_WATERBALLOON: ShellSpec.AssetType
    HOA_1: ShellSpec.AssetType
    HOA_2: ShellSpec.AssetType
    HOA_3: ShellSpec.AssetType
    HYPERLOOP: ShellSpec.AssetType
    HYPERLOOP_TRACK: ShellSpec.AssetType
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    IS_NEW_FIELD_NUMBER: _ClassVar[int]
    LAB_1: ShellSpec.AssetType
    LAB_2: ShellSpec.AssetType
    LAB_3: ShellSpec.AssetType
    LAB_4: ShellSpec.AssetType
    LAB_5: ShellSpec.AssetType
    LAB_6: ShellSpec.AssetType
    LONG_HOUSE: ShellSpec.AssetType
    MAILBOX: ShellSpec.AssetType
    MAILBOX_FULL: ShellSpec.AssetType
    MISSION_CONTROL_1: ShellSpec.AssetType
    MISSION_CONTROL_2: ShellSpec.AssetType
    MISSION_CONTROL_3: ShellSpec.AssetType
    MODIFIED_GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    MONOLITH: ShellSpec.AssetType
    NAME_FIELD_NUMBER: _ClassVar[int]
    PIECES_FIELD_NUMBER: _ClassVar[int]
    PLANET_PORTAL: ShellSpec.AssetType
    POPULARITY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_PIECE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_EOP_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_PARENT_SHELL_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_SOUL_EGGS_FIELD_NUMBER: _ClassVar[int]
    SECONDS_REMAINING_FIELD_NUMBER: _ClassVar[int]
    SECONDS_UNTIL_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    SET_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    SHACK: ShellSpec.AssetType
    SHORT_HOUSE: ShellSpec.AssetType
    SILO_0_LARGE: ShellSpec.AssetType
    SILO_0_MED: ShellSpec.AssetType
    SILO_0_SMALL: ShellSpec.AssetType
    SILO_1_LARGE: ShellSpec.AssetType
    SILO_1_MED: ShellSpec.AssetType
    SILO_1_SMALL: ShellSpec.AssetType
    SILO_ALL: ShellSpec.AssetType
    SUPER_SHACK: ShellSpec.AssetType
    THE_STANDARD: ShellSpec.AssetType
    TOWER: ShellSpec.AssetType
    TROPHY_CASE: ShellSpec.AssetType
    UNKNOWN: ShellSpec.AssetType
    WAREHOUSE: ShellSpec.AssetType
    alt_assets: _containers.RepeatedCompositeFieldContainer[DLCItem]
    default_appearance: bool
    expires: bool
    identifier: str
    is_new: bool
    modified_geometry: bool
    name: str
    pieces: _containers.RepeatedCompositeFieldContainer[ShellSpec.ShellPiece]
    popularity: int
    price: int
    primary_piece: ShellSpec.ShellPiece
    required_eop: int
    required_parent_shell: str
    required_soul_eggs: float
    seconds_remaining: float
    seconds_until_available: float
    set_identifier: str
    def __init__(self, identifier: _Optional[str] = ..., primary_piece: _Optional[_Union[ShellSpec.ShellPiece, _Mapping]] = ..., pieces: _Optional[_Iterable[_Union[ShellSpec.ShellPiece, _Mapping]]] = ..., alt_assets: _Optional[_Iterable[_Union[DLCItem, _Mapping]]] = ..., name: _Optional[str] = ..., set_identifier: _Optional[str] = ..., modified_geometry: bool = ..., price: _Optional[int] = ..., required_eop: _Optional[int] = ..., required_soul_eggs: _Optional[float] = ..., required_parent_shell: _Optional[str] = ..., is_new: bool = ..., expires: bool = ..., seconds_until_available: _Optional[float] = ..., seconds_remaining: _Optional[float] = ..., popularity: _Optional[int] = ..., default_appearance: bool = ...) -> None: ...

class ShellsActionBatch(_message.Message):
    __slots__ = ["actions", "rinfo"]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedCompositeFieldContainer[ShellsActionLog]
    rinfo: BasicRequestInfo
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., actions: _Optional[_Iterable[_Union[ShellsActionLog, _Mapping]]] = ...) -> None: ...

class ShellsActionLog(_message.Message):
    __slots__ = ["action", "approx_time", "cost", "farm_element", "farm_index", "gold_spent", "rinfo", "soul_eggs", "sub_id", "tickets_spent", "user_id", "version"]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    APPROX_TIME_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    FARM_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    FARM_INDEX_FIELD_NUMBER: _ClassVar[int]
    GOLD_SPENT_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    SOUL_EGGS_FIELD_NUMBER: _ClassVar[int]
    SUB_ID_FIELD_NUMBER: _ClassVar[int]
    TICKETS_SPENT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    action: str
    approx_time: float
    cost: int
    farm_element: ShellDB.FarmElement
    farm_index: int
    gold_spent: int
    rinfo: BasicRequestInfo
    soul_eggs: float
    sub_id: str
    tickets_spent: int
    user_id: str
    version: str
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., user_id: _Optional[str] = ..., action: _Optional[str] = ..., sub_id: _Optional[str] = ..., farm_element: _Optional[_Union[ShellDB.FarmElement, str]] = ..., cost: _Optional[int] = ..., approx_time: _Optional[float] = ..., version: _Optional[str] = ..., farm_index: _Optional[int] = ..., soul_eggs: _Optional[float] = ..., tickets_spent: _Optional[int] = ..., gold_spent: _Optional[int] = ...) -> None: ...

class ShowcaseRoyaltyDeliveryConfirmation(_message.Message):
    __slots__ = ["amount", "ids", "rinfo"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    amount: int
    ids: _containers.RepeatedScalarFieldContainer[str]
    rinfo: BasicRequestInfo
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., ids: _Optional[_Iterable[str]] = ..., amount: _Optional[int] = ...) -> None: ...

class SubmitShellShowcaseRequest(_message.Message):
    __slots__ = ["farm_config", "local_id", "public_username", "rinfo", "user_id"]
    FARM_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_USERNAME_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    farm_config: ShellDB.FarmConfiguration
    local_id: str
    public_username: bool
    rinfo: BasicRequestInfo
    user_id: str
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., local_id: _Optional[str] = ..., user_id: _Optional[str] = ..., public_username: bool = ..., farm_config: _Optional[_Union[ShellDB.FarmConfiguration, _Mapping]] = ...) -> None: ...

class SubscriptionChangeHintRequest(_message.Message):
    __slots__ = ["next_subscription_level", "original_transaction_id", "rinfo"]
    NEXT_SUBSCRIPTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    next_subscription_level: UserSubscriptionInfo.Level
    original_transaction_id: str
    rinfo: BasicRequestInfo
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., original_transaction_id: _Optional[str] = ..., next_subscription_level: _Optional[_Union[UserSubscriptionInfo.Level, str]] = ...) -> None: ...

class SyncPathOfVirtueRequest(_message.Message):
    __slots__ = ["reset_index", "rinfo", "sim_time"]
    RESET_INDEX_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    SIM_TIME_FIELD_NUMBER: _ClassVar[int]
    reset_index: int
    rinfo: BasicRequestInfo
    sim_time: float
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., reset_index: _Optional[int] = ..., sim_time: _Optional[float] = ...) -> None: ...

class SyncPathOfVirtueResponse(_message.Message):
    __slots__ = ["sim_debt", "status"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    OK: SyncPathOfVirtueResponse.Status
    PROBLEM: SyncPathOfVirtueResponse.Status
    SIM_DEBT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    sim_debt: float
    status: SyncPathOfVirtueResponse.Status
    def __init__(self, status: _Optional[_Union[SyncPathOfVirtueResponse.Status, str]] = ..., sim_debt: _Optional[float] = ...) -> None: ...

class TipsDB(_message.Message):
    __slots__ = ["tips"]
    TIPS_FIELD_NUMBER: _ClassVar[int]
    tips: _containers.RepeatedCompositeFieldContainer[InGameMail]
    def __init__(self, tips: _Optional[_Iterable[_Union[InGameMail, _Mapping]]] = ...) -> None: ...

class UpdateCoopPermissionsRequest(_message.Message):
    __slots__ = ["client_version", "contract_identifier", "coop_identifier", "public", "requesting_user_id", "rinfo"]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    COOP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    REQUESTING_USER_ID_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    client_version: int
    contract_identifier: str
    coop_identifier: str
    public: bool
    requesting_user_id: str
    rinfo: BasicRequestInfo
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., contract_identifier: _Optional[str] = ..., coop_identifier: _Optional[str] = ..., requesting_user_id: _Optional[str] = ..., public: bool = ..., client_version: _Optional[int] = ...) -> None: ...

class UpdateCoopPermissionsResponse(_message.Message):
    __slots__ = ["message", "success"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    message: str
    success: bool
    def __init__(self, success: bool = ..., message: _Optional[str] = ...) -> None: ...

class UserDataInfoRequest(_message.Message):
    __slots__ = ["backup_checksum", "device_id", "rinfo", "user_id"]
    BACKUP_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    backup_checksum: int
    device_id: str
    rinfo: BasicRequestInfo
    user_id: str
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., user_id: _Optional[str] = ..., device_id: _Optional[str] = ..., backup_checksum: _Optional[int] = ...) -> None: ...

class UserDataInfoResponse(_message.Message):
    __slots__ = ["backup_checksum", "backup_total_cash", "coop_memberships"]
    BACKUP_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    BACKUP_TOTAL_CASH_FIELD_NUMBER: _ClassVar[int]
    COOP_MEMBERSHIPS_FIELD_NUMBER: _ClassVar[int]
    backup_checksum: int
    backup_total_cash: float
    coop_memberships: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, backup_checksum: _Optional[int] = ..., backup_total_cash: _Optional[float] = ..., coop_memberships: _Optional[_Iterable[str]] = ...) -> None: ...

class UserSubscriptionInfo(_message.Message):
    __slots__ = ["acknowledged", "auto_renew", "first_subscribed", "history", "last_updated", "linked_transaction_id", "lock_next_subscription_level", "next_subscription_level", "original_transaction_id", "past_user_ids", "period_end", "platform", "sandbox", "status", "store_status", "subscription_level"]
    class Level(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class HistoryEntry(_message.Message):
        __slots__ = ["message", "message_id", "timestamp"]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        message: str
        message_id: str
        timestamp: float
        def __init__(self, timestamp: _Optional[float] = ..., message_id: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...
    ACKNOWLEDGED_FIELD_NUMBER: _ClassVar[int]
    ACTIVE: UserSubscriptionInfo.Status
    AUTO_RENEW_FIELD_NUMBER: _ClassVar[int]
    EXPIRED: UserSubscriptionInfo.Status
    FIRST_SUBSCRIBED_FIELD_NUMBER: _ClassVar[int]
    GRACE_PERIOD: UserSubscriptionInfo.Status
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    LINKED_TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    LOCK_NEXT_SUBSCRIPTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    NEXT_SUBSCRIPTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    PAST_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    PAUSE_HOLD: UserSubscriptionInfo.Status
    PERIOD_END_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    PRO: UserSubscriptionInfo.Level
    REVOKED: UserSubscriptionInfo.Status
    SANDBOX_FIELD_NUMBER: _ClassVar[int]
    STANDARD: UserSubscriptionInfo.Level
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STORE_STATUS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN: UserSubscriptionInfo.Status
    acknowledged: bool
    auto_renew: bool
    first_subscribed: float
    history: _containers.RepeatedCompositeFieldContainer[UserSubscriptionInfo.HistoryEntry]
    last_updated: float
    linked_transaction_id: str
    lock_next_subscription_level: bool
    next_subscription_level: UserSubscriptionInfo.Level
    original_transaction_id: str
    past_user_ids: _containers.RepeatedScalarFieldContainer[str]
    period_end: float
    platform: Platform
    sandbox: bool
    status: UserSubscriptionInfo.Status
    store_status: str
    subscription_level: UserSubscriptionInfo.Level
    def __init__(self, subscription_level: _Optional[_Union[UserSubscriptionInfo.Level, str]] = ..., next_subscription_level: _Optional[_Union[UserSubscriptionInfo.Level, str]] = ..., lock_next_subscription_level: bool = ..., platform: _Optional[_Union[Platform, str]] = ..., original_transaction_id: _Optional[str] = ..., linked_transaction_id: _Optional[str] = ..., acknowledged: bool = ..., first_subscribed: _Optional[float] = ..., period_end: _Optional[float] = ..., status: _Optional[_Union[UserSubscriptionInfo.Status, str]] = ..., store_status: _Optional[str] = ..., auto_renew: bool = ..., sandbox: bool = ..., last_updated: _Optional[float] = ..., history: _Optional[_Iterable[_Union[UserSubscriptionInfo.HistoryEntry, _Mapping]]] = ..., past_user_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class UserVerificationAnalysis(_message.Message):
    __slots__ = ["artifacts_collected", "artifacts_consumed", "artifacts_in_inventory", "artifacts_status", "completion_time", "contracts_status", "eggs_of_prophecy", "excessive_consumes", "excessive_eop", "excessive_invalid_contracts", "excessive_inventory", "excessive_spend", "gold_earned", "gold_spent_crafting", "iap_status", "invalid_contracts", "legendary_artifacts_in_inventory", "legendary_artifacts_on_server", "missions_completed", "num_coop_memberships", "num_prestiges", "overall_status", "rare_artifacts_in_inventory", "rare_artifacts_on_server", "regular_iap_buyer", "regular_iap_cheater", "soul_eggs", "start_time", "unverified_iap", "valid_contracts", "verification_count", "verification_override", "verification_override_value", "verified", "verified_other_iap", "verified_piggy_breaks", "verified_pro_permit"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ARTIFACTS_COLLECTED_FIELD_NUMBER: _ClassVar[int]
    ARTIFACTS_CONSUMED_FIELD_NUMBER: _ClassVar[int]
    ARTIFACTS_IN_INVENTORY_FIELD_NUMBER: _ClassVar[int]
    ARTIFACTS_STATUS_FIELD_NUMBER: _ClassVar[int]
    COMPLETE: UserVerificationAnalysis.Status
    COMPLETION_TIME_FIELD_NUMBER: _ClassVar[int]
    CONTRACTS_STATUS_FIELD_NUMBER: _ClassVar[int]
    EGGS_OF_PROPHECY_FIELD_NUMBER: _ClassVar[int]
    EXCESSIVE_CONSUMES_FIELD_NUMBER: _ClassVar[int]
    EXCESSIVE_EOP_FIELD_NUMBER: _ClassVar[int]
    EXCESSIVE_INVALID_CONTRACTS_FIELD_NUMBER: _ClassVar[int]
    EXCESSIVE_INVENTORY_FIELD_NUMBER: _ClassVar[int]
    EXCESSIVE_SPEND_FIELD_NUMBER: _ClassVar[int]
    GOLD_EARNED_FIELD_NUMBER: _ClassVar[int]
    GOLD_SPENT_CRAFTING_FIELD_NUMBER: _ClassVar[int]
    IAP_STATUS_FIELD_NUMBER: _ClassVar[int]
    INVALID_CONTRACTS_FIELD_NUMBER: _ClassVar[int]
    LEGENDARY_ARTIFACTS_IN_INVENTORY_FIELD_NUMBER: _ClassVar[int]
    LEGENDARY_ARTIFACTS_ON_SERVER_FIELD_NUMBER: _ClassVar[int]
    MISSIONS_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    NUM_COOP_MEMBERSHIPS_FIELD_NUMBER: _ClassVar[int]
    NUM_PRESTIGES_FIELD_NUMBER: _ClassVar[int]
    OVERALL_STATUS_FIELD_NUMBER: _ClassVar[int]
    PROCESSING: UserVerificationAnalysis.Status
    RARE_ARTIFACTS_IN_INVENTORY_FIELD_NUMBER: _ClassVar[int]
    RARE_ARTIFACTS_ON_SERVER_FIELD_NUMBER: _ClassVar[int]
    REGULAR_IAP_BUYER_FIELD_NUMBER: _ClassVar[int]
    REGULAR_IAP_CHEATER_FIELD_NUMBER: _ClassVar[int]
    SOUL_EGGS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN: UserVerificationAnalysis.Status
    UNVERIFIED_IAP_FIELD_NUMBER: _ClassVar[int]
    VALID_CONTRACTS_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_COUNT_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_OVERRIDE_VALUE_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_OTHER_IAP_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_PIGGY_BREAKS_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_PRO_PERMIT_FIELD_NUMBER: _ClassVar[int]
    artifacts_collected: float
    artifacts_consumed: float
    artifacts_in_inventory: float
    artifacts_status: UserVerificationAnalysis.Status
    completion_time: float
    contracts_status: UserVerificationAnalysis.Status
    eggs_of_prophecy: int
    excessive_consumes: bool
    excessive_eop: bool
    excessive_invalid_contracts: bool
    excessive_inventory: bool
    excessive_spend: bool
    gold_earned: float
    gold_spent_crafting: float
    iap_status: UserVerificationAnalysis.Status
    invalid_contracts: _containers.RepeatedScalarFieldContainer[str]
    legendary_artifacts_in_inventory: int
    legendary_artifacts_on_server: int
    missions_completed: int
    num_coop_memberships: int
    num_prestiges: float
    overall_status: UserVerificationAnalysis.Status
    rare_artifacts_in_inventory: int
    rare_artifacts_on_server: int
    regular_iap_buyer: bool
    regular_iap_cheater: bool
    soul_eggs: float
    start_time: float
    unverified_iap: int
    valid_contracts: int
    verification_count: int
    verification_override: bool
    verification_override_value: bool
    verified: bool
    verified_other_iap: int
    verified_piggy_breaks: int
    verified_pro_permit: bool
    def __init__(self, overall_status: _Optional[_Union[UserVerificationAnalysis.Status, str]] = ..., start_time: _Optional[float] = ..., completion_time: _Optional[float] = ..., verification_count: _Optional[int] = ..., num_prestiges: _Optional[float] = ..., soul_eggs: _Optional[float] = ..., eggs_of_prophecy: _Optional[int] = ..., iap_status: _Optional[_Union[UserVerificationAnalysis.Status, str]] = ..., verified_pro_permit: bool = ..., verified_piggy_breaks: _Optional[int] = ..., verified_other_iap: _Optional[int] = ..., unverified_iap: _Optional[int] = ..., gold_earned: _Optional[float] = ..., regular_iap_buyer: bool = ..., regular_iap_cheater: bool = ..., artifacts_status: _Optional[_Union[UserVerificationAnalysis.Status, str]] = ..., missions_completed: _Optional[int] = ..., artifacts_collected: _Optional[float] = ..., artifacts_consumed: _Optional[float] = ..., artifacts_in_inventory: _Optional[float] = ..., rare_artifacts_in_inventory: _Optional[int] = ..., rare_artifacts_on_server: _Optional[int] = ..., legendary_artifacts_in_inventory: _Optional[int] = ..., legendary_artifacts_on_server: _Optional[int] = ..., gold_spent_crafting: _Optional[float] = ..., excessive_consumes: bool = ..., excessive_inventory: bool = ..., excessive_spend: bool = ..., contracts_status: _Optional[_Union[UserVerificationAnalysis.Status, str]] = ..., num_coop_memberships: _Optional[int] = ..., valid_contracts: _Optional[int] = ..., invalid_contracts: _Optional[_Iterable[str]] = ..., excessive_eop: bool = ..., excessive_invalid_contracts: bool = ..., verified: bool = ..., verification_override: bool = ..., verification_override_value: bool = ...) -> None: ...

class Vector3(_message.Message):
    __slots__ = ["x", "y", "z"]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...

class Vector4(_message.Message):
    __slots__ = ["w", "x", "y", "z"]
    W_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    w: float
    x: float
    y: float
    z: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ..., w: _Optional[float] = ...) -> None: ...

class VerifyPurchaseRequest(_message.Message):
    __slots__ = ["log", "original_transaction_id", "platform", "receipt", "rinfo", "sandbox", "sku", "transaction_id"]
    LOG_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    RECEIPT_FIELD_NUMBER: _ClassVar[int]
    RINFO_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_FIELD_NUMBER: _ClassVar[int]
    SKU_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    log: GenericAction
    original_transaction_id: str
    platform: str
    receipt: str
    rinfo: BasicRequestInfo
    sandbox: bool
    sku: str
    transaction_id: str
    def __init__(self, rinfo: _Optional[_Union[BasicRequestInfo, _Mapping]] = ..., sku: _Optional[str] = ..., transaction_id: _Optional[str] = ..., original_transaction_id: _Optional[str] = ..., receipt: _Optional[str] = ..., platform: _Optional[str] = ..., sandbox: bool = ..., log: _Optional[_Union[GenericAction, _Mapping]] = ...) -> None: ...

class VerifyPurchaseResponse(_message.Message):
    __slots__ = ["message", "verified"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_FIELD_NUMBER: _ClassVar[int]
    message: str
    verified: bool
    def __init__(self, verified: bool = ..., message: _Optional[str] = ...) -> None: ...

class Egg(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class FarmType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class GoalType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class RewardType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class UILocation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class UserType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class LeaderboardScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Platform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class DeviceFormFactor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class AdNetwork(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
