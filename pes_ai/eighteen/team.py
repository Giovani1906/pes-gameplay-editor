import io
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
    data: io.BytesIO, offset: int, length: int
) -> dict[str, float | int | bool | None]:
    vals = []
    data.seek(offset)
    for i in range(int(length / 4)):
        match i:
            # adjustGapDfLineAction
            # adjustSetplay
            # adjustSlideMoveSpeed
            # changeDefenceNumberFromSituation
            # dfAttackWidthForce
            # dfUserPositionAdjustEnable
            # isUseDashSituation
            # numericalRelationDefenceLine
            # offenceZposiAdjust
            # onPassCourse
            # returnControlSide
            # slide
            # slowDownFw
            # teamToGroupAdjustEnable
            # xposiRateCustom
            case 15 | 18 | 21 | 42 | 71 | 90 | 128 | 163 | 166 | 168 | 177 | 184 | 193 | 203 | 215:
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


def map_centeringGet(
    data: io.BytesIO, offset: int, length: int
) -> dict[str, int]:
    vals = []
    data.seek(offset)
    for i in range(int(length / 4)):
        vals += [conv_from_bytes(data.read(4))]

    with open("pes_ai/mappings/18/team/centeringGet.txt", "r") as f:
        return dict(zip(f.read().split("\n"), vals))


def map_defence(
    data: io.BytesIO, offset: int, length: int
) -> dict[str, float | int]:
    vals = []
    data.seek(offset)
    for i in range(int(length / 4)):
        vals += [conv_from_bytes(data.read(4))]

    with open("pes_ai/mappings/18/team/defence.txt", "r") as f:
        return dict(zip(f.read().split("\n"), vals))


def map_defenceCover(
    data: io.BytesIO, offset: int, length: int
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
    data: io.BytesIO, offset: int, length: int
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


def map_diagonalRun(
    data: io.BytesIO, offset: int, length: int
) -> dict[str, float | int]:
    vals = []
    data.seek(offset)
    for i in range(int(length / 4)):
        vals += [conv_from_bytes(data.read(4))]

    with open("pes_ai/mappings/18/team/diagonalRun.txt", "r") as f:
        return dict(zip(f.read().split("\n"), vals))


def map_lineBreak(
    data: io.BytesIO, offset: int, length: int
) -> dict[str, float | int]:
    vals = []
    data.seek(offset)
    for i in range(int(length / 4)):
        vals += [conv_from_bytes(data.read(4))]

    with open("pes_ai/mappings/18/team/lineBreak.txt", "r") as f:
        return dict(zip(f.read().split("\n"), vals))


def map_overlap(
    data: io.BytesIO, offset: int, length: int
) -> dict[str, float | int]:
    vals = []
    data.seek(offset)
    for i in range(int(length / 4)):
        vals += [conv_from_bytes(data.read(4))]

    with open("pes_ai/mappings/18/team/overlap.txt", "r") as f:
        return dict(zip(f.read().split("\n"), vals))


def map_pullAway(
    data: io.BytesIO, offset: int, length: int
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
    data: io.BytesIO, offset: int, length: int
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
    data: io.BytesIO, offset: int, length: int
) -> dict[str, float | int | bool | None]:
    vals = []
    data.seek(offset)
    for i in range(int(length / 4)):
        match i:
            # subConcept
            # padding
            # padding
            case 0 | 1 | 51:
                vals += [conv_from_bytes(data.read(4))]
            # subConcept_passRequest_all_off
            # subConcept_passRequest_off
            case 50:
                vals += list(unpack("2?", data.read(2)))
                data.seek(data.tell() + 2)
                vals += [None]*2
            case _:
                vals += [bool(unpack("<i", data.read(4))[0])]

    with open("pes_ai/mappings/18/team/subConcept.txt", "r") as f:
        return dict(zip(f.read().split("\n"), vals))


def map_support(
    data: io.BytesIO, offset: int, length: int
) -> dict[str, float | int]:
    vals = []
    data.seek(offset)
    for i in range(int(length / 4)):
        vals += [conv_from_bytes(data.read(4))]

    with open("pes_ai/mappings/18/team/support.txt", "r") as f:
        return dict(zip(f.read().split("\n"), vals))
