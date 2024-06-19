# Hakam (Problem solving judge)

## Why Hakam?

As a problem solver, sometimes you might have slow internet, and waiting until your submission get tested might take longer than expected, you might even refresh your page a lot of times.

so why not testing your solution locally before you submit it?

## What does "Hakam" mean?

**Hakam**'s name derives from **"حَكَم"** which is an arabic word means judge, and it is pronounced as **/ħakam/**.
but since there is no /ħ/ sound in english i just _latinised_ the name as **"Hakam"**.

## What languages does Hakam support?

Any language that supports `stdin` & `stdout`.

## Install

- Prerequisites:
  - Make
  - Python
  - PyInstaller
  - Python multiline module
  - In order to perform tests you should have the compiler or the interpreter of your language installed

```bash
git clone --depth 1 https://github.com/iahmadgad/hakam.git && cd hakam && make install
```

## Hakamfile

Hakamfile is a json file Hakam uses to compile، execute, and then test your solution code.

Here is an example of a Hakamfile:

```json
{
   "compile": "g++ solution.cpp",
   "execute": "./a.out",
   "tests":
   [
       ["8", "YES"],
       ["5", "NO"]
   ]
}

```
- `compile` is the command used to compile your code before excuting it. in case your language is interpreted like Python you can just delete this key.

- `execute` is the command used to execute your code. **it is required.**

- `tests` is an array of 2-element arrays, where each [0] index of them is the input and the [1] index is the expected output, i.e. the right answer. **it is required.**

## Usage

```bash
hakam [-h] {new,set,add,rm,test} ...
```

### `[-h, --help]`

prints usage

### `new [-h] [-f, --filename FILENAME] [-c, --compile command] [-e, --execute command] [-t, --tests number]`

- `[-f, --filename FILENAME]`: create file named `[FILENAME]`, if not given create file named `hakamfile.json`.
- `[-c, --compile command]`: command used to compile your code.
- `[-e, --execute command]`: command used to execute your code.
- `[-t, --tests number]`: number of tests, if given, Hakam will prompt you for each input & output.

The file will shoud be something like this:

```json
{
    "compile": "command"
    "execute": "command",
    "tests":,
    [
        ["input1", "output1"],
        ["input2", "output2"]
    ]
}
```

### `set [-h] [-f, --filename FILENAME] [-c, --compile command] [-e, --execute command] [-t, --tests number]`

- `[-f, --filename FILENAME]`: name of file to set values, if not given set values in file named `hakamfile.json`.
- `[-c, --compile command]`: command used to compile your code.
- `[-e, --execute command]`: command used to execute your code.
- `[-t, --tests number]`: number of tests, if given, Hakam will prompt you for each input & output, this will override any previous tests, if you already have tests and you want to add more, then use `add` instead.

### `add [-h] [-f, --filename FILENAME] [-c, --compile command] [-t, --tests number]`

- `[-f, --filename FILENAME]`: name of files to add values, if not given add values to file named `hakamfile.json`.
- `[-c, --compile command]`: command used to compile your code.
- `[-t, --tests number]`: number of tests, if given, Hakam will prompt you for each input & output, this won't override any previous tests.

### `rm [-h] [-f, --filename FILENAME] [-c, --compile command] [-t, --test index]`

- `[-f, --filename FILENAME]`: name of file to delete values from, if not given delete values from file named `hakamfile.json`.
- `[-c, --compile]`: command used to compile your code.
- `[-t, --test index]`: index of test to delete, index begins from 1 not 0.

### `test [-f, --filename FILENAME] [-s, --strict] [-v, --verbose]`

- `[-f, --filename FILENAME]`: test file named `[FILENAME]` , if not given test file named `hakamfile.json`.
- `[-s, --strict]`: exit if code answered wrong or if runtime error is thrown.
- `[-v, --verbose]` print tests & results.
Output should be something like this:

```bash
$ hakam test
Compiling...
Testing...
Passed: 2
Wrong answers: 1
```
with `--verbose`:
```bash
$ hakam test --verbose
Compiling...
Testing...
1: Test Passed :)
2: Test Passed :)
3: Wrong Answer :^)
expected NO for input 2 not YES
Passed: 2
Wrong answers: 1
```

In case your code passed all the tests output should be something like this:
```bash
$ hakam test
Compiling...
Testing...
Accepted
```

with `--verbose`:
```bash
$ hakam test --verbose
Compiling...
Testing...
1: Test Passed :)
2: Test Passed :)
3: Test Passed :)
Accepted
```

In case your code answered wrong and you chose `--strict` option, Hakam won't proceed to perform tests, and output should be something like this:
```bash
hakam test --strict
Compiling...
Testing...
1: Wrong Answer :^)
expected YES for input 8 not NO
```
