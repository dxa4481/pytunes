import math
def c(harmonic):
    return math.pow(2, harmonic) * 16.35
def cSharp(harmonic):
    return math.pow(2, harmonic) * 17.32
def dFlat(harmonic):
    return math.pow(2, harmonic) * 17.32
def d(harmonic):
    return math.pow(2, harmonic) * 18.32
def dSharp(harmonic):
    return math.pow(2, harmonic) * 19.45
def eFlat(harmonic):
    return math.pow(2, harmonic) * 19.45
def e(harmonic):
    return math.pow(2, harmonic) * 20.60
def f(harmonic):
    return math.pow(2, harmonic) * 21.83
def fSharp(harmonic):
    return math.pow(2, harmonic) * 23.12
def gFlat(harmonic):
    return math.pow(2, harmonic) * 23.12
def g(harmonic):
    return math.pow(2, harmonic) * 24.50
def gSharp(harmonic):
    return math.pow(2, harmonic) * 25.96
def aFlat(harmonic):
    return math.pow(2, harmonic) * 25.96 / 2
def a(harmonic):
    return math.pow(2, harmonic) * 27.50 / 2
def aSharp(harmonic):
    return math.pow(2, harmonic) * 29.14 / 2
def bFlat(harmonic):
    return math.pow(2, harmonic) * 29.14 / 2
def b(harmonic):
    return math.pow(2, harmonic) * 30.87 / 2
def cMajor(note, harmonic, pentatonic=False):
    cMajor = []
    cMajor.append(c(0))
    cMajor.append(d(0))
    cMajor.append(e(0))
    cMajor.append(f(0))
    cMajor.append(g(0))
    cMajor.append(a(1))
    cMajor.append(b(1))
    if (pentatonic):
        return [cMajor[0], cMajor[1], cMajor[2], cMajor[4], cMajor[5]][note]*math.pow(2, harmonic)
    return cMajor[note]*math.pow(2, harmonic)
def dMajor(note, harmonic, pentatonic=False):
    dMajor = []
    dMajor.append(d(0))
    dMajor.append(e(0))
    dMajor.append(fSharp(0))
    dMajor.append(g(0))
    dMajor.append(a(1))
    dMajor.append(b(1))
    dMajor.append(cSharp(1))
    if (pentatonic):
        return [dMajor[0], dMajor[1], dMajor[2], dMajor[4], dMajor[5]][note]*math.pow(2, harmonic)
    return dMajor[note]*math.pow(2, harmonic)
def eMajor(note, harmonic, pentatonic=False):
    eMajor = []
    eMajor.append(e(0))
    eMajor.append(fSharp(0))
    eMajor.append(gSharp(0))
    eMajor.append(a(1))
    eMajor.append(b(1))
    eMajor.append(cSharp(1))
    eMajor.append(dSharp(1))
    if (pentatonic):
        return [eMajor[0], eMajor[1], eMajor[2], eMajor[4], eMajor[5]][note]*math.pow(2, harmonic)
    return eMajor[note]*math.pow(2, harmonic)
def fMajor(note, harmonic, pentatonic=False):
    fMajor = []
    fMajor.append(f(0))
    fMajor.append(g(0))
    fMajor.append(a(1))
    fMajor.append(bFlat(1))
    fMajor.append(c(1))
    fMajor.append(d(1))
    fMajor.append(e(1))
    if (pentatonic):
        return [fMajor[0], fMajor[1], fMajor[2], fMajor[4], fMajor[5]][note]*math.pow(2, harmonic)
    return fMajor[note]*math.pow(2, harmonic)
def gMajor(note, harmonic, pentatonic=False):
    gMajor = []
    gMajor.append(g(0))
    gMajor.append(a(1))
    gMajor.append(b(1))
    gMajor.append(c(1))
    gMajor.append(d(1))
    gMajor.append(e(1))
    gMajor.append(fSharp(1))
    if (pentatonic):
        return [gMajor[0], gMajor[1], gMajor[2], gMajor[4], gMajor[5]][note]*math.pow(2, harmonic)
    return gMajor[note]*math.pow(2, harmonic)
def aMajor(note, harmonic, pentatonic=False):
    aMajor = []
    aMajor.append(a(0))
    aMajor.append(b(0))
    aMajor.append(cSharp(0))
    aMajor.append(d(0))
    aMajor.append(e(0))
    aMajor.append(fSharp(0))
    aMajor.append(gSharp(0))
    if (pentatonic):
        return [aMajor[0], aMajor[1], aMajor[2], aMajor[4], aMajor[5]][note]*math.pow(2, harmonic)
    return aMajor[note]*math.pow(2, harmonic)
def bMajor(note, harmonic, pentatonic=False):
    bMajor = []
    bMajor.append(b(0))
    bMajor.append(cSharp(0))
    bMajor.append(dSharp(0))
    bMajor.append(e(0))
    bMajor.append(fSharp(0))
    bMajor.append(gSharp(0))
    bMajor.append(aSharp(1))
    if (pentatonic):
        return [bMajor[0], bMajor[1], bMajor[2], bMajor[4], bMajor[5]][note]*math.pow(2, harmonic)
    return bMajor[note]*math.pow(2, harmonic)
def cSharpMajor(note, harmonic, pentatonic=False):
    cSharpMajor = []
    cSharpMajor.append(cSharp(0))
    cSharpMajor.append(dSharp(0))
    cSharpMajor.append(f(0))
    cSharpMajor.append(fSharp(0))
    cSharpMajor.append(gSharp(0))
    cSharpMajor.append(aSharp(1))
    cSharpMajor.append(c(1))
    if (pentatonic):
        return [cSharpMajor[0], cSharpMajor[1], cSharpMajor[2], cSharpMajor[4], cSharpMajor[5]][note]*math.pow(2, harmonic)
    return cSharpMajor[note]*math.pow(2, harmonic)
def dFlatMajor(note, harmonic, pentatonic=False):
    dFlatMajor = []
    dFlatMajor.append(dFlat(0))
    dFlatMajor.append(eFlat(0))
    dFlatMajor.append(f(0))
    dFlatMajor.append(gFlat(0))
    dFlatMajor.append(aFlat(1))
    dFlatMajor.append(bFlat(1))
    dFlatMajor.append(c(1))
    if (pentatonic):
        return [dFlatMajor[0], dFlatMajor[1], dFlatMajor[2], dFlatMajor[4], dFlatMajor[5]][note]*math.pow(2, harmonic)
    return dFlatMajor[note]*math.pow(2, harmonic)
def eFlatMajor(note, harmonic, pentatonic=False):
    eFlatMajor = []
    eFlatMajor.append(eFlat(0))
    eFlatMajor.append(f(0))
    eFlatMajor.append(g(0))
    eFlatMajor.append(aFlat(1))
    eFlatMajor.append(bFlat(1))
    eFlatMajor.append(c(1))
    eFlatMajor.append(d(1))
    if (pentatonic):
        return [eFlatMajor[0], eFlatMajor[1], eFlatMajor[2], eFlatMajor[4], eFlatMajor[5]][note]*math.pow(2, harmonic)
    return eFlatMajor[note]*math.pow(2, harmonic)
def fSharpMajor(note, harmonic, pentatonic=False):
    fSharpMajor = []
    fSharpMajor.append(fSharp(0))
    fSharpMajor.append(gSharp(0))
    fSharpMajor.append(aSharp(1))
    fSharpMajor.append(c(1))
    fSharpMajor.append(cSharp(1))
    fSharpMajor.append(dSharp(1))
    fSharpMajor.append(f(1))
    if (pentatonic):
        return [fSharpMajor[0], fSharpMajor[1], fSharpMajor[2], fSharpMajor[4], fSharpMajor[5]][note]*math.pow(2, harmonic)
    return fSharpMajor[note]*math.pow(2, harmonic)
def gFlatMajor(note, harmonic, pentatonic=False):
    gFlatMajor = []
    gFlatMajor.append(gFlat(0))
    gFlatMajor.append(aFlat(1))
    gFlatMajor.append(bFlat(1))
    gFlatMajor.append(b(1))
    gFlatMajor.append(dFlat(1))
    gFlatMajor.append(eFlat(1))
    gFlatMajor.append(f(1))
    if (pentatonic):
        return [gFlatMajor[0], gFlatMajor[1], gFlatMajor[2], gFlatMajor[4], gFlatMajor[5]][note]*math.pow(2, harmonic)
    return gFlatMajor[note]*math.pow(2, harmonic)
def aFlatMajor(note, harmonic, pentatonic=False):
    aFlatMajor = []
    aFlatMajor.append(aFlat(0))
    aFlatMajor.append(bFlat(0))
    aFlatMajor.append(c(0))
    aFlatMajor.append(dFlat(0))
    aFlatMajor.append(eFlat(0))
    aFlatMajor.append(f(0))
    aFlatMajor.append(g(0))
    if (pentatonic):
        return [aFlatMajor[0], aFlatMajor[1], aFlatMajor[2], aFlatMajor[4], aFlatMajor[5]][note]*math.pow(2, harmonic)
    return aFlatMajor[note]*math.pow(2, harmonic)
def bFlatMajor(note, harmonic, pentatonic=False):
    bFlatMajor = []
    bFlatMajor.append(bFlat(0))
    bFlatMajor.append(c(0))
    bFlatMajor.append(d(0))
    bFlatMajor.append(eFlat(0))
    bFlatMajor.append(f(0))
    bFlatMajor.append(g(0))
    bFlatMajor.append(a(1))
    if (pentatonic):
        return [bFlatMajor[0], bFlatMajor[1], bFlatMajor[2], bFlatMajor[4], bFlatMajor[5]][note]*math.pow(2, harmonic)
    return bFlatMajor[note]*math.pow(2, harmonic)
def chromaticScale(note, harmonic):
    chrom = []
    chrom.append(c(0))
    chrom.append(cSharp(0))
    chrom.append(d(0))
    chrom.append(dSharp(0))
    chrom.append(e(0))
    chrom.append(f(0))
    chrom.append(fSharp(0))
    chrom.append(g(0))
    chrom.append(gSharp(0))
    chrom.append(a(0))
    chrom.append(aSharp(0))
    chrom.append(b(0))
    return chrom[note]*math.pow(2, harmonic)
    
