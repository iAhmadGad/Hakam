# Hakam (Problem solving judge)

## Why Hakam?

As a problem solver, sometimes you might have slow internet, and waiting until your submission get tested might take longer than expected, you might even refresh your page a lot of times.

so why not testing your solutuon locally before you submit it?

## What does "Hakam" mean?

**Hakam**'s name derives from **"حَكَم"** which is an arabic word means judge, and it is pronounced as **/ħakam/**.
but since there is no /ħ/ sound in english i just _latinised_ the name as **"Hakam"**.

## What languages does Hakam support?

Any language that supports `stdin` & `stdout`.

## Install

- Prerequisites:
  - Make
  - PyInstaller
  - Python multiline module
  - In order to perform tests you should have the compiler or the interpreter of your language installed

```bash
git clone --depth 1 https://github.com/iahmadgad/hakam.git && cd hakam && make install
```

## Test File

Test file is a json file Hakam uses to compile، execute, and then test your solution code.

Here is an example of a test file:

```json
{
   "compile": "g++ solution.cpp"
   ,"execute": "./a.out"
   ,"tests":
   [
       ["8", "YES"]
       ,["5", "NO"]
   ]
}

```
- `compile` is the command used to compile your code before excuting it. in case your language is interpreted like Python you can just delete this key.

- `execute` is the command used to execute your code. **it is required.**

- `tests` is an array of 2-element arrays, where each [0] index of them is the input and the [1] index is the expected output, i.e. the right answer. **it is required.**

## Usage

```bash
hakam [candidate] <option>
```

### `new [testfile]` 

- `[testfile]` candidate is optional, if given, a file will be created with name `[testfile]`, otherwise the name will be literally `testfile.json`.

The file will be written as follows:

```json
{
    "compile": ""
    ,"execute": ""
    ,"tests":
    [
        ["", ""]
	,["", ""]
    ]
}
```

### `test [testfile] <option>`

- `[testfile]` is optional, if given, the file with name `[testfile]` will be tested, otherwise the file with name `testfile.json` will be tested.
- Until now there is no option but `--strict`, which makes Hakam exits if your code answered wrong or if runtime error is thrown.

Output should be something like this:
```
Compiling...
Executing...
0: Test Passed :)
1: Test Passed :)
2: Wrong Answer :^)
expected NO for input 2 not YES
Passed: 2
Wrong answers: 1
```
In case your code passed all the tests output should be something like this:
```
Compiling...
Executing...
0: Test Passed :)
1: Test Passed :)
2: Test Passed :)
Accepted
```
In case your code answered wrong and you chose `strict` option, Hakam won't proceed to perform tests, and output should be something like this:
```
Compiling...
Executing...
0: Wrong Answer :^)
expected YES for input 8 not NO
```
