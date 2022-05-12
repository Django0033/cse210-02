# Hilo Class Documentation

## Classes

### Card

> #### Attributes
>
> - number: int
>
> #### Methods
>
> - \_\_init\_\_(min, max): None
> - \_\_eq\_\_(obj): boolean
> - \_\_lt\_\_(obj): boolean
> - \_\_gt\_\_(obj): boolean

### Director

> #### Attributes
>
> - min_card: int
> - max_card: int
> - ask_h_or_l_func: function
> - right_guess_func: function
> - wrong_guess_func: function
> - same_number_func: function
>
> #### Methods
>
> - \_\_init\_\_(min_card, max_card, ask_h_or_l, right_guess, wrong_guess, same_number): None
> - next_play(): None

## Behavioral Relationship

| Main                      |                              | Director |               | Card                                     |
| ------------------------- | ---------------------------- | -------- | ------------- | ---------------------------------------- |
|                           | next_play()                  |          | Card(min,max) | \_\_init\_\_(min,max)                    |
|                           |                              |          | Card(min_max) | \_\_init\_\_(min,max)                    |
| input('Higher or lower?') | ask_h_or_l()                 |          |               |                                          |
|                           |                              |          |               | \_\_lt\_\_(), \_\_eq\_\_(), \_\_gt\_\_() |
| score += POINTS           | right_guess(), wrong_guess() |          |               |                                          |
| input('Play again?')      |                              |          |               |                                          |
