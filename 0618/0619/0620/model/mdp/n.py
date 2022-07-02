from collections import deque
import random

def node(text):
    
    wordlist = text

    return wordlist

        
def make_model(text, order):
    model = {}
    wordlist = node(text)
    queue = deque([], order)
    # queue.append("[init]")
    for markov_value in wordlist:
        if len(queue) < order:
            queue.append(markov_value)
            continue

        if queue[-1] == 2:
            markov_key = tuple(queue)
            if markov_key not in model:
                model[markov_key] = []
            # model.setdefault(markov_key, []) # .append("[init]")
            # queue.append("[init]")
        markov_key = tuple(queue)
        model.setdefault(markov_key, []).append(markov_value)
        queue.append(markov_value)
    return model

def make_sentence(model, sentence_num=5, seed=3, max_words = 100):    
    sentence_count = 0

    # key_candidates = [key for key in model if key[0] == seed]
    key_candidates = [key for key in model if key[0] == seed]
    print(f"key:{key_candidates}")
    # if not key_candidates:
    #     print("Not find Keyword")
    #     return
    markov_key = random.choice(key_candidates)
    queue = deque(list(markov_key), len(list(model.keys())[0]))
    print(f"queue 0:{queue}")
    # sentence = "-".join(markov_key)
    # sentence = '-'.join([str(n) for n in markov_key])
    sentence = []
    for _ in range(max_words):
        markov_key = tuple(queue)
        next_word = random.choice(model[markov_key])
        print(markov_key,     next_word)
        # print(f"model;{model[markov_key]},     next:{next_word}")
        # sentence += next_word
        sentence.append(next_word)
        queue.append(next_word)
        print(f"queue {_+1}:{queue}")

        if next_word == 2:
            # sentence_count += 1
            # if sentence_count == sentence_num:
                break
    return sentence

if __name__ == "__main__":
    text = [3, 1,0,1,0,0,1,1,0,2] # "適当なとても長い文章。"
    order = 2
    model = make_model(text, order)
    # sentence = make_sentence(model)
    print(text)

    print(model)
    sentence = make_sentence(model)
    print(sentence)