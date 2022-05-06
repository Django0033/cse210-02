# Hilo Class Documentation

## Classes

### Card

> #### Attributes
>
> -   value: int
> -   guess: string
> -   points: int
>
> #### Methods
>
> -   draw(): None

### Director

> #### Attributes
>
> -   Card: Card
> -   is_playing: boolean
> -   score: int
> -   total_score: int
>
> #### Methods
>
> -   start_game(): None
> -   get_input(): None
> -   do_updates(): None
> -   do_outputs(): None

## Behavioral Relationship

| Main |              | Director |              | Card                      |
| ---- | ------------ | -------- | ------------ | ------------------------- |
|      | start_game() |          | draw()       |                           |
|      |              |          | get_input()  |                           |
|      |              |          |              | input('Higher or lower?') |
|      |              |          | draw()       |                           |
|      |              |          | do_updates() |                           |
|      |              |          | get_input()  |                           |
|      |              |          | get_input()  |                           |
|      |              |          |              | input('Play again?')      |
