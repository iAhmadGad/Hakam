# Hakam (Problem solving judge)

## Why Hakam?

As a problem solver, sometimes you might have slow internet connection, so you wait until your submission get tested, so why not testing your solutuon locally before you submit it?

## What does "Hakam" mean?

**"حكم"** is an arabic word means judge, and it is pronounced as **/ħakam/**.
but since there is no /ħ/ sound in english i just _latinised_ the name as **"Hakam"**.

## Install:

- prerequisites:
  - Make
  - PyInstaller
  - Python multiline module

```bash
git clone --depth 1 https://github.com/iAhmadGad/hakam.git && cd hakam && make install
```

## Manual:

### Test File:

Hakam depends on json files to compile your soltution code, execute it, and then test it.

here is an example:

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

- `execute` is the command used to execute your code. it is required

- `tests` is an array of 2-element arrays, where each [0] index of them is the input and the [1] index is the expected output, i.e. right answer.

### Create new testlistfile:

no need to write everything in the test file manually, Hakam will just handle this for you, just execute:

```bash
hakam new [testname]
```

- `[testname]` is optional, if given, the filename will be `[testname].json`, otherwise `hakam.json`

the result file will be as follows:

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

### Test your solution:

```bash
hakam test [testname]
```

- `[testname]` is optional, if given, the filename will be `[testname].json`, otherwise `hakam.json`