from io import BytesIO
from struct import unpack

from pes_ai.utils import conv_from_bytes

one_byte_bools = []


def map_avoid(data: BytesIO, offset: int, length: int) -> dict[str, float]:
    vals = []
    data.seek(offset)
    for i in range(int(length / 4)):
        vals += [unpack("<f", data.read(4))[0]]

    with open("pes_ai/mappings/18/player/avoid.txt", "r") as f:
        return dict(zip(f.read().split("\n"), vals))


def map_ballplayer(data: BytesIO, offset: int, length: int) -> dict[str, int]:
    data.seek(offset)
    with open("pes_ai/mappings/18/player/ballplayer.txt", "r") as f:
        return dict(zip(f.read().split("\n"), [unpack("<i", data.read(4))[0]]))


def map_ballplayerAnalyze(data: BytesIO, offset: int, length: int) -> dict[str, int]:
    data.seek(offset)
    with open("pes_ai/mappings/18/player/ballplayerAnalyze.txt", "r") as f:
        return dict(zip(f.read().split("\n"), [unpack("<i", data.read(4))[0]]))


def map_ballplayerClear(data: BytesIO, offset: int, length: int) -> dict[str, int]:
    data.seek(offset)
    with open("pes_ai/mappings/18/player/ballplayerClear.txt", "r") as f:
        return dict(zip(f.read().split("\n"), [unpack("<i", data.read(4))[0]]))


def map_ballplayerShoot(data: BytesIO, offset: int, length: int) -> dict[str, float]:
    vals = []
    data.seek(offset)
    for i in range(int(length / 4)):
        vals += [unpack("<f", data.read(4))[0]]

    with open("pes_ai/mappings/18/player/ballplayerShoot.txt", "r") as f:
        return dict(zip(f.read().split("\n"), vals))


def map_contact(data: BytesIO, offset: int, length: int) -> dict[str, float | bool]:
    vals = []
    data.seek(offset)
    for i in range(int(length / 4)):
        match i:
            # back_charge_forced_falldown
            case 0:
                vals += [bool(unpack("<i", data.read(4))[0])]
            case _:
                vals += [unpack("<f", data.read(4))[0]]

    with open("pes_ai/mappings/18/player/contact.txt", "r") as f:
        return dict(zip(f.read().split("\n"), vals))


def map_freekick(data: BytesIO, offset: int, length: int) -> dict[str, float | bool]:
    vals = []
    data.seek(offset)
    for i in range(int(length / 4)):
        match i:
            # longpassInplayUse
            case 0:
                vals += [bool(unpack("<i", data.read(4))[0])]
            case _:
                vals += [unpack("<f", data.read(4))[0]]

    with open("pes_ai/mappings/18/player/freekick.txt", "r") as f:
        return dict(zip(f.read().split("\n"), vals))


def map_goalKick(data: BytesIO, offset: int, length: int) -> dict[str, float]:
    vals = []
    data.seek(offset)
    for i in range(int(length / 4)):
        vals += [unpack("<f", data.read(4))[0]]

    with open("pes_ai/mappings/18/player/goalKick.txt", "r") as f:
        return dict(zip(f.read().split("\n"), vals))


def map_matchup(data: BytesIO, offset: int, length: int) -> dict[str, float | bool]:
    vals = []
    data.seek(offset)
    for i in range(int(length / 4)):
        match i:
            # delayAutoClose
            case 8:
                vals += [bool(unpack("<i", data.read(4))[0])]
            case _:
                vals += [unpack("<f", data.read(4))[0]]

    with open("pes_ai/mappings/18/player/matchup.txt", "r") as f:
        return dict(zip(f.read().split("\n"), vals))


def map_moveOnPass(data: BytesIO, offset: int, length: int) -> dict[str, float | int]:
    vals = []
    data.seek(offset)
    for i in range(int(length / 4)):
        vals += [conv_from_bytes(data.read(4))]

    with open("pes_ai/mappings/18/player/moveOnPass.txt", "r") as f:
        return dict(zip(f.read().split("\n"), vals))
