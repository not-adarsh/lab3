import random
array = ["I", "am", "Studying", "in", "BU"]
words = []
for i in range(1500):
    word = random.choice(array)
    words.append(word)
sample_space = []
for i in range(len(words)-1):
    if(words[i]=="BU"):
        sample_space.append(words[i+1])
occurance = {}
for word in sample_space:
    if(not(word in occurance.keys())):
        occurance[word]=1
        continue
    occurance[word]+=1 
probability = {}
for word in array:
    probability[word]=occurance[word]/len(sample_space)
print("Question 1")
print(probability)

num_tosses = 4
num_trials = 10000000

counts = [0] * (num_tosses + 1)

for _ in range(num_trials):
    heads = sum(random.choice([0, 1]) for _ in range(num_tosses))
    counts[heads] += 1

probabilities = [count / num_trials for count in counts]

print("Question 2")
for k in range(num_tosses + 1):
    print(f"P(X = {k}) = {probabilities[k]:.4f}")







