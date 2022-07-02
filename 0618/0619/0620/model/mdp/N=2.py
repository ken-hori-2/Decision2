from collections import deque
import random

def node(text):
    
    wordlist = text

    return wordlist

        
def make_model(text, order):
    model = {}
    wordlist = node(text)
    queue = deque([], order)
    queue.append("init")
    for markov_value in wordlist:
        if len(queue) < order:
            queue.append(markov_value)
            continue

        if queue[-1] == 2:
            markov_key = tuple(queue)
            if markov_key not in model:
                model[markov_key] = []
            
        markov_key = tuple(queue)
        model.setdefault(markov_key, []).append(markov_value)
        queue.append(markov_value)
    return model

def make_sentence(model, sentence_num=5, seed="init", max_words = 10):    
    
    key_candidates = [key for key in model if key[0] == seed]
    # print(f"init:{key_candidates}")
    
    markov_key = random.choice(key_candidates)
    queue = deque(list(markov_key), len(list(model.keys())[0]))
    # print(f"queue 0:{queue}")
    
    sentence = []
    for _ in range(max_words):
        markov_key = tuple(queue)
        next_state = random.choice(model[markov_key])
        # print(markov_key,     next_state)
        # print(f"model;{model[markov_key]},     next:{next_state}")
        # sentence += next_state
        sentence.append(next_state)
        queue.append(next_state)
        # print(f"queue {_+1}:{queue}")

        if next_state == 2:

                break

    return sentence

if __name__ == "__main__":
    print("\n########################\n")
    # text = [3, 1,0,1,0,0,1,1,0,2] # "適当なとても長い文章。"
    # text = [3,0,1,0,2]
    text = [0,0,1,0,0,1,0,1,1,0,0,0,2]
    order = 2
    model = make_model(text, order)
    # sentence = make_sentence(model)
    print(f"\nnode:{text}")

    print(f"\nmodel:{model}")
    sentence = make_sentence(model)
    print(f"\noutput:{sentence}")