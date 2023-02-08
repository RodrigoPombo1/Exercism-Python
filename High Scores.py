class HighScores:
    def __init__(self, scores):
        self.scores = scores
        self.latest_res = scores[-1]
        if len(scores) > 3:
            personal_top_three_res = []
            aux = scores.copy()
            for i in range(3):
                personal_top_three_res.append(max(aux))
                aux.remove(max(aux))
        else:
            personal_top_three_res = sorted(scores)[::-1]
        self.personal_top_three_res = personal_top_three_res
        self.highest_to_lowest_res = sorted(scores)
        self.personal_best_res = max(scores)
    def latest(self):
        return self.latest_res
    def personal_top_three(self):
        return self.personal_top_three_res
    def highest_to_lowest(self):
        return self.highest_to_lowest_res
    def personal_best(self):
        return self.personal_best_res
