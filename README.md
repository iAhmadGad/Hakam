# Hakam (Problem solving judge)

## Why Hakam?

As a problem solver, sometimes you might have slow internet, and waiting until your submission get tested may take longer than expected, you may refresh your page a lot of times as well.

so why not testing your solutuon locally before you submit it?

## What does "Hakam" mean?

**Hakam**'s name derives from **"حَكَم"** which is an arabic word means judge, and it is pronounced as **/ħakam/**.
but since there is no /ħ/ sound in english i just _latinised_ the name as **"Hakam"**.

## Install

- Prerequisites:
  - Make
  - PyInstaller
  - Python multiline module

```bash
git clone --depth 1 https://github.com/iAhmadGad/hakam.git && cd hakam && make install
```

## Manual

### Test File

Hakam reads json files to compile، execute, and then test your solution code.

Here is an example:

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

### Create new Test File

No need to write everything in the test file manually, Hakam will just handle this for you, just execute:

```bash
hakam new [testname]
```

- `[testname]` is optional, if given, the filename will be `[testname].json`, otherwise `hakam.json`.

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

### Test your solution

```bash
hakam test [testname] <option>
```

- `[testname]` is optional, if given, the filename will be `[testname].json`, otherwise `hakam.json`.
- Until now there is no option but `--strict`, which makes Hakam exits when your code answers wrong or if runtime error is thrown.

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
In case all your code passed all the tests output should be something like this:
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
