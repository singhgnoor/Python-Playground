from time import time, sleep


def match_Words(sen1, sen2):
    words1 = sen1.strip().split(" ")
    words2 = sen2.strip().split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            # print(f"Matching this '{word1}' with '{word2}'")
            if word1.lower() == word2.lower():
                score += 1
    return score


if __name__ == "__main__":
    sentences = ['this is good', 'this is me', 'gurnoor is a good boy',
                 'python is good', 'python is not python snake ']
    # print(match_Words("this is good", "python is good"))

    queary = input("Please enter quarie string\n")
    intime = time()
    score = [match_Words(queary, sentence) for sentence in sentences]
    # print(score)
    sort_Sent_sore = [sent_Score for sent_Score in sorted(
        zip(score, sentences), reverse=True) if sent_Score[0] != 0]
    # sleep(0.001)
    outtime = time()
    # print(sort_Sent_sore)
    print(f"{len(sort_Sent_sore)} results found in {outtime-intime}")
    for s, i in sort_Sent_sore:
        if s != 0:
            print(f"{i}")
