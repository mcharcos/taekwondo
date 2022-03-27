
TOPICS = ["Sogui Kisul", "Son Kisul Maki"]

TECHNIQUES = dict()
TECHNIQUES[0] = {"name": "Pionji Sogui", "type": "Sogui Kisul", "description": "description"}
TECHNIQUES[1] = {"name": "Moa Sogui", "type": "Sogui Kisul", "description": "description"}
TECHNIQUES[2] = {"name": "Ap Sogui", "type": "Sogui Kisul", "description": "description"}
TECHNIQUES[3] = {"name": "Ap Kubi Sogui", "type": "Sogui Kisul", "description": "description"}
TECHNIQUES[4] = {"name": "Chuchum Sogui", "type": "Sogui Kisul", "description": "description"}
TECHNIQUES[5] = {"name": "Bom Sogui", "type": "Sogui Kisul", "description": "description"}
TECHNIQUES[6] = {"name": "Tuit Kubi Sogui", "type": "Sogui Kisul", "description": "description"}
TECHNIQUES[7] = {"name": "Tuit Kua Sogui", "type": "Sogui Kisul", "description": "description"}
TECHNIQUES[8] = {"name": "Naranji Sogui", "type": "Sogui Kisul", "description": "description"}
TECHNIQUES[9] = {"name": "Uen Sogui", "type": "Sogui Kisul", "description": "description"}
TECHNIQUES[10] = {"name": "Orun Sogui", "type": "Sogui Kisul", "description": "description"}

TECHNIQUES[11] = {"name": "Are Maki", "type": "Son Kisul Maki", "description": "description"}
TECHNIQUES[12] = {"name": "Montong An Maki", "type": "Son Kisul Maki", "description": "description"}
TECHNIQUES[13] = {"name": "Montong Maki", "type": "Son Kisul Maki", "description": "description"}
TECHNIQUES[14] = {"name": "Olgul Maki", "type": "Son Kisul Maki", "description": "description"}
TECHNIQUES[15] = {"name": "Jansonnal Montong Bakat Maki", "type": "Son Kisul Maki", "description": "description"}
TECHNIQUES[16] = {"name": "Sonnal Montong Maki", "type": "Son Kisul Maki", "description": "description"}
TECHNIQUES[17] = {"name": "Montong Bakat Maki", "type": "Son Kisul Maki", "description": "description"}
TECHNIQUES[18] = {"name": "Olgul Bakat Maki", "type": "Son Kisul Maki", "description": "description"}
TECHNIQUES[19] = {"name": "GechioAre Maki", "type": "Son Kisul Maki", "description": "description"}
TECHNIQUES[20] = {"name": "Batangson Montong Maki", "type": "Son Kisul Maki", "description": "description"}
TECHNIQUES[21] = {"name": "Batangson Montong An Maki", "type": "Son Kisul Maki", "description": "description"}
TECHNIQUES[22] = {"name": "Sonnal Are Maki", "type": "Son Kisul Maki", "description": "description"}
TECHNIQUES[23] = {"name": "Goduro Batangson Montong An Maki", "type": "Son Kisul Maki", "description": "description"}
TECHNIQUES[24] = {"name": "Okoro Are Maki", "type": "Son Kisul Maki", "description": "description"}
TECHNIQUES[25] = {"name": "Jansonnal Montong Yop Maki", "type": "Son Kisul Maki", "description": "description"}
TECHNIQUES[26] = {"name": "Goduro Montong Maki", "type": "Son Kisul Maki", "description": "description"}
TECHNIQUES[27] = {"name": "Goduro Are Maki", "type": "Son Kisul Maki", "description": "description"}

BELT_EXAM = dict()
BELT_EXAM["black"] = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,1,8,19,20,21,22,23,24,25,26,27]


class TkwCards(object):

    def __init__(self, **kwargs):
        super(TkwCards, self).__init__(**kwargs)

    def get_belt_techniques(self, belt):
        blt = belt.lower()
        if blt not in BELT_EXAM: return dict()
        idx_list = TECHNIQUES.keys() if blt == "all" else BELT_EXAM[blt]
        result = dict()
        for id in idx_list:
            tec = TECHNIQUES[id]
            topic = tec["type"]
            if topic in result: result[topic].append(tec)
            else: result[topic] = [tec]
        return result

    def get_topic_techniques(self, belt, topic):
        belt_techniques = self.get_belt_techniques(belt)
        if topic not in belt_techniques: return []

        return belt_techniques[topic]