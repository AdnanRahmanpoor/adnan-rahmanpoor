---
publishDate: 2023-03-07 10:45:40
title: 'Day 1 of #100daysofphp: My Journey Begins'
excerpt: Diving into PHP. Day 1.
image: ~/assets/images/post-2/php.jpg
category: PHP
tags:
  - Programming
  - PHP
  - Foundations
  - Web development
---

## Diving into PHP

Welcome, fellow coding enthusiasts, to my blog post documenting my first steps in the exciting world of PHP! and beginning the #100DaysOfPHP and #100DaysOfCode. Today, we'll embark on a journey through the fundamentals of PHP, laying the groundwork for building interactive and dynamic web experiences.

### **What is PHP?**

Ever encountered a website that adjusts based on your actions? Perhaps an online store displaying products based on your searches, or a forum where users can interact and leave comments. These dynamic elements are often powered by PHP, a scripting language specifically crafted for web development.

### **Getting Started with PHP:**

**Setup**

*Regarding the setup of PHP, I will create a complete guide on how to start coding and working with it. Today we will go over the topics I learnt on day 1.*

**PHP**

PHP code resides in files with the `.php` extension. The primary file, often acting as the website's main view, is typically named `index.php`. Interestingly, PHP code isn't displayed directly on the webpage; instead, it works behind the scenes, seamlessly integrating with HTML to create interactive elements.

To identify PHP code, we use special tags:

```php
<?php
// Your code goes here
?>
```

**Printing Messages:**

Now, let's display a simple message on our website using the `echo` or `print` statements:

```php
<?php
  echo "Hello, World!"; // Output: Hello, World!

  print "Welcome to the wonderful world of PHP!"; // Output: Welcome to the wonderful world of PHP!
?>
```

**Introducing Variables:**

Imagine a box that can store and hold information. In PHP, these boxes are called variables. We use them to store various data, like names, numbers, or even messages. Variables always begin with a dollar sign (`$`) followed by a chosen name. Here's how we create and use a variable:

```php
<?php
  $name = "John";
  echo "Hello, " . $name . "!"; // Output: Hello, John!
?>
```

**Exploring Data Types:**

Just like our box can hold different items, variables can store various data types. Here are some common ones:

- **String:** Textual data, like names or messages (enclosed in quotes).
- **Integer:** Whole numbers (e.g., 1, 2, -10).
- **Float:** Numbers with decimal points (e.g., 3.14, -5.2).
- **Boolean:** True or False values, often used for making decisions.
- **Array:** Ordered lists of various data types, like a shopping list.
- **Object and Classes:** More complex data structures for advanced functionalities (beyond the scope of this post).
- **Null:** Represents the absence of a value, like an empty box.

Assigning values to variables follows a similar pattern:

```php
$string = "This is a string";
$number = 365;
$float = 0.1234;
$boolean = true;
$array = ["apple", "banana", 2];
// Object and Classes explained later
$null = null;
```

This blog post serves as a springboard for our PHP journey. By understanding the basics, we've equipped ourselves with the essential building blocks to create engaging and interactive web experiences. Stay tuned as we delve deeper into the world of PHP, exploring more advanced concepts and functionalities!
