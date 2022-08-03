# SI 506 Midterm Review

## This review
In order to prepare you for the midterm coming up this thursday, I have created a series of exercises for us to go through. Starting with material from the beginning of the semster and covering more recent material as we go along.

## Background
In an alternate universe in which halloween is a thing this year, you and your friends, Mike, Jane, and Andy, are going trick-or-treating together.

## Problem 1
1. After stopping by the first few houses, your friend Jane asks you what you got in your candy bag. Your response is in the string `candy_str`. Using `candy_str`, create a list, called `candy_list` that contains the individual strings of each type of candy you recieved.

    :bulb: What method could you use to split up the string into a list?

    :bulb: Depending on how you implemented this, you might want to modify the last string in the list. How can you `replace` part of that string?
    * If you print `candy_list`, it should look like this:
        ```
        ['starburst', 'skittles', 'butterfinger', 'twix', 'candy corn', 'm&ms']
        ```

2. As you continue with your night of trick-or-treating, you get more candy to add to your bag. Add each of the following to the end of your `candy_list`:

    1. `'snickers'`
    2. `'candy corn'`
    3. `'a rock'`
    * If you print `candy_list`, it should look like this:
        ```
        ['starburst', 'skittles', 'butterfinger', 'twix', 'candy corn', 'm&ms', 'snickers', 'candy corn', 'a rock']
        ```

3. Did someone really give you a rock for halloween? Wow, that's rude. Remove the rock from your `candy_list`
    * If you print `candy_list`, it should look like this:
        ```
        ['starburst', 'skittles', 'butterfinger', 'twix', 'candy corn', 'm&ms', 'snickers', 'candy corn']
        ```

## Problem 2
1. Now that you have your list of candies, let's practice some list slicing.
    1. Create a (very creatively named) list called `first_three` that contains the first three candies in the candy list
        * If you print `first_three`, it should look like this:
            ```
            ['starburst', 'skittles', 'butterfinger']
            ```
    2. Create a list called `reverse` that contains a reversed version of `candy_list`
        * If you print `reverse`, it should look like this:
            ```
            ['candy corn', 'snickers', 'm&ms', 'candy corn', 'twix', 'butterfinger', 'skittles', 'starburst']
            ```
    3. Create a list called `every_other` that contains every other item in `candy_list`
        * If you print `every_other`, it should look like this:
            ```
            ['starburst', 'butterfinger', 'candy corn', 'snickers']
            ```

## Problem 3
1. The tuple `candy_bags` contains lists that represent the candy that Mike, Jane, and Andy got respectively. Unpack this tuple and assign the lists to three variables named `mikes_bag`, `andys_bag`, and `janes_bag`.
2. The creator of these practice exercises is very biased against candy corn and wants to create a function that judges different candies. 
    1. Create a function called `judge_candy` that takes in a string representing a type of candy as a required parameter. 
    2. `judge_candy` should check to see whether or not a given candy is `'candy corn'`, if not, it should print 
        ```
        {candy}? That's great!
        ```
    3. If the candy is not `'candy corn'`, `judge_candy` should print
        ```
        {candy}? How unfortunate!
        ```
    :bulb: `judge_candy` should `print`, not return
3. Now that we have a function that judges individual candies, let's create a function that judges entire bags of candy
    1. Create a function called `judge_bag` that takes in a list representing a bag of candy as a parameter
    2. `judge_bag` should go through each piece of candy in the `bag` list and judge whether or not it is candy corn

        :bulb: make use of the `judge_candy` function to make this judgement
    3. If you were to run `judge_bag` on `mikes_bag` the output should look like this:
        ```
        skittles? That's great!
        reeses cup? That's great!
        tootsie roll? That's great!
        hershey bar? That's great!
        candy corn? How unfortunate!
        ```


## Problem 4
1. Now let's create some functions that can separate the types of candy
    * For the purposes of this exercise, there are three types of candy:
        - chocolate: snickers, hershey bar, reeses cup
        - fruit: starburst, skittles, airheads
        - other: candy corn, tootsie roll
    1. Create a function called `sort_chocolate` that takes in a list representing a bag of candy as a parameter and `returns` a list of all of the chocolate candies in the bag
        * `sort_chocolate` should go through each piece of candy in the `bag` and check if it is a chocolate candy (snickers, hershey bar, or reeses cup)
        * If the candy is a chocolate candy, it should be added to the `chocolate` list
        * `sort_chocolate` should return a list of all of the chocolate candies in a bag
        * If you were to print the results of calling `sort_chocolate` on `mikes_bag`, the output should look like this:
            ```
            ['reeses cup', 'hershey bar']
            ```
    2. Sorting one type of candy is fine, but now let's try sorting every type of candy. Create a function called `sort_candy` that takes in a list representing a bag of candy as a parameter. `sort_candy` should return a tuple containing three lists, the first list should have all of the chocolate candies, the second list should have all of the fruit candies, and the third should have all of the other candies.
        * `sort_candy` should go through each piece of candy in the `bag` and check what kind of candy it is (chocolate, fruit, or other)

            :bulb: In 4.1, we created a list called `chocolate` and added to that list as we found chocolates. Perhapse we can take a similar approach for the other types of candy
        * Based on the type of candy that it is, it should be added to the appropriate list
        * `sort_candy` should return a tuple containing the candy lists
        * If you were to print the results of calling `sort_candy` on `mikes_bag`, the output should look like this:
            ```
            (['reeses cup', 'hershey bar'], ['skittles'], ['tootsie roll', 'candy corn'])
            ```
