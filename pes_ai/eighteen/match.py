from io import BytesIO
from struct import unpack

from pes_ai.utils import conv_from_bytes

one_byte_bools = []


def map_cursor(data: BytesIO, offset: int, length: int) -> dict[str, float]:
    vals = []
    data.seek(offset)
    for i in range(int(length / 4)):
        vals += [unpack("<f", data.read(4))[0]]

    with open("pes_ai/mappings/18/match/cursor.txt", "r") as f:
        return dict(zip(f.read().split("\n"), vals))


def map_injury(data: BytesIO, offset: int, length: int) -> dict[str, int]:
    vals = []
    data.seek(offset)
    for i in range(int(length / 4)):
        vals += [unpack("<i", data.read(4))[0]]

    with open("pes_ai/mappings/18/match/injury.txt", "r") as f:
        return dict(zip(f.read().split("\n"), vals))


def map_inplayDemo(
    data: BytesIO, offset: int, length: int
) -> dict[str, float | int | bool | None]:
    vals = []
    data.seek(offset)
    for i in range(int(length / 4)):
        match i:
            # isHard
            # onoff
            case 4:
                vals += list(unpack("2?", data.read(2)))
                data.seek(data.tell() + 2)
                vals += [None] * 2
            case _:
                vals += [conv_from_bytes(data.read(4))]

    with open("pes_ai/mappings/18/match/inplayDemo.txt", "r") as f:
        return dict(zip(f.read().split("\n"), vals))


def map_setplayGuideCommon(
    data: BytesIO, offset: int, length: int
) -> dict[str, float | int | bool]:
    vals = []
    data.seek(offset)
    for i in range(int(length / 4)):
        match i:
            # freekickDebug
            case 0:
                vals += [bool(unpack("<i", data.read(4))[0])]
            case _:
                vals += [conv_from_bytes(data.read(4))]

    with open("pes_ai/mappings/18/match/setplayGuideCommon.txt", "r") as f:
        return dict(zip(f.read().split("\n"), vals))
