def convert(unit, input):
    switcher = {
        "yavodara": input*0.24,
        "angula": input*1.95,
        "bitahasti": input*22.86,
        "aratni": input*41.91,
        "hasta": input*45.72,
        "nrpahasta": input*55.88,
        "rajahasta": input*55.88,
        "vyama": input*182.88,
        //end of length units
        "karsa": input*12,
        "tola": input*12,
        "masa": input,
        "ratti": input*125,
        "gunga": input*125,
        "palam": input*48,
        "prasrti": input*96,
        "kudava": input*192,
        "manika": input*384,
        "prastha": input*768,
        "adhaka": input*3073,
        "drona": input*12228,
        "surpa": input*24576,
        "droni": input*49152,
        "vahi": input*49152,
        "khari": input*196608,
        "tula": input*4800,
        "bhara": input*96,
        //end of weight units
    }
    switcher.get(unit, "Unknown unit");
