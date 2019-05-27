from src.services.dtos import MIDto
from src.entities.mi import MI


def mi_to_dto(mi: MI):
    if mi is MI.NULL:
        return MIDto.NULL

    return MIDto(
        mid1=mi
    )
