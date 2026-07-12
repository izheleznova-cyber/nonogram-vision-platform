# Reverse Engineering Status

| Component | Status |
|-----------|--------|
| HTML structure | ✅ decoded |
| Passport format | ✅ decoded |
| JavaScript loader | ✅ decoded |
| Matrix E | ✅ located |
| Matrix F | ✅ decoded |
| Row hints N | ✅ decoded |
| Column hints O | ✅ decoded |
| Array d header | 🔄 under investigation |
| Array d records | 🔄 under investigation |

# Format of array `d`

## Purpose

This document describes the internal data format used by
https://www.nonograms.ru.

The format was reconstructed by reverse engineering
`nonogram.min.062.js`.

---

# Data flow

```
Excel

    ↓

Passport

    ↓

HTML page

    ↓

JavaScript

    ↓

var d

    ↓

Matrix E

    ↓

Hints N and O

    ↓

HTML table
```

---

# Variable d

The page contains a JavaScript variable

```javascript
var d = [
    ...
];
```

The array contains encoded information required to reconstruct
the puzzle.

The exact internal structure is still under investigation.

---

# Confirmed facts

## Every record has four integers

Example

```text
[221,185,140,198]
```

```text
[69,53,72,83]
```

```text
[67,58,183,95]
```

For puzzle 1039

```
records = 1081
```

Every record contains

```
4 integers
```

---

## The array is decoded by JavaScript

The site itself never stores the puzzle as HTML.

Instead

```
var d
```

is decoded by

```
nonogram.min.062.js
```

---

## Matrix E

The decoded puzzle is stored in

```javascript
E[row][column]
```

This matrix represents the solution of the puzzle.

Initialization

```javascript
for(w=0;w<C;w++)
    for(E[w]=[],F[w]=[],v=0;v<D;v++)
        E[w][v]=0;
```

---

## Matrix F

```
F
```

contains the current player state.

```
E = correct solution

F = player solution
```

---

## Row hints

Row hints are generated automatically.

```javascript
N[row]
```

Structure

```
[
    [length,color],
    [length,color],
    ...
]
```

Example

```
[[3,1],[2,2]]
```

---

## Column hints

Column hints are generated automatically.

```javascript
O[column]
```

Structure

```
[
    [length,color],
    [length,color],
    ...
]
```

---

## HTML generation

JavaScript generates the complete HTML table.

Cell ids

```
nmf{column}_{row}
```

Example

```
nmf10_5
```

Row hints

```
nmh{hint}_{row}
```

Column hints

```
nmv{column}_{hint}
```

---

## Reconstruction pipeline

The JavaScript performs

```
d

↓

E

↓

N

↓

O

↓

HTML
```

---

# Partially decoded section

The following fragment reconstructs matrix E.

```javascript
var V=Aa+5;

...

E[d[x][3]-Ia[3]-1][v] =
    d[x][2]-Ia[2];
```

Observations

```
d[x][1]
```

appears to describe the run length.

```
d[x][2]
```

appears to describe the color.

```
d[x][3]
```

appears to describe the row.

The first coordinate is still unknown.

---

# Unknown fields

The meaning of

```
d[x][0]
```

has not yet been determined.

The exact header format before

```
V=Aa+5
```

also remains unknown.

---

# Next steps

1. Decode the header.

2. Reconstruct matrix E entirely in Python.

3. Generate N and O without JavaScript.

4. Export Puzzle JSON.






Excel workbook
                           │
                           ▼
                     PassportRecord
                           │
                           ▼
                     HTML page
                           │
                           ▼
                    JavaScript page
                           │
                           ▼
                        var d
                           │
          ┌────────────────┴───────────────┐
          ▼                                ▼
    Header decoder                  Body decoder
          │                                │
          ▼                                ▼
     Puzzle metadata                  Matrix E
                                              │
                          ┌───────────────────┴───────────────────┐
                          ▼                                       ▼
                   Row hints N                            Column hints O
                          │                                       │
                          └──────────────┬────────────────────────┘
                                         ▼
                                 HTML generation



HTML identifiers 
Game field

nmf{column}_{row}

Example

nmf15_24



Horizontal hints

nmh{hint}_{row}
Vertical hints

nmv{column}_{hint}
Row id

l{row}

# Research Notes

The website does not store hints directly.

The hints are generated from matrix E.

Therefore only one structure needs to be decoded:

d

↓

E 

Everything else can be reconstructed automatically.

E

↓

N

↓

O 
The website does not store row and column hints. They are generated from the solution matrix E.






