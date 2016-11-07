def front_x(words):
  newlist = []
  none_x = []
  words_sorted = sorted(words)
  for x in words_sorted:
    if x[0] == 'x':
      newlist.append(x)
    else:
      none_x.append(x)
  final_sort = newlist + none_x
  return final_sort