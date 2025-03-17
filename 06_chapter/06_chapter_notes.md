# Notes for Chapter 6, Decision Structures

I've always wondered about:

```python
if __name__ == '__main__':
    main()
```

`__main__` is the name python gives to a script being run directly. You can test this by opening a python interactive shell and typing `__name__`: python will return `__main__`. So basically this statement is saying "check the value of `__name__` and execute the `main()` function if it's `__main__`.

The value of this is that you can write a script that you could either run directly or import as a function library. If you run it directly, the interpretor will give it a `__name__` of `__main__`, if you import it, it gets a different `__name__`, which is the name of the module/file. This gate stops the `main()` function from running if the module is imported.

## Sorting
* Decision tree algorithms don't scale particularly well and get complicated quickly.
* Sequential sorting (holding a `max_val` variable and adjusting it as you go through the list sequentially) scales well to large data sets
