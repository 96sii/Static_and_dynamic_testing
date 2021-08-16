### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.:
Thinking that methods should be renamed or should be class level, or using string interpolation etc.

These aren't errors but rather standards that vary from developer to developer.

Only comment on errors that would stop the tests running.

```python

class CardGame: # There is no need to make this a class as it only contains methods. We don't create any instances of this class anywhere else.


  def check_for_ace(self, card):
    if card.value = 1: # Should use == and not =.
      return True
    else # Missing colon.
      return False


  dif highest_card(self, card1 card2): # Should be 'def' to define a function not 'dif'. There is also a comma missing between card 1 and card 2.
  if card1.value > card2.value: # Missing indentation on this line.
    return card # This should say 'card1' and not 'card'
  else:
    return card2



def cards_total(self, cards):
  total # Missing = 0.
  for card in cards:
    total += card.value
    return "You have a total of" + total # This line is indented slightly and needs to be pushed back to be in line with the previous for. You also Can't concantonate an integer.

```
