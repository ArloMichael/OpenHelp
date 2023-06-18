# OpenHelp

A Python module that uses the Stack Overflow API to help you with all your coding needs

## Installation

Clone the GitHub repository to your local machine:

``` console
git clone https://github.com/ArloMichael/OpenHelp.git
```

## Usage

To use the `find` function, first import it from the `openhelp` module:

``` python
from openhelp import find
```

Then, call the `find` function with your query string as its argument:

``` python
best_answer_texts = find("how to print hello world in python")
```

The `find` function will use the Stack Overflow API to search for questions and their corresponding answers that match your query string. It will then return a list of strings containing the text of the best answer(s) found.

You can then iterate over this list of answer texts and do whatever you need with them. For example, to print out each answer text:

``` python
for answer_text in best_answer_texts:
    print(answer_text)
```

This will print out each answer text on a new line.

## Example

Here's a complete example:

``` python
from openhelp import find

query = "how to print hello world in python"
best_answer_texts = find(query)
for answer_text in best_answer_texts:
    print(answer_text)
```
