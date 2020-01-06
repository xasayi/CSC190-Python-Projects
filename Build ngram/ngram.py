import utilities

def parse_story(file_name):
  givenfile = open(file_name, 'r')
  content = givenfile.read()
  content = content.lower()
  token_list = []
  element = ''
  for i in range(len(content)):
    if not(content[i] in utilities.BAD_CHARS) and not (content[i] in utilities.VALID_PUNCTUATION) and content[i] != '\n' and content[i] != ' ':
      element += content[i]
    if content[i] in [' ', '\n', '\t', '']:
      if element:
        token_list.append(element)
      element =''
    elif content[i] in utilities.VALID_PUNCTUATION + utilities.END_OF_SENTENCE_PUNCTUATION:
      if element:
        token_list.append(element)
      element =''
      token_list.append(content[i])
  return token_list

def get_prob_from_count(counts):
  total_value = 0
  output = []
  for i in range(len(counts)):
    total_value += counts[i]
  for i in range(len(counts)):
    output.append(counts[i]/total_value)

  return output


def build_ngram_counts(words, n):
  holder_set = {}
  word_list = []
  word_tup = ()
  count = []
  following_words = []
  value_words = []

  difference = len(words)%n
  if len(words)%2==0:
    size = len(words)-difference-n
  else:
    size = len(words)-difference-n+1

  #get the tuple list and following words list
  for i in range(size):
    word_tup = tuple(words[i:i+n])
    word_list.append(word_tup)
    following_words.append([words[i+n]])

    for j in range(len(word_list)-2):
      if word_list[j] == word_tup:
        following_words[j].append(words[i+n])
        following_words.pop()
        word_list.pop()

  for o in range(len(following_words)):
    num_list = []
    single_value = []
    i = 0
    for p in following_words[o]:
      if not(p in single_value):
        number = following_words[o].count(p)
        single_value.append(p)
        num_list.append(number)
    count.append(num_list)
    value_words.append(single_value)

  final_value = [[]]*len(count)

  for i in range(len(count)):
    final_value[i]=[value_words[i], count[i]]

  for j in range(len(word_list)):
    holder_set[word_list[j]] = final_value[j]
  return holder_set

def prune_ngram_counts(counts, prune_len):
  value_list = list(counts.values())
  key_list = list(counts.keys())
  tie = []
  for i in range(len(value_list)):
    tie.append([])
    for j in range(len(value_list[i][1])):
      tie[i].append(1)
  for i in range(len(value_list)):
    for j in range(1, len(value_list[i][1])):
      min = value_list[i][1][j-1]
      if min > value_list[i][1][j]:
        min = value_list[i][1][j]
      elif min == value_list[i][1][j]:
        tie[i][j-1] +=1
    index_num = value_list[i][1].index (min)
    if len(value_list[i][1]) > prune_len and tie[i][index_num] ==1:
      value_list[i][0].pop(index_num)
      value_list[i][1].pop(index_num)
  output = {}
  for i in range(len(value_list)):
    output[key_list[i]] = value_list[i]
  return output

def probify_ngram_counts(counts):
  value_list = list(counts.values())
  key_list = list(counts.keys())
  output = {}
  for i in range(len(key_list)):
    output[key_list[i]] = get_prob_from_count(value_list[i][1])
  return output

def build_ngram_model(words, n):
  dict = build_ngram_counts(words, n)
  value_list = list(dict.values())
  key_list = list(dict.keys())
  output = {}

  for i in range(len(key_list)):
    value_list[i].append(get_prob_from_count(value_list[i][1]))
    value_list[i].pop(1)
    output[key_list[i]] = value_list[i]

  #sorting algrithm
  for k, v in output.items():
    if len(v[0])>1:
      for j in range(len(v[0])-1, 0, -1):
        while j>0 and j <len(v[0]) and v[1][j-1] <= v[1][j] :
          v[1][j-1], v[1][j] = v[1][j], v[1][j-1]
          v[0][j-1], v[0][j] = v[0][j], v[0][j-1]
          j+=1

  #limit to 15 following words
  for k, v in output.items():
    if len(v[0])>15:
      v[0]=(v[0][:15])
      v[1]= v[1][:15]
  return output

def gen_bot_list(ngram_model, seed, num_token = 0):
  output = []
  seed_list = list(seed)
  key_list = list(ngram_model.keys())
  if not(seed in key_list) and num_token == 0:
     return output
  elif not(seed in key_list):
    if num_token >= len(seed_list):
      output.extend(seed_list)
      return output
    else:
      output.extend(seed_list[:num_token])
      return output
  elif seed in key_list:
    output.extend(seed_list)
    while seed in ngram_model and len(output)<num_token:
      output.append(utilities.gen_next_token(seed, ngram_model))
      seed_list.pop(0)
      seed_list.append(output[-1])
      seed = tuple(seed_list)
    return output

def gen_bot_text(token_list, bad_author):
  string = ''
  if bad_author:
    for j in token_list:
      string = j + ' '
    return string
  else:
    for i in range(len(token_list)):
      if i == 0:
        string1 = token_list[i]
        string2 = string1.capitalize()
        string += string2 + ' '
      elif (token_list[i] in utilities.VALID_PUNCTUATION):
        string = string[:-1]
        string += token_list[i] + ' '
        if token_list[i] in utilities.END_OF_SENTENCE_PUNCTUATION and i!=len(token_list)-1:
          token_list[i+1] = token_list[i+1].capitalize()
      else:
        string+= token_list[i] +' '
        print(string)
    return string

def write_story(file_name, text, title, student_name, author, year):
  myfile = open(file_name, 'w+')
  for i in range(10):
    myfile.write('\n')
  string = title + ": " + str(year) + " , UNLEASHED\n" + student_name + ", inspired by " + author + "\nCopyright year publihed (" + str(year) + "), published: EngSci press\nFor exact formatting and spacing between character refer to test_write_story.txt"
  myfile.write(string)
  for i in range(17):
    myfile.write('\n')
  max = 0
  ult_max = [0]
  p =0
  k = 0
  j = 0
  for i in range(len(text)):
    while (i-ult_max[i]) <= 90:
      if text[i] == " ":
        max = i
    ult_max.append(max)
    j+=1
    myfile.write(text[ult_max[i]:max]+"\n")
    k +=1
    if k % 30 == 0:
      j = k / 30
      myfile.write('\n' + j + '\n')
      p +=1
    if p % 12 == 0:
      ch = p/12
      myfile.write("CHAPTER" + ch +"\n\n")
  myfile.close()
