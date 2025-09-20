# apps/nickgen/wordbank.py
import random

ADJ_KO = {
    'cute': ['말랑한','초록빛','반짝이는','포근한','뚝딱','쑥쑥','총총','상큼한','빠른','가벼운'],
    'tech': ['커널급','바이너리','네온','양자','벡터','아카이브','캐시드','펌웨어','루트','그래프'],
    'sage': ['도연한','순후한','정직한','담대한','온유한','청렴한','성실한','자비로운','지혜로운','자명한'],
    'myth': ['천룡','백호','현무','주작','풍운','낙뢰','강철','곤륜','태산','북두'],
    'city': ['시티','메트로','나이트','네온','브릿지','하버','라인','스카이','어번','브릭']
}

NOUN_KO = {
    'cute': ['토끼','너구리','두부','젤리','코딩씨','모코모','도토리','반디','꼬마','몽글'],
    'tech': ['코더','레지스터','버퍼','포인터','커밋','패킷','엔진','소켓','파서','노드'],
    'sage': ['학인','도인','청자','서생','지기','문인','선비','풍류','경학','강호'],
    'myth': ['영웅','장수','도깨비','호걸','수호','비룡','선풍','천리','백검','운검'],
    'city': ['러너','워커','드리머','메이커','라이더','서퍼','챔프','리거','크루','플로우']
}

ADJ_EN = {
    'cute': ['Fluffy','Minty','Sunny','Bubbly','Tiny','Mellow','Zippy','Spry','Cheery','Brisk'],
    'tech': ['Quantum','Vector','Neon','Binary','Kernel','Socket','Matrix','Turbo','Cached','Atomic'],
    'sage': ['Earnest','Noble','Sincere','Just','Humble','Graceful','Prudent','Sage','Bright','Kind'],
    'myth': ['Dragon','Tiger','Phoenix','Vermilion','Thunder','Aegis','Frost','Storm','Mythic','Rune'],
    'city': ['Urban','Metro','Harbor','Skyline','Bridge','Night','Brick','Subway','Station','Neon']
}

NOUN_EN = {
    'cute': ['Bunny','Puff','Jelly','Bean','Dobby','Mochi','Dandelion','Firefly','Buddy','Nori'],
    'tech': ['Coder','Pointer','Packet','Engine','Router','Vector','Kernel','Commit','Node','Parser'],
    'sage': ['Scholar','Monk','Scribe','Seeker','Sage','Gentle','Virtue','Civitas','Honest','Grace'],
    'myth': ['Hero','Blade','Guardian','Rider','Wolf','Aquila','Levi','Hydra','Aegis','Rex'],
    'city': ['Runner','Maker','Rider','Dreamer','Walker','Flo','Crew','Chaser','Pilot','Drifter']
}

TAIL_NUM = [7, 77, 101, 2049, 314, 404, 808, 9009]

BAN = {'욕설','금칙어','admin','root'}

SEP = ['', '', '', '-', '_']

def pick(style, lang):
    style = style if style in ADJ_KO else 'tech'
    lang = lang if lang in ('ko','en','mix') else 'mix'
    if lang == 'ko':
        adj = random.choice(ADJ_KO[style])
        nn = random.choice(NOUN_KO[style])
    elif lang == 'en':
        adj = random.choice(ADJ_EN[style])
        nn = random.choice(NOUN_EN[style])
    else:
        if random.random() < 0.5:
            adj = random.choice(ADJ_KO[style]); nn = random.choice(NOUN_EN[style])
        else:
            adj = random.choice(ADJ_EN[style]); nn = random.choice(NOUN_KO[style])
    return adj, nn

def compose(adj, nn, seed='', sep=None, tail_num=False):
    sep = random.choice(SEP) if sep is None else sep
    base = f"{adj}{sep}{nn}"
    if seed:
        if random.random() < 0.5:
            base = f"{seed}{sep}{base}"
        else:
            base = f"{base}{sep}{seed}"
    if tail_num and random.random() < 0.6:
        base = f"{base}{random.choice(TAIL_NUM)}"
    return base
