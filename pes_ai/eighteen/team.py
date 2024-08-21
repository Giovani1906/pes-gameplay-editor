from io import BytesIO
from struct import unpack

from pes_ai.utils import conv_from_bytes

one_byte_bools = [
    # basePosition
    "defenceFormationTest1",
    "defenceFormationTest2",
    "dfAdjustZ",
    "dfCoverAdjustX",
    "dfCoverEnable",
    "dfForceAverageZ",
    # pullAway
    "eyeOff",
    "lastLine",
    "lastLineEnemy",
    "pullAway",
    # spaceRun
    "createPassCourse",
    "defenceGap",
    "inOut",
    "roundTest",
    # subConcept
    "subConcept_passRequest_all_off",
    "subConcept_passRequest_off",
]


def map_basePosition(
    data: BytesIO, offset: int, length: int
) -> dict[str, float | int | bool | None]:
    vals = []
    data.seek(offset)
    for i in range(int(length / 4)):
        match i:
            case (
                15  # adjustGapDfLineAction
                | 18  # adjustSetplay
                | 21  # adjustSlideMoveSpeed
                | 42  # changeDefenceNumberFromSituation
                | 71  # dfAttackWidthForce
                | 90  # dfUserPositionAdjustEnable
                | 128  # isUseDashSituation
                | 163  # numericalRelationDefenceLine
                | 166  # offenceZposiAdjust
                | 168  # onPassCourse
                | 177  # returnControlSide
                | 184  # slide
                | 193  # slowDownFw
                | 203  # teamToGroupAdjustEnable
                | 215  # xposiRateCustom
            ):
                vals += [bool(unpack("<i", data.read(4))[0])]
            # defenceFormationTest1
            # defenceFormationTest2
            # dfAdjustZ
            # dfCoverAdjustX
            # dfCoverEnable
            # dfForceAverageZ
            case 64 | 75:
                vals += list(unpack("3?", data.read(3)))
                data.seek(data.tell() + 1)
                vals += [None]
            case _:
                vals += [conv_from_bytes(data.read(4))]

    with open("pes_ai/mappings/18/team/basePosition.txt", "r") as f:
        return dict(zip(f.read().split("\n"), vals))


def map_centeringGet(data: BytesIO, offset: int, length: int) -> dict[str, int]:
    vals = []
    data.seek(offset)
    for i in range(int(length / 4)):
        vals += [conv_from_bytes(data.read(4))]

    with open("pes_ai/mappings/18/team/centeringGet.txt", "r") as f:
        return dict(zip(f.read().split("\n"), vals))


def map_defence(data: BytesIO, offset: int, length: int) -> dict[str, float | int]:
    vals = []
    data.seek(offset)
    for i in range(int(length / 4)):
        vals += [conv_from_bytes(data.read(4))]

    with open("pes_ai/mappings/18/team/defence.txt", "r") as f:
        return dict(zip(f.read().split("\n"), vals))


def map_defenceCover(
    data: BytesIO, offset: int, length: int
) -> dict[str, float | int | bool]:
    vals = []
    data.seek(offset)
    for i in range(int(length / 4)):
        match i:
            # isNearPlayerAssign
            case 29:
                vals += [bool(unpack("<i", data.read(4))[0])]
            case _:
                vals += [conv_from_bytes(data.read(4))]

    with open("pes_ai/mappings/18/team/defenceCover.txt", "r") as f:
        return dict(zip(f.read().split("\n"), vals))


def map_defenceMark(
    data: BytesIO, offset: int, length: int
) -> dict[str, float | int | bool]:
    vals = []
    data.seek(offset)
    for i in range(int(length / 4)):
        match i:
            # useCoverMoveSpeed
            case 69:
                vals += [bool(unpack("<i", data.read(4))[0])]
            case _:
                vals += [conv_from_bytes(data.read(4))]

    with open("pes_ai/mappings/18/team/defenceMark.txt", "r") as f:
        return dict(zip(f.read().split("\n"), vals))


def map_diagonalRun(data: BytesIO, offset: int, length: int) -> dict[str, float | int]:
    vals = []
    data.seek(offset)
    for i in range(int(length / 4)):
        vals += [conv_from_bytes(data.read(4))]

    with open("pes_ai/mappings/18/team/diagonalRun.txt", "r") as f:
        return dict(zip(f.read().split("\n"), vals))


def map_lineBreak(data: BytesIO, offset: int, length: int) -> dict[str, float | int]:
    vals = []
    data.seek(offset)
    for i in range(int(length / 4)):
        vals += [conv_from_bytes(data.read(4))]

    with open("pes_ai/mappings/18/team/lineBreak.txt", "r") as f:
        return dict(zip(f.read().split("\n"), vals))


def map_overlap(data: BytesIO, offset: int, length: int) -> dict[str, float | int]:
    vals = []
    data.seek(offset)
    for i in range(int(length / 4)):
        vals += [conv_from_bytes(data.read(4))]

    with open("pes_ai/mappings/18/team/overlap.txt", "r") as f:
        return dict(zip(f.read().split("\n"), vals))


def map_pullAway(
    data: BytesIO, offset: int, length: int
) -> dict[str, int | float | bool | None]:
    vals = []
    data.seek(offset)
    for i in range(int(length / 4)):
        match i:
            # eyeOff
            # lastLine
            # lastLineEnemy
            # pullAway
            case 10:
                vals += list(unpack("4?", data.read(4)))
            # pullAwaySide
            case 11:
                vals += [bool(unpack("<i", data.read(4))[0])]
            case _:
                vals += [conv_from_bytes(data.read(4))]

    with open("pes_ai/mappings/18/team/pullAway.txt", "r") as f:
        return dict(zip(f.read().split("\n"), vals))


def map_spaceRun(
    data: BytesIO, offset: int, length: int
) -> dict[str, int | float | bool]:
    vals = []
    data.seek(offset)
    for i in range(int(length / 4)):
        match i:
            # backwardCurve
            # shortConceptTest
            # vitalSupportPrior
            case 4 | 60 | 63:
                vals += [bool(unpack("<i", data.read(4))[0])]
            # createPassCourse
            # defenceGap
            # inOut
            # roundTest
            case 57:
                vals += list(unpack("4?", data.read(4)))
            case _:
                vals += [conv_from_bytes(data.read(4))]

    with open("pes_ai/mappings/18/team/spaceRun.txt", "r") as f:
        return dict(zip(f.read().split("\n"), vals))


def map_subConcept(
    data: BytesIO, offset: int, length: int
) -> dict[str, float | int | bool | None]:
    vals = []
    data.seek(offset + 16)
    for i in range(int(length / 4)):
        match i:
            case 46:
                vals += list(unpack("2?", data.read(2)))
            case _:
                vals += [bool(unpack("<i", data.read(4))[0])]

    with open("pes_ai/mappings/18/team/subConcept.txt", "r") as f:
        return dict(zip(f.read().split("\n"), vals))


def map_support(data: BytesIO, offset: int, length: int) -> dict[str, float | int]:
    vals = []
    data.seek(offset)
    for i in range(int(length / 4)):
        vals += [conv_from_bytes(data.read(4))]

    with open("pes_ai/mappings/18/team/support.txt", "r") as f:
        return dict(zip(f.read().split("\n"), vals))
