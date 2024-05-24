def get_coordinate(record):
    teasure, coordinate=record
    return coordinate

def convert_coordinate(coordinate):
    num, letra=coordinate
    return num, letra


def create_record(azara_record, rui_record):
    tesoro, coordenadaA=azara_record
    ubicación, coordenadaR, cuadrante=rui_record
    NUM,LETRA=coordenadaA
    conjunto= NUM,LETRA
    if conjunto==coordenadaR:
        return tesoro, coordenadaA, ubicación, coordenadaR, cuadrante
    else:
        return "not a match"   
