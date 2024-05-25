# Poem Generator

This project generates a poem using a Markov chain-based random walk over the words in a text file. The text file can be a collection of sonnets, a book, or any other large text file.

## Prerequisites

- Python 3.x
- Make

## Files

- `poem.py`: Python script that generates the poem.
- `sonnets.txt`: Text file containing Shakespeare's sonnets.
- `Makefile`: Makefile for running the project.

## How to Run

1. Ensure you have Python 3.x installed on your machine.
2. Use the `Makefile` to run the project.

### Steps:

1. Open your terminal.
2. Navigate to the project directory.
3. Run the following command:

   ```sh
   $ make run
   ```

   This will execute the `poem.py` script and generate the poem.

## Example Output

```
from sullen sullen limits his thee,
you thee, limits sullen me thee,
fairest sullen his me hence thee,
you thy heaven hands you you
where thee, hands sullen fairest you
me whence me heaven fairest limits
you this fairest whence where me
sullen heaven thee, where heaven sullen
hence whence heaven hence me you
thee, limits heaven sullen where fairest
where hence hands fairest this me
hands thy me hands fairest heaven
hence limits thy fairest thy fairest
limits hands you fairest thy whence
thee, me whence thee, heaven whence...
```