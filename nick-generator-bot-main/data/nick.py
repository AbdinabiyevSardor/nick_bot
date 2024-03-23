text = "qwertyuiopasdfghjklzxcvbnm"
fonts = ["🅠🅦🅔🅡🅣🅨🅤🅘🅞🅟🅐🅢🅓🅕🅖🅗🅙🅚🅛🅩🅧🅒🅥🅑🅝🅜","🅀🅆🄴🅁🅃🅈🅄🄸🄾🄿🄰🅂🄳🄵🄶🄷🄹🄺🄻🅉🅇🄲🅅🄱🄽🄼","𝕢𝕨𝕖𝕣𝕥𝕪𝕦𝕚𝕠𝕡𝕒𝕤𝕕𝕗𝕘𝕙𝕛𝕜𝕝𝕫𝕩𝕔𝕧𝕓𝕟𝕞","ｑｗｅｒｔｙｕｉｏｐａｓｄｆｇｈｊｋｌｚｘｃｖｂｎｍ","qʷᵉʳᵗʸᵘⁱᵒᵖᵃˢᵈᶠᵍʰʲᵏˡᶻˣᶜᵛᵇⁿᵐ","qwₑᵣₜyᵤᵢₒₚₐₛdfgₕⱼₖₗzₓcᵥbₙₘ","🍳🔱𝓔🌱🍄🏋⛎🕴😀🅿🅰💲🐬🔩🐋♓🎷🎉👢💤❎🌜✌🅱🥄Ⓜ","♥q♥w♥e♥r♥t♥y♥u♥i♥o♥p♥a♥s♥d♥f♥g♥h♥j♥k♥l♥z♥x♥c♥v♥b♥n♥m♥","𝓺𝔀𝓮𝓻𝓽𝔂𝓾𝓲𝓸𝓹𝓪𝓼𝓭𝓯𝓰𝓱𝓳𝓴𝓵𝔃𝔁𝓬𝓿𝓫𝓷𝓶","𝔮𝔴𝔢𝔯𝔱𝔶𝔲𝔦𝔬𝔭𝔞𝔰𝔡𝔣𝔤𝔥𝔧𝔨𝔩𝔷𝔵𝔠𝔳𝔟𝔫𝔪"]
emoji = "💯👋💻🌄🎀🎈🎁⭕️❌🟠🟡"
import random

def nick_generator(name):
    result = []
    for font in fonts:
        my_name = name
        for i in range(len(text)):
            my_name = my_name.replace(text[i],font[i])
        e = random.choice(emoji)
        result.append(e+my_name+e)
    return result

