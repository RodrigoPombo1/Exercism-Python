class Allergies:
    allergies_dict = {
        1: "eggs",
        2: "peanuts",
        4: "shellfish",
        8: "strawberries",
        16: "tomatoes",
        32: "chocolate",
        64: "pollen",
        128: "cats"
    }
    def __init__(self, score):
        self.score = score
        items = []
        
        for allergy_score, allergy_name in Allergies.allergies_dict.items():
            if allergy_score & self.score:
                items.append(allergy_name)
            
        self.items = items

    def allergic_to(self, item):
        if item in self.items:
            return True
        return False

    @property
    def lst(self):
        return self.items
