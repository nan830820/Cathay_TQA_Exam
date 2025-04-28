def correct_scores(wrong_scores):
    corrected = []
    for score in wrong_scores:
        if 0 <= score < 100:
            tens = score // 10
            ones = score % 10
            corrected_score = ones * 10 + tens
            corrected.append(corrected_score)
        else:
            corrected.append(score)
    return corrected

if __name__=="__main__":
    wrong_scores = [35, 46, 57, 91, 29]
    corrected_scores = correct_scores(wrong_scores)
    print(corrected_scores)
